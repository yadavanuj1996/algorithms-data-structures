
"""
Ninja’s Training

Problem Link:
https://www.codingninjas.com/studio/problems/ninja%E2%80%99s-training_3621003

Statement
Ninja is planing this ‘N’ days-long training schedule. Each day, he can perform any one of these three activities.
(Running, Fighting Practice or Learning New Moves). Each activity has some merit points on each day. As Ninja 
has to improve all his skills, he can’t do the same activity in two consecutive days. Can you help Ninja find 
out the maximum merit points Ninja can earn?

You are given a 2D array of size N*3 ‘POINTS’ with the points corresponding to each day and activity. 
Your task is to calculate the maximum number of merit points that Ninja can earn.

For Example
If the given ‘POINTS’ array is [[1,2,5], [3 ,1 ,1] ,[3,3,3] ],the answer will be 11 as 5 + 3 + 3.

Constraints:
- 1 <= T <= 10
- 1 <= N <= 100000.
- 1 <= values of POINTS arrays <= 100 .


Test Case:

Input:
1 2 5 
3 1 1
3 3 3

Output:
11

"""



"""
Time Complexity: O(N) 
Space Complexity: O(N )

"""
from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    
    memo = []
    for item in range(n):
        memo.append([-1, -1, -1])
    
    def get_max_point(i:int, j:int)->int:
        if i == n:
            return 0
        
        if not memo[i][j] == -1:
            return memo[i][j]
        
        child_indexes = [0,1,2]
        child_indexes.remove(j)
        
        temp_max = float("-inf")

        for child_index in child_indexes:
            temp = points[i][j] + get_max_point(i+1, child_index)
            temp_max = max(temp_max, temp)
        
        memo[i][j] = temp_max

        return memo[i][j]
    
    
    memo = [[-1, -1, -1] for item in range(n)]   
    result = float("-inf")
    for activity_no in range(3):
        result = max(result, get_max_point(0, activity_no))
    
    
    return result
    

    