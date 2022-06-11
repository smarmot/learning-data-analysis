select 
    toString(date) as date,
    toString(start_date) as start_date,
    count(user_id) as active_users
from (
    SELECT 
        user_id,
        min(toDate(time)) start_date
    FROM simulator_20220420.feed_actions
    GROUP BY user_id
    HAVING start_date >= today() - 20) t1
join (
    select distinct 
        user_id,
        toDate(time) date
    from simulator_20220420.feed_actions) t2 
using user_id

group by 
    date, 
    start_date