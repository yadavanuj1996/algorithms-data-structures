"""
TC: O(n)
SC: O(n)
"""
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for element in s:
            if len(stack) == 0:
                stack.append(element)
            else:
                if element == "}" and stack[-1] == "{" \
                    or element == ")" and stack[-1] == "(" \
                    or element == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(element)

        return len(stack) == 0
