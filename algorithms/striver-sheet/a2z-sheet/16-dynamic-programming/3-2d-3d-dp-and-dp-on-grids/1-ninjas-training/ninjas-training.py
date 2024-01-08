
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
Time Complexity: O(N),  Because we’ll be traversing the entire array twice.
Space Complexity: O(N ),  Because we’ll be creating an auxiliary array to store the maximum amount robbed for every house.

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if len(nums) == 1:
            return nums[0]
        
        def robMax(n, min_index, memo):
            if n < min_index:
                return 0
            
            if not memo[n] == -1:
                return memo[n]
            
            pick = nums[n] + robMax(n-2, min_index, memo)
            not_picked = 0 + robMax(n-1, min_index, memo)

            memo[n] = max(pick, not_picked)

            return memo[n]
            
        return max(
            robMax(n-1, 1, [-1] * (n)),
            robMax(n-2, 0, [-1] * (n))
        )
            