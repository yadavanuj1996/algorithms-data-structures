"""
Sliding Window Maximum

Problem Link:
https://leetcode.com/problems/sliding-window-maximum/

Statement:
You are given an array of integers nums, there is a sliding window of size k which is moving from the very 
left of the array to the very right. You can only see the k numbers in the window. Each time the sliding 
window moves right by one position.

Return the max sliding window.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length


Test Case:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

"""

"""
# Brute force solution (THIS WILL NOT PASS ALL TEST CASES)

Time Complexity: O(n^2)
Space Complexity: O(n)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n-k+1):
            max_val = float("-inf")
            for j in range(k):
                max_val = max(max_val, nums[i+j])
            
            res.append(max_val)
        
        return res
"""
"""
Optimized Solution (All test cases passed), using decreasing deque approach
Time Complexity: O(n)
Space Complexity: O(n)
"""
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()
        
        for i in range(len(nums)):
            # before adding we are removing all the index whose values are less than newly 
            # added index value as we need to maintain a decreasing order deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # popping from head if the head index is less than window start value
            # here i-k-1 represents the current window start value
            window_start = i - (k - 1)
            while dq and dq[0] < window_start:
                dq.popleft()
            
            # Adding the head element in the result
            if i >= k-1:
                result.append(nums[dq[0]])
            
        return result