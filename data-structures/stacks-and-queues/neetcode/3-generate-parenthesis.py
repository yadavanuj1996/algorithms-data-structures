"""

Generate Parentheses

Problem Link:
https://leetcode.com/problems/generate-parentheses/

Statement
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Constraints:
- 1 <= n <= 8


Test Case:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]

"""

from collections import deque

# Time Complexity: O(n)
# Space Complexity O(n) 
# The size of the deque can grow a maximum up to a size of w.
class Solution:
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n: int) -> list[str]:
        self.generatePattern(n, 1, 0, "(")
        return self.result

    def generatePattern(self, n:int, no_of_left_brackets:int, no_of_right_brackets:int, pattern: str):
        if no_of_left_brackets < no_of_right_brackets or no_of_left_brackets > n or no_of_right_brackets > n:
            return
        elif no_of_left_brackets == n and no_of_right_brackets == n: 
            self.result.append(pattern)
            return
        
        self.generatePattern(n, no_of_left_brackets+1, no_of_right_brackets, pattern+'(')
        self.generatePattern(n, no_of_left_brackets, no_of_right_brackets+1, pattern+')')
    

def main():
    n = 3
    sol = Solution()
    print(sol.generateParenthesis(n))


if __name__ == "__main__":
    main()


"""
Solution Summary:

Algorithm Steps:
  1. Initialize an empty list to store the valid combinations, often denoted as `result`.
  2. Define a recursive function `generatePattern` with parameters:
     - `n`: Remaining number of pairs of parentheses.
     - `no_of_left_brackets`: Number of left parentheses used so far.
     - `no_of_right_brackets`: Number of right parentheses used so far.
     - `pattern`: Current combination of parentheses being formed.
  3. Base case:
     - If `no_of_left_brackets` and `no_of_right_brackets` are both equal to n, add `pattern` to `result`.
     - If `no_of_left_brackets` is greater than `no_of_right_brackets` and both are less than or equal to n:
       - Recursively call `generatePattern` with one more right parenthesis added to `pattern`.
       - Recursively call `generatePattern` with one more left parenthesis added to `pattern`.
  4. When the base case is met, all valid combinations will be added to the `result` list.
  5. Return the `result` list containing all valid combinations of parentheses.

Solution Video:
https://www.youtube.com/watch?v=s9fokUqJ76A
"""
