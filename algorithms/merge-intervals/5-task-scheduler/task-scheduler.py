"""
Task Scheduler

Statement
We’re given a character array, tasks, where each character represents a unique task. These tasks need to be 
performed by a single CPU, with each task taking one unit of time. The tasks can be performed in any order.
At any given time, a CPU can either perform some task or stay idle.

For the given tasks, we are also provided with a positive integer value, n, which represents the cooling 
period between any two identical tasks. This means that the CPU must wait for at least n units of time before
it performs the same task again. For example, if we have the tasks [A,B,A,C] and n = 2, then after performing the first 
A task, the CPU will wait for at least 2 units of time to perform the second A task. During these 2 units of 
time, the CPU can either perform some other task or stay idle.

Given the two input values, tasks and n, find the least number of units of time the CPU will take to perform
the given tasks.

Constraints:
- 1 ≤ tasks.length ≤ 10000
- tasks consists of uppercase English letters.
- 0 <= n

Test Case:
Input:
Tasks = ["A", "B", "A", "A", "B", "C"]
n=3 

Output:
9
"""


"""
Time Complexity: O(m log m)
Space Complexity: O(m), where m is the number of unique tasks
"""
def least_time(tasks, n):
    idle_time = 0
    current = {}

    for task in tasks:
        current[task] = current.get(task, 0) + 1
    
    current = dict(sorted(current.items(), key=lambda x: x[1], reverse=True))
    max_freq_key = max(current, key=lambda x: current[x])
    max_freq = current[max_freq_key]
    del current[max_freq_key]
    # Max idle time 
    idle_time = (max_freq - 1) * n
    # Loop over each item except max element (as it is removed) and calculate idle_time
    for item in current:
        if idle_time <= 0:
            idle_time = 0
            break
        
        current_freq = current[item]
        idle_time = idle_time - min(max_freq-1, current_freq)
        

    total_tasks = len(tasks)
    return total_tasks + idle_time


def main():
    #tasks = ["A","B","A","A", "B", "C"]
    #n = 3
    tasks = ["A", "B", "C", "O", "Q", "C", "Z", "O", "X", "C", "W", "Q", "Z", "B", "M", "N", "R", "L", "C", "J"] 
    n = 10
    #tasks = ["A", "A", "A", "B", "B", "C", "C"]
    #n = 1
    print(least_time(tasks, n))

if __name__ == "__main__":
    main()
