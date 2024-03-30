### Intuition

val = [[1,3], [3,5], [2,3], [3,4], [1,2], [2,4]]
After sort
-> val = [[1,2], [1,3], [2,3], [3,4], [2,4], [3,5]]
-> val = [[1,2], [2,3], [3,4], [2,4], [3,5]]
-> val = [[1,2], [2,3], [3,4], [3,5]]
-> val = [[1,2], [2,3], [3,4]]

res will be updated to 3 after all the iterations

### Algorithm Steps
- Sort the given intervals based on the end time of each interval.
- Initialize variables `res` and `ind` to 0.
- Iterate through the sorted intervals using a while loop until `ind` is less than `len(intervals) - 1`.
  - Retrieve the end time of the current interval (`cur_interval_end`) and the start time of the next interval (`next_interval_start`).
  - Check if the start time of the next interval is less than the end time of the current interval, indicating an overlap.
    - If there's an overlap, remove the next interval by popping it from the list, increment `res` by 1, and continue to the next iteration.
  - If there's no overlap, increment `ind` by 1 to move to the next interval.
- Return the value of `res`, which represents the number of intervals removed to erase overlaps.

