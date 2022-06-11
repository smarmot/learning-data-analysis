from datetime import datetime, timedelta

import pandahouse
import pandas as pd

from airflow.decorators import dag, task
from airflow.operators.python import get_current_context


connection_read = {
    'host': 'https://clickhouse...',
    'password': '',
    'user': '',
    'database': 'simulator_20220420'
}

connection_write = {
    'host': 'https://clickhouse...',
    'password': '',
    'user': ',
    'database': ''
}


def read_db(query: str, connection) -> pd.DataFrame:
    data = pandahouse.read_clickhouse(query, connection=connection)
    
    return data


default_args = {
    'owner': 'm.surkova',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2022, 5, 16),
}

schedule_interval = '0 23 * * *'


@dag(default_args=default_args, schedule_interval=schedule_interval, catchup=False)
def m_surkova_6_report_dag():
    @task()
    def extract_feed() -> pd.DataFrame:
        context = get_current_context()

        query = f"""
        SELECT 
          user_id, 
          sum(action = 'view') as views, 
          sum(action = 'like') as likes
        FROM simulator_20220420.feed_actions 
        WHERE toDate(time) = toDate('{context["ds"]}') - 1
        GROUP BY user_id"""

        feed_data = read_db(query=query, connection=connection_read)
        return feed_data
    
    
    @task
    def extract_messages() -> pd.DataFrame:
        context = get_current_context()

        query = f"""
        WITH sent as (
          SELECT 
            user_id,
            count(user_id) messages_sent, -- отсылает сообщений
            count(distinct reciever_id) users_sent -- скольким людям он пишет
          FROM simulator_20220420.message_actions snd
          WHERE toDate(time) = toDate('{context["ds"]}') - 1
          GROUP BY user_id
        )
        , received as (
          SELECT
            reciever_id,
            count(user_id) messages_received, -- сколько он получает
            count(distinct user_id) users_received -- сколько людей пишут ему
          FROM simulator_20220420.message_actions snd
          WHERE toDate(time) = toDate('{context["ds"]}') - 1
          GROUP BY reciever_id
        )

        SELECT 
          if(user_id = 0, reciever_id, user_id) user_id,
          messages_sent,
          users_sent,
          messages_received,
          users_received

        FROM sent
        FULL JOIN received 
          ON sent.user_id = received.reciever_id"""

        message_data = read_db(query=query, connection=connection_read)
        return message_data
    
    
    @task
    def extract_user_data() -> pd.DataFrame:
        context = get_current_context()
        query = f"""
        WITH users as (
            SELECT distinct user_id, gender, age, os
            from simulator_20220420.feed_actions 
            WHERE toDate(time) = toDate('{context["ds"]}') - 1

            UNION DISTINCT

            SELECT distinct user_id, gender, age, os
            from simulator_20220420.message_actions 
            WHERE toDate(time) = toDate('{context["ds"]}') - 1

            UNION DISTINCT

            SELECT distinct s.user_id, s.gender, s.age, s.os 
            from (
              SELECT DISTINCT s.user_id, s.gender, s.age, s.os  
              from simulator_20220420.message_actions r
              inner join simulator_20220420.message_actions s on s.user_id = r.reciever_id 
              WHERE toDate(r.time) = toDate('{context["ds"]}') - 1
            )
        )
        select * from users
         """
        user_data = read_db(query=query, connection=connection_read)
        
        return user_data
    
    
    @task
    def merge_data(feed_data: pd.DataFrame, message_data: pd.DataFrame, user_data: pd.DataFrame) -> pd.DataFrame:
        merged_data = (
            user_data
            .merge(feed_data, how='left', on='user_id')
            .merge(message_data, how='left', on='user_id')
            .fillna(0)
        )

        return merged_data
    
    
    @task
    def transform_by_gender(merged_data):
        stat_by_gender = (
            merged_data
            .groupby('gender')
            .sum()
            .drop(['user_id', 'age'], axis=1)
            .reset_index()
            .rename(columns={'gender': 'metric_slice'})
        )
        stat_by_gender['metric_name'] = 'gender'

        return stat_by_gender
    
    
    @task
    def transform_by_age(merged_data):
        stat_by_age = (
            merged_data
            .groupby('age')
            .sum()
            .drop(['user_id', 'gender'], axis=1)
            .reset_index()
            .rename(columns={'age': 'metric_slice'})
        )
        stat_by_age['metric_name'] = 'age'

        return stat_by_age
    
    
    @task
    def transform_by_os(merged_data):
        stat_by_os = (
            merged_data
            .groupby('os')
            .sum()
            .drop(['user_id', 'gender', 'age'], axis=1)
            .reset_index()
            .rename(columns={'os': 'metric_slice'})
        )
        stat_by_os['metric_name'] = 'os'

        return stat_by_os

        
    @task
    def prepare_df_to_load(stat_by_gender, stat_by_age, stat_by_os):
        final_stat = pd.concat([stat_by_gender, stat_by_age, stat_by_os])
        final_stat['event_date'] = datetime.strptime(get_current_context()['ds'], '%Y-%m-%d') - timedelta(days=1)

        col_order = ['event_date', 'metric_name', 'metric_slice', 'views', 'likes', 
                     'messages_received', 'messages_sent', 'users_received', 'users_sent']

        final_stat = final_stat[col_order]

        final_stat = final_stat.astype({
            'metric_name': str,
            'metric_slice': str,
            'views': int,
            'likes': int,
            'messages_received': int,
            'messages_sent': int,
            'users_received': int,
            'users_sent': int,
        })
        
        return final_stat[col_order]
    
    
    @task
    def load(final_stat):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS test.m_surkova_6_report
            (
                event_date String NOT NULL,
                metric_name String,
                metric_slice String,
                views Int64 NULL,
                likes Int64 NULL,
                messages_received Int64 NULL,
                messages_sent Int64 NULL,
                users_received Int64 NULL,
                users_sent Int64 NULL

            ) ENGINE = MergeTree ORDER BY (event_date)
        """
        pandahouse.execute(create_table_query, connection_write)
        pandahouse.to_clickhouse(df=final_stat, table='m_surkova_6_report', index=False, connection=connection_write)
        

    feed_data = extract_feed()
    message_data = extract_messages()
    user_data = extract_user_data()
    merged_data = merge_data(feed_data, message_data, user_data)
    
    stat_by_gender = transform_by_gender(merged_data)
    stat_by_age = transform_by_age(merged_data)
    stat_by_os = transform_by_os(merged_data)
    
    final_stat = prepare_df_to_load(stat_by_gender, stat_by_age, stat_by_os)
    
    load(final_stat)

    
m_surkova_6_report_dag = m_surkova_6_report_dag()
