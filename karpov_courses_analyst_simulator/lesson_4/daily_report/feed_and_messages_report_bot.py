import os
import io
import sys, traceback

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import telegram

from read_db import Getch


def get_data() -> (pd.DataFrame, pd.DataFrame):
    feed_data_query = """
        SELECT
            distinct user_id,
            toDate(time) date
        FROM simulator_20220420.feed_actions
        WHERE dateDiff('day', toDate(time), toDate(today())) <= 7
            AND toDate(time) <> toDate(today())
    """

    feed_data = Getch(feed_data_query).df
    
    message_data_query = """
        SELECT
            distinct user_id,
            toDate(time) date
        FROM simulator_20220420.message_actions
        WHERE dateDiff('day', toDate(time), toDate(today())) <= 7
            AND toDate(time) <> toDate(today())
    """

    message_data = Getch(message_data_query).df
        
    return feed_data, message_data


def get_text(feed_data: pd.DataFrame, message_data: pd.DataFrame) -> str:
    last_date = feed_data['date'].max()

    feed_last_day = feed_data[feed_data['date'] == last_date]
    msg_last_day = message_data[message_data['date'] == last_date]
    
    text_message = f"""Отчет по Ленте и Сообщениям за {last_date.date()}\n
`Пользователи ленты             {feed_last_day['user_id'].nunique():,}
Пользователи сообщений         {msg_last_day['user_id'].nunique():,}
Использовали только ленту      {feed_last_day[~feed_last_day['user_id'].isin(msg_last_day['user_id'])]['user_id'].nunique():,}
Использовали только сообщения  {msg_last_day[~msg_last_day['user_id'].isin(feed_last_day['user_id'])]['user_id'].nunique():,}`
"""
    return text_message


def get_plot(feed_data: pd.DataFrame, message_data: pd.DataFrame) -> io.BytesIO:
    sns.set()
    
    report_date_begin = (pd.Timestamp('now') - pd.DateOffset(days=7)).date()
    report_date_end = (pd.Timestamp('now') - pd.DateOffset(days=1)).date()
    
    feed_agg_data = feed_data.groupby("date").agg({"user_id": "count"}).reset_index()
    msg_agg_data = message_data.groupby("date").agg({"user_id": "count"}).reset_index()
    
    feed_and_msg_agg_data = feed_agg_data.merge(msg_agg_data, on='date', suffixes=['_feed', '_msg'])
    feed_and_msg_agg_data['part_of_msg_users'] = feed_and_msg_agg_data['user_id_msg'] / feed_and_msg_agg_data['user_id_feed']
    
    annotation_xytext = (0, 0) # distance from text to points (x, y)
    annotatin_ha = 'center' # horizontal alignment can be left, right or center
    annotation_font_size = 9
    annotation_bbox = dict(boxstyle="round", fc="w", alpha=0.5)
    
    fig, axes = plt.subplots(3, 1, figsize=(8, 11), dpi=200)
    fig.suptitle(f"Report on {report_date_begin} – {report_date_end}", fontsize=15)
    fig.subplots_adjust(hspace=0.3)

    ############### Активные пользователи в ленте ###############
    sns.lineplot(
        ax=axes[0],
        data=feed_agg_data, 
        x='date', 
        y='user_id', 
        )

    axes[0].set(xlabel=None)
    axes[0].set(ylabel='Количество пользователей')


    for x, y in zip(feed_agg_data["date"], feed_agg_data["user_id"]):
        label = f"{y:,}"
        axes[0].annotate(
            label, # this is the text
            (x, y), # these are the coordinates to position the label
            size=annotation_font_size,
            textcoords="offset points", # how to position the text
            xytext=annotation_xytext, # distance from text to points (x, y)
            ha=annotatin_ha, # horizontal alignment can be left, right or center
            bbox=annotation_bbox,
        ) 

    axes[0].set_title("Активные пользователи в мессенджере")
    axes[0].set(ylim=(None, feed_agg_data['user_id'].max() * 1.03))


    ############### Активные пользователи в сообщениях ###############
    sns.lineplot(
        ax=axes[1],
        data=msg_agg_data, 
        x='date', 
        y='user_id', 
        )

    axes[1].set(xlabel=None)
    axes[1].set(ylabel='Количество пользователей')


    for x, y in zip(msg_agg_data["date"], msg_agg_data["user_id"]):
        label = f"{y:,}"
        axes[1].annotate(
            label, # this is the text
            (x, y), # these are the coordinates to position the label
            size=annotation_font_size,
            textcoords="offset points", # how to position the text
            xytext=annotation_xytext, # distance from text to points (x, y)
            ha=annotatin_ha, # horizontal alignment can be left, right or center
            bbox=annotation_bbox,
        ) 

    axes[1].set_title("Активные пользователи в ленте")
    axes[1].set(ylim=(None, msg_agg_data['user_id'].max() * 1.03))


    ############### Доля пользователей сообщений от пользователей ленты ###############
    sns.lineplot(
        ax=axes[2],
        data=feed_and_msg_agg_data, 
        x='date', 
        y='part_of_msg_users', 
        )

    axes[2].set(xlabel=None)
    axes[2].set(ylabel='Доля пользователей')


    for x, y in zip(feed_and_msg_agg_data["date"], feed_and_msg_agg_data["part_of_msg_users"]):
        label = f"{y:.2}"
        axes[2].annotate(
            label, # this is the text
            (x, y), # these are the coordinates to position the label
            size=annotation_font_size,
            textcoords="offset points", # how to position the text
            xytext=annotation_xytext, # distance from text to points (x, y)
            ha=annotatin_ha, # horizontal alignment can be left, right or center
            bbox=annotation_bbox,
        ) 

    axes[2].set_title("Активные пользователи в ленте")
    axes[2].set(ylim=(None, feed_and_msg_agg_data['part_of_msg_users'].max() * 1.03))

    # Sending picture
    plot_object = io.BytesIO()
    plt.savefig(plot_object)
    plot_object.name = 'test_plot.png'
    plot_object.seek(0)
    plt.close()
    
    return plot_object


def send_report(chat: int = None):
    chat_id = chat or int(os.environ.get("REPORT_CHAT_ID"))
    # Создаем бота
    bot = telegram.Bot(token=os.environ.get("REPORT_BOT_TOKEN"))
    
    # Получение данных
    feed_data, message_data = get_data()
    
    # Расчет текстовых метрик
    text_report = get_text(feed_data, message_data)
    
    # Построение графика
    plot_object = get_plot(feed_data, message_data)
    
    # Отправка текста
    bot.send_message(chat_id=chat_id, text=text_report, parse_mode='markdown')
    
    # Отправка графиков
    bot.send_photo(chat_id=chat_id, photo=plot_object)
    
try:
    print("Report start building")
    send_report()
    print("Report sent")
except Exception as e:
    print(e)
    traceback.print_exc(file=sys.stdout)
