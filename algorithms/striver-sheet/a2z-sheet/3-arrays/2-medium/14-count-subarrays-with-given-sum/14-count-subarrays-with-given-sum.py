"""
Subarray Sum Equals K

Problem Link:
https://leetcode.com/problems/subarray-sum-equals-k

Statement
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
1 <= 'N' <= 20
- Time limit: 1 second

Test Case:

Input: nums = [1,2,3,1,1,1], k = 3

Output: 3

"""



"""
Time Complexity: O(N) 
Space Complexity: O(N) 
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:   
        # Write your code here
        pre_sum = 0 # prefix sum
        old_pre_sums = {0: 1}
        count = 0
        for val in nums:
            pre_sum += val
            # updating the count
            count += old_pre_sums[pre_sum - k] if pre_sum - k in old_pre_sums else 0
            
            # add pre_sum to the old prefix sums dict
            old_pre_sums[pre_sum] = old_pre_sums[pre_sum] + 1 if pre_sum in old_pre_sums else 1

        return count
            