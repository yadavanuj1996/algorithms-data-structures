
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

"""
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
def employee_free_time(schedule):  
    temp_schedule = []
    for schedule_item in schedule:
        for item in schedule_item:
            temp_schedule.append(Interval(item.start, item.end))
    
    temp_schedule.sort(key=lambda x: x.start)

    merged_intervals_result = merge_intervals(temp_schedule)
    current = 0
    next = 1
    result = []
    while next < len(merged_intervals_result):
        result.append(Interval(merged_intervals_result[current].end, merged_intervals_result[next].start))
        current = next
        next += 1

    return result


def merge_intervals(intervals):
    size = len(intervals)
    result = []
    current, next = 0,1 
    
    while next < size:
        if intervals[current].start <= intervals[next].start <= intervals[current].end:
            intervals[current].start = min(intervals[current].start, intervals[next].start)
            intervals[current].end = max(intervals[current].end, intervals[next].end)

            next += 1 
            continue
    
        result.append(intervals[current])
        current = next
        next += 1
    
    result.append(intervals[current])

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
    #employee_free_time(schedule)
    for item in employee_free_time(schedule):
        print(item)

if __name__ == "__main__":
    main()


