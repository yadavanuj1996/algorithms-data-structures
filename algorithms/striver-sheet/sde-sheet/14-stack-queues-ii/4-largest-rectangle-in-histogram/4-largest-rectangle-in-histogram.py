"""
Largest Rectangle in Histogram

Problem Link:
https://leetcode.com/problems/largest-rectangle-in-histogram/

Statement:
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.


Constraints:
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4


Test Case:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

"""

"""
Time Complexity: O(N) 
Space Complexity: O(N)
"""
from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        dq = deque() 
        # adding an element at the end of arr
        heights.append(float("-inf"))
        n = len(heights)

        area = 0
        for i in range(n):
            while dq and heights[dq[-1]] > heights[i]:
                right_index = i
                cur_index = dq.pop()
                left_index = dq[-1] if dq else -1
                area = max(area, heights[cur_index]*(right_index-(left_index+1)))
            
            dq.append(i)

        # removing added element from the end of arr
        heights.pop()
        return area
                


















        