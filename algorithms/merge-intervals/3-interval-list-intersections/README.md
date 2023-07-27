
# Interval List Intersections

## Statement
For two lists of closed intervals given as input, interval_list_a and interval_list_b, where each interval has 
its own start and end time, write a function that returns the intersection of the two interval lists.

For example, the intersection of [3,8] and [5,10] is [5,8].

## Constraints:
- 0 ≤ interval_list_a.length, interval_list_b.length ≤ 1000
- 0 ≤ start[i] < end[i] ≤ 10^9, where i is used to indicate interval_list_a.
- end[i] < start[i + 1]
- 0 ≤ start[j] < end[j] ≤10^9, where j is used to indicate interval_list_b
- end[j] < start[j + 1]

## Test Case:
Input:
List 1 = [[2, 6], [7, 9], [10, 13], [14, 19], [20, 24]]
List 2 = [[1, 4], [6, 8], [15, 18]]
    
Output:
[[2, 4], [6, 6], [7, 8], [15, 18]]



<img width="767" alt="Screenshot 2023-07-27 at 6 37 10 PM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/09e00c37-e1a8-49d0-b58f-b0495d5fe924">



## Solution Summary
- Finding Intersections: The algorithm iterates through both lists simultaneously using two pointers, first and second. It compares intervals at these pointers to identify overlaps.

- Overlap Check: For each pair of intervals, it uses the are_intervals_overlapping function, which checks if two intervals overlap. If an overlap is found, the algorithm calculates the intersection and adds it to the result list.

- Intersection Calculation: To find the intersection of two overlapping intervals, the algorithm calculates the maximum of the start points and the minimum of the end points of the two intervals. This ensures that the intersection is a valid interval.

- Pointer Update: After processing the current intervals, the algorithm updates the pointers first and second based on the end points of the current intervals. The pointer with the smaller end point is incremented, as there can be no further overlaps with the other list for the current interval.

- Final Result: The algorithm continues this process until it reaches the end of either interval_list_a or interval_list_b. The result is a list of intersecting intervals, which is returned as the output.

![IMG_7783_2](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/60fdf261-8dfb-4167-b8fe-595dbbddbc77)


