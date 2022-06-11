WITH reg as
 (SELECT user_id,
         min(toDate(time)) start_date,
         min(source) as source
  FROM simulator_20220420.feed_actions
  GROUP BY user_id
  HAVING start_date >= today() - 60
  AND start_date <= today() - 31),
  
activity as
 (SELECT distinct user_id,
                  toDate(time) as activity_date
  FROM simulator_20220420.feed_actions
  WHERE toDate(time) >= today() - 60 ),
  
cohort_size as
 (SELECT start_date,
         source,
         uniq(user_id) cohort_count_users
  FROM reg
  GROUP BY start_date,
           source) 

select reg.start_date,
  reg.source,
  min(cs.cohort_count_users) cohort_count_users,
  dateDiff('day', reg.start_date, activity_date) as diff_days,
  uniq(activity.user_id) count_returned_users,
  uniq(activity.user_id) / min(cs.cohort_count_users) retention
from reg
join cohort_size cs on cs.start_date = reg.start_date
  and cs.source = reg.source
left join activity 
  on activity.user_id = reg.user_id
  
where dateDiff('day', reg.start_date, activity_date) between 0 and 30
group by reg.source,
        reg.start_date,
        diff_days
order by reg.source,
        reg.start_date,
        diff_days