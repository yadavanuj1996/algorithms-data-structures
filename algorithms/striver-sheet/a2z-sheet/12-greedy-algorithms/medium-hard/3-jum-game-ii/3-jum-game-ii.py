"""
Jump Game II

Problem Link:
https://leetcode.com/problems/jump-game-ii/

Statement
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you
are at nums[i], you can jump to any nums[i + j] where: 0 <= j <= nums[i] and i + j < n Return the minimum
number of jumps to reach nums[n - 1].  The test cases are generated such that you can reach nums[n - 1].


Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 1000
- It's guaranteed that you can reach nums[n - 1].


Test Case:

Input: nums = [2,3,1,1,4]
Output: 2

Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1,
then 3 steps to the last index.
"""
"""
Approach 1: Using recursion
Time complexity: O(N)
Space complexity: O(N)

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        def jump_step(s_ind, e_ind, steps):
            if e_ind >= n-1:
                return steps

            e_next_ind = -1

            for i in range(s_ind, e_ind+1, 1):
                if nums[i] + i > e_next_ind:
                    e_next_ind = nums[i] + i

            return jump_step(e_ind+1, e_next_ind, steps+1)  
               
        return jump_step(0, 0, 0)

            
        
"""

"""
Using Iteration
Time complexity: O(N), Note: we are using two loops but the while loop is just for condition check if you
notice that each item in array will only be visited once thus time complexity will be O(N)

Space complexity: O(1)
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        s_ind, e_ind = 0, 0
        steps = 0

        while e_ind < n-1:
            e_next_ind = -1

            for i in range(s_ind, e_ind+1, 1):
                if nums[i] + i > e_next_ind:
                    e_next_ind = nums[i] + i
            
            s_ind = e_ind+1
            e_ind = e_next_ind
            steps += 1
        
        return steps

            
            
            
