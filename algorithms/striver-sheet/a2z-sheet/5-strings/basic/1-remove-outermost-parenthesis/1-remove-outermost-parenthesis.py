"""
Remove Outermost Parentheses

Problem Link:
https://leetcode.com/problems/remove-outermost-parentheses/

Statement
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses 
strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it 
into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where 
Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition 
of s.



Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '(' or ')'.
- s is a valid parentheses string.


Test Case:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"

Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

"""

"""
Time complexity: O(N)
Space complexity: O(N)
"""
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        result = ""
        
        for ch in s:
            if ch == "(" and count == 0:
                count += 1
            elif ch == "(" and count > 0:
                result += ch
                count += 1
            elif ch == ")" and count == 1:
                count -= 1
            elif ch == ")" and count > 1:
                result += ch
                count -= 1
            
        return result


            
            

