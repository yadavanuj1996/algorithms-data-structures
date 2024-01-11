"""
Partition Equal Subset Sum

Problem Link:
https://leetcode.com/problems/partition-equal-subset-sum/description/

Statement
Given an integer array nums, return true if you can partition the array into two subsets such that the sum
of the elements in both subsets is equal or false otherwise.


Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100

Test Case:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

"""


"""
Solution 1: Memorization Solution

Time Complexity: O(N*S) + O(N), S is total sum of array, n is size of nums array, O(n) due to calculating total sum
Space Complexity: O(N*S) + O(S), where O(S) is auxilary space used for solving problem 

Note: I have not added tabulation approach this time
"""

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum = 0 
        n = len(nums)

        for item in nums:
            sum += item
        # An array cannot be divided into two sub sets (such that both array contain all the elements )
        # with both equal sum if original sum of array is an odd number 
        # (given that it contains integer values only)
        if not sum % 2 == 0:
            return False

        n = len(nums)
        target = sum // 2
        memo = [[-1 for i in range(target+1)] for j in range(len(nums))]

        def get_partition_sum_to_target(index, target):
            if target == 0:
                return True

            if index == 0:
                return nums[0] == target
                
            if target < 0:
                return False

            if not memo[index][target] == -1:
                return memo[index][target]
            
            # pick 
            pick = get_partition_sum_to_target(index-1, target-nums[index])
            #unpick
            unpick = get_partition_sum_to_target(index-1, target)

            memo[index][target] = pick or unpick
            return memo[index][target]

        return get_partition_sum_to_target(n-1, target)
