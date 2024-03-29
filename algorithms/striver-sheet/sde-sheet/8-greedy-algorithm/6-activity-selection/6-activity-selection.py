"""
Maximum activities

Problem Link:
https://www.naukri.com/code360/problems/1062712

Statement
You are given N activities with their start time Start[] and finish time Finish[]. You need to tell the
maximum number of activities a single person can perform.

Note:
A person can only work on a single activity at a time. The start time of one activity can coincide with the
end time of another.


Constraints:
- 1 <= T <= 5
- 1 <= N <= (10^5)
- 0 <= Start[i] < Finish[i] <= (10^9)
- Time Limit: 1 sec

Test Case:

Sample Input 1:
2
4
1 6 2 4 
2 7 5 8 
3
1 1 1
4 5 9
Sample Output 1:
3
1

"""


"""
Time Complexity: O(N log N) , actually to be more precise O(2N) + O(N log N)
Space Complexity: O(N), N is length of start and finish array
"""
def maximumActivities(start, finish):
    # Write your Code here.
    n = len(start)
    tasks = []
    for i in range(n):
        tasks.append([start[i], finish[i]])
    
    def sort_logic(arr):
        return arr[1]
    
    tasks.sort(key=sort_logic)
    task_pos_count = 0        # task possible count
    cur_int_end = -1            # current interval end

    # cur task[0] contains start time and cur task[1] contains end time
    for cur_task in tasks:
        if cur_task[0] >= cur_int_end:
            task_pos_count += 1
            cur_int_end = cur_task[1]
        
    return task_pos_count