select 
    toDate(activity.time) day,
    count(distinct activity.user_id) as active_users,
    count(distinct future_activity.user_id) as retained_users,
    count(distinct future_activity.user_id) / count(distinct activity.user_id) as retention
    
from simulator_20220420.feed_actions activity

left join simulator_20220420.feed_actions as future_activity 
    on activity.user_id = future_activity.user_id
    and toDate(activity.time) = toDate(future_activity.time) + interval 1 day
    
group by day