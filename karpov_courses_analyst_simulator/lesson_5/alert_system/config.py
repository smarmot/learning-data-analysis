metrics = [
    {
        "metric_name": "Активные пользователи в ленте",
        "slice":  "All",
        "a": 4,
        "chart_link": "http://superset.lab.karpov.courses/r/916",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(distinct user_id) as active_users
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Активные пользователи в ленте",
        "slice": "OS – Android",
        "a": 4,
        "chart_link": "http://superset.lab.karpov.courses/r/917",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(distinct user_id) as active_users
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and os = 'Android'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Активные пользователи в ленте",
        "slice":  "OS – iOS",
        "a": 4,
        "chart_link": "http://superset.lab.karpov.courses/r/918",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(distinct user_id) as active_users
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and os = 'iOS'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Активные пользователи в ленте",
        "slice":  "Source – Organic",
        "a": 4,
        "chart_link": "http://superset.lab.karpov.courses/r/919",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(distinct user_id) as active_users
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and source = 'organic'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Активные пользователи в ленте",
        "slice":  "Source – Ads",
        "a": 4,
        "chart_link": "http://superset.lab.karpov.courses/r/920",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(distinct user_id) as active_users
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and source = 'ads'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Активные пользователи в ленте",
        "slice":  "Country – Russia",
        "a": 4,
        "chart_link": "",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(distinct user_id) as active_users
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and country = 'Russia'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Активные пользователи в ленте",
        "slice": "Country – Not Russia",
        "a": 4,
        "chart_link": "",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(distinct user_id) as active_users
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and country <> 'Russia'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    
    
    {
        "metric_name": "Активные пользователи в мессенджере",
        "slice":  "All",
        "a": 4.5,
        "chart_link": "",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(distinct user_id) as active_users
            FROM simulator_20220420.message_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Активные пользователи в мессенджере",
        "slice": "OS – Android",
        "a": 4.5,
        "chart_link": "",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(distinct user_id) as active_users
            FROM simulator_20220420.message_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and os = 'Android'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Активные пользователи в мессенджере",
        "slice":  "OS – iOS",
        "a": 4.5,
        "chart_link": "",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(distinct user_id) as active_users
            FROM simulator_20220420.message_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and os = 'iOS'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Активные пользователи в мессенджере",
        "slice":  "Source – Organic",
        "a": 4.5,
        "chart_link": "",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(distinct user_id) as active_users
            FROM simulator_20220420.message_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and source = 'organic'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Активные пользователи в мессенджере",
        "slice":  "Source – Ads",
        "a": 4.5,
        "chart_link": "",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(distinct user_id) as active_users
            FROM simulator_20220420.message_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and source = 'ads'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Активные пользователи в мессенджере",
        "slice":  "Country – Russia",
        "a": 4.5,
        "chart_link": "",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(distinct user_id) as active_users
            FROM simulator_20220420.message_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and country = 'Russia'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Активные пользователи в мессенджере",
        "slice": "Country – Not Russia",
        "a": 4.5,
        "chart_link": "",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(distinct user_id) as active_users
            FROM simulator_20220420.message_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and country <> 'Russia'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    
    
    {
        "metric_name": "Просмотры",
        "slice":  "All",
        "a": 4,
        "chart_link": "http://superset.lab.karpov.courses/r/932",
        "metric_col": "views",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as views
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and action = 'view'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Просмотры",
        "slice": "OS – Android",
        "a": 4,
        "chart_link": "",
        "metric_col": "views",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as views
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and action = 'view'
              and os = 'Android'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Просмотры",
        "slice":  "OS – iOS",
        "a": 4,
        "chart_link": "",
        "metric_col": "views",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as views
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and action = 'view'
              and os = 'iOS'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Просмотры",
        "slice":  "Source – Organic",
        "a": 4,
        "chart_link": "",
        "metric_col": "views",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as views
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and action = 'view'
              and source = 'organic'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Просмотры",
        "slice":  "Source – Ads",
        "a": 4,
        "chart_link": "",
        "metric_col": "views",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as views
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and action = 'view'
              and source = 'ads'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Просмотры",
        "slice":  "Country – Russia",
        "a": 4,
        "chart_link": "",
        "metric_col": "views",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as views
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and action = 'view'
              and country = 'Russia'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Просмотры",
        "slice": "Country – Not Russia",
        "a": 4,
        "chart_link": "",
        "metric_col": "views",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as views
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and action = 'view'
              and country <> 'Russia'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    
    
    {
        "metric_name": "Лайки",
        "slice":  "All",
        "a": 4,
        "chart_link": "http://superset.lab.karpov.courses/r/932",
        "metric_col": "likes",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as likes
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and action = 'like'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Лайки",
        "slice": "OS – Android",
        "a": 4,
        "chart_link": "",
        "metric_col": "likes",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as likes
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and action = 'like'
              and os = 'Android'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Лайки",
        "slice":  "OS – iOS",
        "a": 4,
        "chart_link": "",
        "metric_col": "likes",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as likes
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and action = 'like'
              and os = 'iOS'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Лайки",
        "slice":  "Source – Organic",
        "a": 4,
        "chart_link": "",
        "metric_col": "likes",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as likes
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and action = 'like'
              and source = 'organic'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Лайки",
        "slice":  "Source – Ads",
        "a": 4,
        "chart_link": "",
        "metric_col": "likes",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as likes
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and action = 'like'
              and source = 'ads'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Лайки",
        "slice":  "Country – Russia",
        "a": 4,
        "chart_link": "",
        "metric_col": "likes",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as likes
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and action = 'like'
              and country = 'Russia'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Лайки",
        "slice": "Country – Not Russia",
        "a": 4,
        "chart_link": "",
        "metric_col": "likes",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as likes
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and action = 'like'
              and country <> 'Russia'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    
    
    {
        "metric_name": "CTR",
        "slice":  "All",
        "a": 5,
        "chart_link": "http://superset.lab.karpov.courses/r/933",
        "metric_col": "CTR",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              countIf(action = 'like') / countIf(action = 'view') as CTR
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "CTR",
        "slice": "OS – Android",
        "a": 5,
        "chart_link": "",
        "metric_col": "CTR",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              countIf(action = 'like') / countIf(action = 'view') as CTR
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and os = 'Android'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "CTR",
        "slice":  "OS – iOS",
        "a": 5,
        "chart_link": "",
        "metric_col": "CTR",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              countIf(action = 'like') / countIf(action = 'view') as CTR
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and os = 'iOS'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "CTR",
        "slice":  "Source – Organic",
        "a": 5,
        "chart_link": "",
        "metric_col": "CTR",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              countIf(action = 'like') / countIf(action = 'view') as CTR
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and source = 'organic'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "CTR",
        "slice":  "Source – Ads",
        "a": 5,
        "chart_link": "",
        "metric_col": "CTR",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              countIf(action = 'like') / countIf(action = 'view') as CTR
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and source = 'ads'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "CTR",
        "slice":  "Country – Russia",
        "a": 5,
        "chart_link": "",
        "metric_col": "CTR",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              countIf(action = 'like') / countIf(action = 'view') as CTR
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and country = 'Russia'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "CTR",
        "slice": "Country – Not Russia",
        "a": 5,
        "chart_link": "",
        "metric_col": "CTR",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              countIf(action = 'like') / countIf(action = 'view') as CTR
            FROM simulator_20220420.feed_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and country <> 'Russia'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    
    
    {
        "metric_name": "Количество отправленных сообщений",
        "slice":  "All",
        "a": 4,
        "chart_link": "http://superset.lab.karpov.courses/r/934",
        "metric_col": "sent_messages",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as sent_messages
            FROM simulator_20220420.message_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Количество отправленных сообщений",
        "slice": "OS – Android",
        "a": 4,
        "chart_link": "",
        "metric_col": "sent_messages",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as sent_messages
            FROM simulator_20220420.message_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and os = 'Android'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Количество отправленных сообщений",
        "slice":  "OS – iOS",
        "a": 4,
        "chart_link": "",
        "metric_col": "sent_messages",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as sent_messages
            FROM simulator_20220420.message_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and os = 'iOS'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Количество отправленных сообщений",
        "slice":  "Source – Organic",
        "a": 4,
        "chart_link": "",
        "metric_col": "sent_messages",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as sent_messages
            FROM simulator_20220420.message_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and source = 'organic'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Количество отправленных сообщений",
        "slice":  "Source – Ads",
        "a": 4,
        "chart_link": "",
        "metric_col": "sent_messages",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as sent_messages
            FROM simulator_20220420.message_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and source = 'ads'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Количество отправленных сообщений",
        "slice":  "Country – Russia",
        "a": 4,
        "chart_link": "",
        "metric_col": "sent_messages",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as sent_messages
            FROM simulator_20220420.message_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and country = 'Russia'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
    {
        "metric_name": "Количество отправленных сообщений",
        "slice": "Country – Not Russia",
        "a": 4,
        "chart_link": "",
        "metric_col": "sent_messages",
        "sql_query": """
            SELECT
              toStartOfFifteenMinutes(time) time_15,
              formatDateTime(time_15, '%R') as hour_min,
              count(user_id) as sent_messages
            FROM simulator_20220420.message_actions
            where toStartOfFifteenMinutes(time) <> toStartOfFifteenMinutes(now())
              and dateDiff('minute', time, now()) <= 2 * 7 * 24 * 60 + 15
              and country <> 'Russia'
            group by toStartOfFifteenMinutes(time), formatDateTime(time_15, '%R')
            order by time_15
        """,
    },
]
