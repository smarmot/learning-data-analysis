import io

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from read_db import Getch


def get_data() -> pd.DataFrame:
    # Читаем данные
    # Запрос на подсчет метрик в ленте новостей с группировкой по дням за последнюю неделю (без текущего дня)
    report_query = """
    SELECT toStartOfDay(toDateTime(time)) AS date,
           count(DISTINCT user_id) AS "Уникальные пользователи",
           countIf(user_id, action = 'view') "Количество просмотров",
           countIf(user_id, action = 'like') "Количество лайков",
           round(countIf(user_id, action = 'like') / countIf(user_id, action = 'view'), 3) "CTR"
    FROM simulator_20220420.feed_actions

    WHERE dateDiff('day', toDate(time), toDate(today())) <= 7
      AND toDate(time) <> toDate(today())

    GROUP BY toStartOfDay(toDateTime(time))

    ORDER BY date
    """
    
    report_data = Getch(report_query).df
    return report_data


def get_text(report_data: pd.DataFrame) -> str:
    last_metrics = report_data.sort_values(by="date", ascending=False).iloc[0]
    
    report_date_end = (pd.Timestamp('now') - pd.DateOffset(days=1)).date()

    text_report = f"""Метрики за *{report_date_end}*
`DAU         {last_metrics['Уникальные пользователи']:,}
Просмотры   {last_metrics['Количество просмотров']:,}
Лайки       {last_metrics['Количество лайков']:,}
CTR         {last_metrics['CTR']:.2%}`"""
    
    return text_report
    

def get_plot(report_data: pd.DataFrame) -> io.BytesIO:
    # График с значениями метрик за предыдущие 7 дней:
    # - DAU 
    # - Просмотры
    # - Лайки
    # - CTR

    sns.set(font_scale=0.9)
    annotation_xytext = (0, 0) # distance from text to points (x, y)
    annotatin_ha = 'center' # horizontal alignment can be left, right or center
    annotation_font_size = 9
    annotation_bbox = dict(boxstyle="round", fc="w", alpha=0.5)
    
    report_date_begin = (pd.Timestamp('now') - pd.DateOffset(days=7)).date()
    report_date_end = (pd.Timestamp('now') - pd.DateOffset(days=1)).date()
    
    fig, axes = plt.subplots(4, 1, figsize=(8,13), dpi=300)
    fig.suptitle(f"Report on {report_date_begin} – {report_date_end}", fontsize=15)
    fig.subplots_adjust(hspace=0.5)


    ############### DAU ############### 
    sns.lineplot(
        ax=axes[0],
        data=report_data,
        x="date", 
        y="Уникальные пользователи",

    )
    axes[0].set_title("DAU")
    axes[0].set_xlabel("")

    # zip joins x and y coordinates in pairs
    for x, y in zip(report_data["date"], report_data["Уникальные пользователи"]):
        label = f"{y:,}"
        axes[0].annotate(
            label, # this is the text
            (x, y), # these are the coordinates to position the label
            size = annotation_font_size,
            textcoords="offset points", # how to position the text
            xytext=annotation_xytext, # distance from text to points (x, y)
            ha=annotatin_ha, # horizontal alignment can be left, right or center
            bbox=annotation_bbox,
        ) 

    ############### Просмотры ############### 
    sns.lineplot(
        ax=axes[1],
        data=report_data,
        x="date", 
        y="Количество просмотров",
    )
    axes[1].set_title("Просмотры")
    axes[1].set_xlabel("")

    for x, y in zip(report_data["date"], report_data["Количество просмотров"]):
        label = f"{y:,}"
        axes[1].annotate(
            label,
            (x, y),
            size = annotation_font_size,
            textcoords="offset points",
            xytext=annotation_xytext,
            ha=annotatin_ha,
            bbox=annotation_bbox,
        ) 

    ############### Лайки ############### 
    sns.lineplot(
        ax=axes[2],
        data=report_data,
        x="date", 
        y="Количество лайков",
    )
    axes[2].set_title("Лайки")
    axes[2].set_xlabel("")

    for x, y in zip(report_data["date"], report_data["Количество лайков"]):
        label = f"{y:,}"
        axes[2].annotate(
            label,
            (x, y),
            size = annotation_font_size,
            textcoords="offset points",
            xytext=annotation_xytext,
            ha=annotatin_ha,
            bbox=annotation_bbox,
        ) 

    ############### CTR ############### 
    sns.lineplot(
        ax=axes[3],
        data=report_data,
        x="date", 
        y="CTR",
    )
    axes[3].set_title("CTR")
    axes[3].set_xlabel("")

    for x, y in zip(report_data["date"], report_data["CTR"]):
        label = str(y)
        axes[3].annotate(
            label,
            (x, y),
            size = annotation_font_size,
            textcoords="offset points",
            xytext=annotation_xytext,
            ha=annotatin_ha,
            bbox=annotation_bbox,
        )  

    plot_object = io.BytesIO()
    plt.savefig(plot_object)
    plot_object.name = 'test_plot.png'
    plot_object.seek(0)
    plt.close()
    
    return plot_object
