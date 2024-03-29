"""
Valid Parenthesis String

Problem Link:
https://leetcode.com/problems/valid-parenthesis-string/

Statement
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Constraints:
- 1 <= s.length <= 100
- s[i] is '(', ')' or '*'.

Test Case:

Input: s = "(*))"
Output: true

Input: s = "*((*"
Output: false

"""

"""
Time Complexity: O(N), actuall O(1.5N)
Space Complexity: O(N), actually O(2N)
"""
from collections import deque
# We have used stack based approach
class Solution:
    def checkValidString(self, s: str) -> bool:
        star_count = 0
        par_count = 0 
        left_par_index = []     # left parnthesis index STACK
        start_par_index = []    # start index STACK

        # for balancing all the right parenthesis
        for i in range(len(s)):
            if s[i] == "*":
                start_par_index.append(i)
            elif s[i] == "(":
                left_par_index.append(i)
            elif s[i] == ")":
                # first we will check if left paran exist, if it does we will pop it which means there
                # exist a left bracket on previous indexes for the current right bracket and we will
                # pop this left bracket so it cannot be used with any future right bracket
                if left_par_index:
                    left_par_index.pop()
                # if left bracket does not exist we will check till now if there is a valid star found
                # if it does we will assume is as a left bracket that satisfies current right bracket and
                # pop it as it cannot be used with any future right bracket
                elif start_par_index:
                    start_par_index.pop()
                else:
                    return False

        # for balancing all the left parenthesis
        while left_par_index:
            # for every remaning left bracket there should exists a star which comes after (to the right side)
            # of the current left bracket, as we will assume start to be a right bracket here to balance
            # current left bracket, Note: here we are checking if the start stack top (max index of star)
            # if it is still less than the current left bracket index that means the left index cannot be
            # balanced
            if not start_par_index or start_par_index.pop() < left_par_index.pop():
                return False
        
        return True