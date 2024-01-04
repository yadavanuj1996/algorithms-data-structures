"""
Problem Statement
https://www.codingninjas.com/studio/problems/maximum-meetings_1062658?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

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











