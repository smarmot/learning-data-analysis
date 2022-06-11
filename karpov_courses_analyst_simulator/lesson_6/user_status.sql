WITH week_users as
     (SELECT distinct toMonday(time) week, user_id
      from simulator_20220420.feed_actions) 
      
      
select distinct 
    if(curr_w.user_id = 0, prev_w.week + 7, curr_w.week) week,
    if(curr_w.user_id = 0, prev_w.user_id, curr_w.user_id) user_id,
    multiIf(prev_w.user_id = 0, 'new', prev_w.user_id <> 0 and curr_w.user_id <> 0, 'retained', 'gone') user_status,
    if(curr_w.user_id = 0, -1, 1) user_counter
from week_users curr_w
full join week_users as prev_w 
    on prev_w.user_id = curr_w.user_id
    and prev_w.week + 7 = curr_w.week