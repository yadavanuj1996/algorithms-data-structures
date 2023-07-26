# Merge Intervals

## Statement
We are given an array of closed intervals, intervals, where each interval has a start time and an end time.
The input array is sorted with respect to the start times of each interval. For example, 
intervals = [ [1,4], [3,6], [7,9] ] is sorted in terms of start times 1, 3 and 7.

Your task is to merge the overlapping intervals and return a new output array consisting of only the
non-overlapping intervals.


### Constraints:
- 1 ≤ intervals.length ≤ 10^4
- intervals[i].length = 2
- 0 ≤ start time ≤ end time ≤ 10^4

### Test Case:
Input:
intervals = [[1, 5], [3, 7] ,[4, 6], [6, 8]]
    
Output:
[[1,8]]

## Algorithm/ Solution Summary
- Initialize an empty list result to store the merged intervals.
- Use two pointers, current and next, to track the intervals being compared for merging.
- Use two variables, start and end, to keep track of the start and end points of intervals.
- Iterate through the intervals using a while loop until the next pointer reaches the end of the list.
- If the interval pointed by next overlaps with the interval pointed by current, merge them by updating the start and end points accordingly.
- If there is no overlap between the intervals, append the current interval to the result list, and move the pointers to the next interval.
- After the loop, add the last interval (or the only interval if there is only one) to the result list.
- Return the result list containing the merged intervals.