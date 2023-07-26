# Merge Intervals

#### Leetcode problem link
https://leetcode.com/problems/merge-intervals
The leetcode solution is solved in the merge-intervals.py file in iteration 2, the solution for leetcode problem
is slightly different than the original solution.

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


#### All Cases
<img width="851" alt="Screenshot 2023-07-27 at 3 15 06 AM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/0495b4d6-4f72-4e72-84f7-72a3e311b3e8">


#### Cases that will arise in our problems
<img width="851" alt="Screenshot 2023-07-27 at 3 13 54 AM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/4a2a42cf-4181-48c6-b16b-47b5b25010bf">


<img width="851" alt="Screenshot 2023-07-27 at 3 14 09 AM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/ee26be86-963b-4b95-8a91-a5129d439a21">

![IMG_7774](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/e6fe6e96-6d1a-4f2b-bd78-bce17968e96b)



#### Leetcode solution 
```
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        size = len(intervals)
        result = []
        
        current, next = 0,1 
        start, end = 0, 1

        while next < size:
            if intervals[current][start] <= intervals[next][start] <= intervals[current][end]:
                intervals[current][start] = min(intervals[current][start], intervals[next][start])
                intervals[current][end] = max(intervals[current][end], intervals[next][end])

                next += 1 
                continue
        
            result.append(intervals[current])
            current = next
            next += 1
        
        result.append(intervals[current])

        return result

```



