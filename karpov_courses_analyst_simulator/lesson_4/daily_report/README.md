# daily_report_feed

## Name
Daily Report feed

## Description
Скрипт для сборки отчета по ленте новостей и отправка отчета в телеграм-канал.

Отчет состоит из двух частей:
- текст с информацией о значениях ключевых метрик за предыдущий день
- график с значениями метрик за предыдущие 7 дней

Ключевые метрики: 
- DAU 
- Просмотры
- Лайки
- CTR


## Installation
Склонируйте репозиторий, задайте переменные окружения:
- REPORT_BOT_TOKEN – токен телеграм бота
- REPORT_CHAT_ID – id чата, в который необходимо отправлять отчет

## Usage
Для запуска используйте скрипт `report_bot.py`
```bash
export REPORT_CHAT_ID=<chat_id>
export REPORT_BOT_TOKEN=<telegram_bot_token>
python report_bot.py
```