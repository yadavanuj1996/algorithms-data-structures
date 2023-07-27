
"""
Insert Interval

Statement
Given a sorted list of nonoverlapping intervals and a new interval, your task is to insert the new interval 
into the correct position while ensuring that the resulting list of intervals remains sorted and nonoverlapping.
 Each interval is a pair of nonnegative numbers, the first being the start time and the second being the end
time of the interval.

Constraints:
- 0 <= existing_intervals.length ≤ 10^4
- existing_intervals[i].length, new_interval.length == 2
- 0 ≤ start time, end time ≤ 10^4
- The first number should always be less than the second number in each interval.
- The list of intervals is sorted in ascending order based on the first element in every interval.

Test Case:
Input:
Existing Intervals = [ [1,3], [5, 7], [8, 9], [10, 13] ]
New Intervals = [2, 6]
    
Output:
[ [1,7], [8,9], [10,13] ]
"""

from interval import *

"""
Time Complexity: O(n), Actually it's O(n + n) = O(2n) = O(n)
Space Complexity: O(n)
"""
def insert_interval(existing_intervals, new_interval):
    result = []
    temp_interval = []
    start, end = 0, 0
    for item in existing_intervals:
        if new_interval and item.start <= new_interval.start:
            temp_interval.append(item)
        elif new_interval:
            temp_interval.append(new_interval)
            temp_interval.append(item)
            new_interval = None
        else:
            temp_interval.append(item)
    
    if new_interval:
        temp_interval.append(new_interval)

    intervals = temp_interval
    size = len(intervals)
    result = []
    current, next = 0,1 
    start, end = 0, 1

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
    #new_interval = [9, 11]
    intervals = [Interval(1, 6), Interval(8, 9), Interval(10, 15), Interval(16, 18)]
    new_interval = Interval(9, 10)
    insert_interval(intervals, new_interval)
    #for item in insert_interval(intervals, new_interval):
    #    print(item)

if __name__ == "__main__":
    main()



"""
Iteration 1

Time Complexity: O(n log n)
Space Complexity: O(n)

def insert_interval(existing_intervals, new_interval):
    result = []
    temp_interval = []
    start, end = 0, 0
    for item in existing_intervals:
        if new_interval and item.start <= new_interval.start:
            temp_interval.append(item)
        elif new_interval:
            temp_interval.append(new_interval)
            temp_interval.append(item)
            new_interval = None
        else:
            temp_interval.append(item)

    if new_interval:
        existing_intervals.append(new_interval)
        
    for item in temp_interval:
        print(item)

    #print(temp_interval)
    intervals = temp_interval
    size = len(intervals)
    result = []
    current, next = 0,1 
    start, end = 0, 1

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

"""