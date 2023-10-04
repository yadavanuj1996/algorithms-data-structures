"""
 Largest Rectangle in Histogram

Problem Link:
https://leetcode.com/problems/largest-rectangle-in-histogram

Statement
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Constraints:
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4


Test Case:

Input: heights = [2,4]
Output: 4

Input: heights = [2,1,5,6,2,3]
Output: 10

"""
"""
Time Complexity:** O(n) - Iterate through heights once.
Space Complexity:** O(n) - Stack stores at most n elements.
"""
from collections import deque

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = deque()
        max_area = 0

        for curr_index in range(len(heights)):
            curr_height = heights[curr_index]
            left_valid_index = curr_index

            while len(stack) and stack[-1][1] > curr_height:
                left_valid_index, value = stack.pop()
                max_area = max(max_area, ((curr_index - left_valid_index) * value))
                
            stack.append((left_valid_index, curr_height))
        
        
        curr_index += 1

        while len(stack):
            i, value = stack.pop()
            max_area = max(max_area, ((curr_index-i)* value))
            
        return max_area
                
    

def main():
    input = [2,1,5,6,2,3]
    sol = Solution()
    print(sol.largestRectangleArea(input))


if __name__ == "__main__":
    main()


"""
Solution Summary:

1. Initialize an empty stack and `max_area` variable (set to 0).
2. Iterate through heights:
    - While stack not empty and current height smaller than stack top:
        - Pop stack, calculate area, update `max_area`.
    - Push current index and height to stack.
3. After loop, while stack not empty:
    - Pop stack, calculate area, update `max_area`.
4. `max_area` holds the largest rectangle area.


Solution Video:
https://www.youtube.com/watch?v=X0X6G-eWgQ8
"""
