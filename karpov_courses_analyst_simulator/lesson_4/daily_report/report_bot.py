import os

import telegram

from generate_report import get_data, get_plot, get_text


def send_report(chat: int = None):
    chat_id = chat or int(os.environ.get("REPORT_CHAT_ID"))
    # Создаем бота
    bot = telegram.Bot(token=os.environ.get("REPORT_BOT_TOKEN"))
    
    # Получение данных
    report_data = get_data()
    
    # Расчет текстовых метрик
    text_report = get_text(report_data)
    
    # Построение графика
    plot_object = get_plot(report_data)
    
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
