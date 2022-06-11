SELECT 
    user_id,
    toStartOfWeek(time) week,
    count(distinct toDate(time)) lness
FROM simulator_20220420.feed_actions
GROUP BY 
    user_id,
    toStartOfWeek(time)
ORDER BY 
    user_id,
    week