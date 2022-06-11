import pandas as pd


def check_alert(
    data: pd.DataFrame, 
    time_col: str, 
    metric_col: str, 
    hour_min_col: str, 
    a: float = 1.5
) -> (bool, float, float):
    # Проверка на аномалий 
    # Алгоритм проверки:
    # Берем 2-х недельную историю изменений значения текущей 15-ти минутки
    # Считаем по этим значениям квартили Q1 и Q3, находим межквартильный размах IQR
    # Находим предельную нижнюю и верхнюю границу допустимых значений метрики:
    # Q1 - a * IQR и Q3 + a * IQR
    
    
    if time_col not in data.columns:
        raise Exception(f"KeyError: '{time_col}' not in DataFrame")
    if metric_col not in data.columns:
        raise Exception(f"KeyError: '{metric_col}' not in DataFrame")
    if hour_min_col not in data.columns:
        raise Exception(f"KeyError: '{hour_min_col}' not in DataFrame")
        
    current_hour_min = data[hour_min_col].iloc[-1]
    curr_15_min_history = data[data[hour_min_col] == current_hour_min]
    
    # считаем статистику, не учитывая 15-минутуку, которую будем проверять на аномалию
    stat = curr_15_min_history[metric_col].iloc[:-1].describe()
    current_value = curr_15_min_history[metric_col].iloc[-1]
    iqr = stat['75%'] - stat['25%']
    
    low_boundary = stat['25%'] - a * iqr
    high_boundary = stat['75%'] + a * iqr
    
    # отклонение текущего значения от среднего
    change = abs(current_value / stat['mean'] - 1)
    
    if current_value < low_boundary or current_value > high_boundary:
        has_anomaly = True
    else:
        has_anomaly = False
        
    return has_anomaly, current_value, change
