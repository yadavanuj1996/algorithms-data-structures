"""
Maximum meetings

Link: https://www.codingninjas.com/studio/problems/maximum-meetings_1062658?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

Problem Statement:
You are given the schedule of 'N' meetings with their start time 'Start[i]' and end time 'End[i]'.

You have only 1 meeting room. So, you need to return the maximum number of meetings you can organize.

The start time of one chosen meeting can’t be equal to the end time of the other chosen meeting.

Test Case:

Input:
6
1 3 0 5 8 5
2 4 6 7 9 9

Output:
4

Constraints:
- 1 <= 'N' <= 10^5
- 0 <= 'Start[i]' < 'End[i]' <= 10^9

"""

"""
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
from typing import List

def maximumMeetings(start: List[int], end: List[int]) -> int:
    # write your code here
    interval = []
    size = len(start)
    for i in range(len(start)):
        interval.append([start[i], end[i]])
    
    interval.sort(key=lambda x: x[0])
    if len(interval) == 1:
        return 1
    
    cur, next = 0, 1
    while next < len(interval):
        if interval[cur][0] <= interval[next][0] <= interval[cur][1]:
            if interval[cur][1] <= interval[next][1]:
                interval.pop(next)
                continue
            else:
                interval.pop(cur)
                continue
        
        cur += 1
        next +=1

    return len(interval)











