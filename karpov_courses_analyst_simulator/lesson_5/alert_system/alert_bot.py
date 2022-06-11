import os
import io
import sys, traceback

import telegram
import matplotlib.pyplot as plt
import seaborn as sns

import config
from alert_system import check_alert
from read_db import Getch


def run_alert(chat: int = None):
    chat_id = chat or int(os.environ.get("REPORT_CHAT_ID"))
    # Создаем бота
    bot = telegram.Bot(token=os.environ.get("REPORT_BOT_TOKEN"))
    
    metric_config = config.metrics
    
    for metric in metric_config:
        # Достанем параметры из конфига
        time_col = metric.get('time_col', 'time_15')
        metric_col = metric.get('metric_col', 'active_users')
        hour_min_col = metric.get('hour_min_col', 'hour_min')
        a = metric.get('a', 1.5)
        chart_link = f'<a href="{metric["chart_link"]}">Ссылка на график</a>' if metric.get('chart_link', '') != '' else ''
        metric_name = metric.get('metric_name', 'unknown')
        slice_name = metric.get('slice', 'unknown')
        
        print(f"Metric {metric_name}: {slice_name}.")
        
        data_query = metric['sql_query']
        data = Getch(data_query).df
        
        if not data.shape[0]:
            print("Empty dataframe")
            continue
        
        is_anomaly, current_value, change = check_alert(
            data=data,
            time_col=time_col,
            metric_col=metric_col,
            hour_min_col=hour_min_col,
            a=a,
        )
        
        print(is_anomaly, current_value, change, data[time_col].iloc[-1])
        
        if is_anomaly:
            # Сообщение об аномалии
            alert_message = f"""Метрика <b>{metric_name}</b> в срезе <b>{slice_name}</b>.\n\nТекущее значение {current_value:.2f}. \nОтклонение более {change:.2%} от среднего за последние 2 недели.\n{chart_link} 
            """
            
            # Нарисуем график за последние 2 недели и отметим аномалию
            sns.set(rc={'figure.figsize': (20, 6), 'figure.dpi': 300}) 

            ax = sns.lineplot(
                data=data, 
                x=time_col, 
                y=metric_col, 
                )

            sns.scatterplot(
                data=data.tail(1), 
                x=time_col, 
                y=metric_col,
                color='r',
                )

            ax.set(xlabel='date')
            ax.set(ylabel=metric_name)

            ax.set_title(metric_name)
            ax.set(ylim=(0, None))
            
            # формируем файловый объект
            plot_object = io.BytesIO()
            ax.figure.savefig(plot_object)
            plot_object.seek(0)
            plot_object.name = f'{metric_name}.png'
            plt.close()

            # отправляем алерт
            # Отправка текста
            bot.send_message(chat_id=chat_id, text=alert_message, parse_mode='html')
            bot.send_photo(chat_id=chat_id, photo=plot_object)


print("Start check alert")
run_alert()
print("End check alert")

# try:
#     print("Start check alert")
#     run_alert()
#     print("End check alert")
# except Exception as e:
#     traceback.print_exc(file=sys.stdout)
