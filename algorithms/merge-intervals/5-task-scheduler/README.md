# Task Scheduler

## Statement
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

## Constraints:
- 1 ≤ tasks.length ≤ 10000
- tasks consists of uppercase English letters.
- 0 <= n

## Test Case:
Input:
Tasks = ["A", "B", "A", "A", "B", "C"]
n=3 

Output:
9

<img width="788" alt="Screenshot 2023-08-03 at 7 01 32 AM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/2c205e92-033e-46dd-b521-7f4d50ddc713">

## Solution Summary

- Create a dictionary current to store the frequency of each task in the input tasks list.
- Sort the current dictionary based on task frequency (descending order).
- Find the task with the highest frequency, max_freq, and remove it from the dictionary.
- Calculate the maximum idle time between tasks of the same type: idle_time = (max_freq - 1) * n.
- Iterate over the remaining tasks in the current dictionary and update idle_time based on their frequencies.
- Return the total time required to execute all tasks, considering the idle time: total_tasks + idle_time.

### Time and Space complexity:
- Time Complexity: O(m log m), where m is the number of unique tasks in the input list.
- Space Complexity: O(m), where m is the number of unique tasks in the input list.

![IMG_8302](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/cb73e844-f1de-42f1-9140-c25f8e520721)

![IMG_8303](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/a6027ee3-b688-43c5-ac6e-cb6ff6a0d698)

