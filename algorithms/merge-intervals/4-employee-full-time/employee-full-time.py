
"""
Employee Free Time

Statement
You’re given a list containing the schedules of multiple employees. Each person’s schedule is a list of
non-overlapping intervals in sorted order. An interval is specified with the start and end time, both being 
positive integers. Your task is to find the list of intervals representing the free time for all the employees.

Constraints:
- 1 ≤ schedule.length , schedule[i].length ≤ 50
- 0 ≤ interval.start < interval.end ≤ 10^8, where interval is any interval in the list of schedules.


Test Case:
Input:
schedule = [ [[3, 5], [8, 10]], [[4, 6], [9, 12]], [[5, 6], [8, 10]] ]
    
Output:
[[6, 8]]

"""


from interval import *
import heapq
"""
Time Complexity: O(n log m), 
where n is the total number of intervals across all employees and m is the 
number of employees. This is because the heap can contain a maximum of k elements.

Space Complexity: O(m), 
where m is the number of employees.
"""
from interval import *
import heapq

def employee_free_time(schedule):  
    result = []
    min_heap = []
    
    size = len(schedule)
    for i in range(size):
        min_heap.append((schedule[i][0].start, i, 0))
        
    heapq.heapify(min_heap)
    # Get the first element start time
    previous = min_heap[0]
    while min_heap:
        current_interval_start, i , j = heapq.heappop(min_heap)
        if current_interval_start > previous[0]:
            result.append(Interval(schedule[previous[1]][previous[2]].end , schedule[i][j].start) )
        
        current_interval_end = schedule[i][j].end
        if previous[0] < current_interval_end:
            previous =  (current_interval_end, i , j)

        if j+1 < len(schedule[i]):
            min_heap.append((schedule[i][j+1].start, i, j+1))
            heapq.heapify(min_heap)

    
    return result



def main():
    #intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [18, 20]]
    """
    schedule = [
        [Interval(3, 5), Interval(8, 10)],
        [Interval(4, 6), Interval(9, 12)], 
        [Interval(5, 6), Interval(8, 10)]
    ]
    """
    schedule = [
        [Interval(1, 3), Interval(5, 6), Interval(9, 10)],
        [Interval(2, 4), Interval(7, 8)], 
        [Interval(8, 11), Interval(12, 14)]
    ]
    
    employee_free_time(schedule)
    
if __name__ == "__main__":
    main()


