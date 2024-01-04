"""

Valid Parentheses

Problem Link:
https://leetcode.com/problems/valid-parentheses/

Statement
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Constraints:
- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.

Test Case:

Input: s = "()"
Output: true

Input: s = "(]"
Output: false

"""

from collections import deque

# Time Complexity: O(n)
# Space Complexity O(n) 
# The size of the deque can grow a maximum up to a size of w.

def isValid(s: str) -> bool:
    stack = deque()
    for curr_char in s:
        if not len(stack) == 0:
            if curr_char == "}" and stack[-1] == "{" or curr_char == ")" and stack[-1] == "(" or \
                curr_char == "]" and stack[-1] == "[":
                stack.pop()
                continue
        
        stack.append(curr_char)

    return len(stack) == 0

def main():
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(])"

    print(isValid(s3))


if __name__ == "__main__":
    main()


"""
Solution Summary:

- Initialize an empty stack (dequeue in python) data structure to keep track of opening symbols.
- Iterate through each character, `curr_char`, in the input string `s`:
  - If `curr_char` is a closing symbol and the stack is not empty:
    - Check if `curr_char` matches the corresponding opening symbol at the top of the stack.
    - If they match, pop the top element from the stack.
  - Otherwise, push `curr_char` onto the stack.
- After processing the entire string, if the stack is empty, return `True` (indicating a valid string).
- If the stack is not empty, return `False` (indicating an invalid string).

- The time complexity is O(n) because we iterate through the string once.
- The space complexity is O(n) in the worst case, where the stack can grow to n/2 elements.

Solution Video:
https://www.youtube.com/watch?v=WTzjTskDFMg
"""
