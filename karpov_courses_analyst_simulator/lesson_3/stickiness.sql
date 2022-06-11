select distinct 
    date, 
    dau / mau as stickiness
from (
    select 
        toDate(time) as date,
        count(distinct user_id) over (order by date range between 29 preceding and current row) as mau,
        count(distinct user_id) over (partition by date) as dau
    from simulator_20220420.feed_actions
)