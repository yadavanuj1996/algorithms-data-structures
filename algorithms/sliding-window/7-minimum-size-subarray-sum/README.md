# Minimum Size Subarray Sum

#### Leetcode Problem Link
https://leetcode.com/problems/minimum-size-subarray-sum/

## Statement
Given an array of positive integers, nums, and a positive integer, target, find the minimum length of a contiguous subarray whose sum is greater than or equal to the target. If no such subarray is found, return 0.

## Constraints:
- 1 ≤ target ≤ 10^9
- 1 ≤ nums.length ≤ 10^5
- 1 ≤ nums[i] ≤ 10^4

## Test Case:
Input:
nums = [2,3,1,2,4,3]
target = 7
    
Output:
2


## Solution Summary
- Initialize result_len to positive infinity and l, r, and sum to 0.
- Use a two-pointer approach (l and r) to traverse the array from the left to the right.
- While r is less than the array size, do the following:
    - Add the element at r to the sum.
    - While the sum is greater than or equal to the target:
        - Update result_len as the minimum of result_len and the current subarray length (r - l + 1).
        - Subtract the element at l from the sum, and increment l.
    - Increment r to expand the subarray window.
- After the loop, if result_len remains infinity (never updated), set it to 0 to handle cases when no subarray with a sum greater than or equal to the target is found.
- Return the result_len as the minimum length of the subarray.