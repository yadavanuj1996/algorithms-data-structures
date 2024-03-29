# Greedy Activity Selection Algorithm

The logic of the Greedy Activity Selection algorithm works because it leverages the greedy strategy of selecting activities that **end** earliest and ensuring that they do not overlap with previously selected activities. 

## Algorithm Summary

- Define a function `maximumActivities(start, finish)` to find the maximum number of non-overlapping activities.
- Create a list of activities with their start and finish times.
- Sort the activities based on their finish times in ascending order.
- Initialize two variables: `task_pos_count` to count the number of possible activities and `cur_int_end` to track the end time of the current interval.
- Iterate through the sorted activities:
  - Check if the start time of the current activity is greater than or equal to the end time of the current interval.
  - If it is, increment `task_pos_count` by 1 and update `cur_int_end` to the finish time of the current activity.
- Return `task_pos_count` as the maximum number of activities that can be performed without overlapping.

