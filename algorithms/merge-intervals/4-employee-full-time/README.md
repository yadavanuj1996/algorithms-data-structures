# Employee Free Time

## Statement
You’re given a list containing the schedules of multiple employees. Each person’s schedule is a list of
non-overlapping intervals in sorted order. An interval is specified with the start and end time, both being 
positive integers. Your task is to find the list of intervals representing the free time for all the employees.

## Constraints:
- 1 ≤ schedule.length , schedule[i].length ≤ 50
- 0 ≤ interval.start < interval.end ≤ 10^8, where interval is any interval in the list of schedules.


## Test Case:
Input:
schedule = [ [[3, 5], [8, 10]], [[4, 6], [9, 12]], [[5, 6], [8, 10]] ]
    
Output:
[[6, 8]]



## Solution Summary:
- We store the start time of each employee’s first interval along with its index value and a value 0 into a min-heap.
- We set previous to the start time of the first interval present in a heap.
- Then we iterate a loop until the heap is empty, and in each iteration, we do the following:
  - Pop an element from the min-heap and set i and j to the second and third values, respectively, from the popped value.
  - Select the interval from input located at i,j.
  - If the selected interval’s start time is greater than previous, it means that the time from previous to the selected interval’s start time is free. So, add this interval to the result array.
  - Now, update the previous as max(previous, end time of selected interval).
  - If the current employee has any other interval, push it into the heap.
- After all the iterations, when the heap becomes empty, return the result array.

![IMG_8050_2](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/dbe6381c-186f-4481-87d9-32f24a53ac14)
