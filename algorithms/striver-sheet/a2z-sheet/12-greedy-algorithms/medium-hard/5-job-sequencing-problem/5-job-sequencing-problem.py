"""
Job Sequencing Problem

Problem Link:
https://www.naukri.com/code360/problems/job-sequencing-problem_1169460

Statement
You are given a 'Nx3' 2-D array 'Jobs' describing 'N' jobs where 'Jobs[i][0]' denotes the id of 'i-th' job, 
'Jobs[i][1]' denotes the deadline of 'i-th' job, and 'Jobs[i][2]' denotes the profit associated with 'i-th job'.

You will make a particular profit if you complete the job within the deadline associated with it. Each job
takes 1 unit of time to be completed, and you can schedule only one job at a particular time.

Return the number of jobs to be done to get maximum profit.

For Example :
'N' = 3, Jobs = [[1, 1, 30], [2, 3, 40], [3, 2, 10]].

All the jobs have different deadlines. So we can complete all the jobs.

At time 0-1, Job 1 will complete.
At time 1-2, Job 3 will complete.
At time 2-3, Job 2 will complete.

So our answer is [3 80].


Note :
If a particular job has a deadline 'x', it means that it needs to be completed at any time before 'x'.

Assume that the start time is 0.

Constraints:
- 1 <= 'N' <= 10^5
- 1 <= jobs[i][0] <= 'N'
- 1 <= jobs[i][1] <= 'N'
- 1 <= jobs[i][2] <= 10^3


Test Case:

Sample Input 1 :
4
1 2 30
2 2 40
3 1 10
4 1 10
Sample Output 1 :
2 70
"""

"""
Time complexity: 
Space complexity: 
"""
from os import *
from sys import *
from collections import *
from math import *

def jobScheduling(jobs):
    def sort_logic(arr):
        return arr[2]
    
    jobs.sort(key=sort_logic, reverse=True)

    max_deadline = -1
    job_count = 0
    profit = 0

    for item in jobs:
        max_deadline = max(max_deadline, item[1])
        
    deadline_arr = [False] * (max_deadline + 1)

    for item in jobs:
        deadline_time = item[1]
        while deadline_time > 0:
            if not deadline_arr[deadline_time]:
                deadline_arr[deadline_time] = True
                job_count += 1
                profit += item[2]
                break
            
            deadline_time -= 1
    
    return [job_count, profit]