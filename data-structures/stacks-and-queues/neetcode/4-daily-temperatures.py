"""
Daily Temperatures

Problem Link:
https://leetcode.com/problems/daily-temperatures/

Statement
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100


Test Case:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

"""

from collections import deque

# Time Complexity: O(n)
# Space Complexity O(n) 
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        size = len(temperatures)
        result = [0] * size
        i = 0
        stack = deque()
        
        while i < size:
            if len(stack) and stack[-1][0] < temperatures[i]:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
                continue
            
            stack.append((temperatures[i], i))
            i += 1
        
        return result


def main():
    input = [73,74,75,71,69,72,76,73]
    sol = Solution()
    print(sol.dailyTemperatures(input))


if __name__ == "__main__":
    main()

"""
Solution Summary:

1. Initialize an empty stack and an output list `result`.
2. Iterate through the `temperatures` list.
3. While the stack is not empty and the current temperature is greater than the temperature at the index stored at the top of the stack:
   - Pop the index from the stack.
   - Update the result at the popped index with the difference between the current index and the popped index.
4. Push the current index onto the stack.
5. Continue this process for all elements in the `temperatures` list.
6. Return the `result` list containing the number of days until a warmer temperature for each day in the input list.


# Time and Space complexity explained:

Time complexity: O(n)
The while loop iterates through the "temperatures" list once, and each element is pushed and popped from the stack at most once. Therefore, the time complexity is linear, O(n), where n is the number of elements in the "temperatures" list.

Space complexity: O(n)
The space complexity is also O(n) because the additional data structures used, namely the "result" list and the "stack" deque, both can have a maximum of n elements in the worst case scenario, where n is the number of elements in the "temperatures" list.


# Solution Video:
https://www.youtube.com/watch?v=cTBiBSnjO3c
"""
