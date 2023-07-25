
"""
Minimum Size Subarray Sum

Statement
Given an array of positive integers, nums, and a positive integer, target, find the minimum length of a 
contiguous subarray whose sum is greater than or equal to the target. If no such subarray is found, return 0.

Constraints:
- 1 ≤ target ≤ 10^9
- 1 ≤ nums.length ≤ 10^5
- 1 ≤ nums[i] ≤ 10^4

Test Case:
Input:
nums = [2,3,1,2,4,3]
target = 7
    
Output:
2
"""

import sys

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
def min_sub_array_len(target, nums):
    result_len = sys.maxsize
    l, r, sum = 0, 0, 0
    size = len(nums)

    while r < size:
        sum += nums[r]
        while sum >= target:
            if r - l + 1 < result_len:
                result_len = r - l + 1

            sum -= nums[l]
            l += 1
        
        r += 1
    # To handle the case when no such contiguous sub array is found
    if result_len == sys.maxsize:
        result_len = 0
        
    return result_len

def main():
    nums = [2,3,1,2,4,3]
    target = 7
    print(min_sub_array_len(target, nums))


if __name__ == "__main__":
    main()
    

"""
Solution Summary
- Initialize result_len to positive infinity and l, r, and sum to 0.
- Use a sliding window approach (l and r) to traverse the array from the left to the right.
- While r is less than the array size, do the following:
    - Add the element at r to the sum.
    - While the sum is greater than or equal to the target:
        - Update result_len as the minimum of result_len and the current subarray length (r - l + 1).
        - Subtract the element at l from the sum, and increment l.
    - Increment r to expand the subarray window.
- After the loop, if result_len remains infinity (never updated), set it to 0 to handle cases when no subarray with a sum greater than or equal to the target is found.
- Return the result_len as the minimum length of the subarray.
"""