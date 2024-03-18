"""
Reverse Stack Using Recursion

Statement
Reverse a given stack of 'N' integers using recursion. You are required to make changes in the input 
parameter itself.
Note: You are not allowed to use any extra space other than the internal stack space used due to recursion.

Constraints:
- 0 <= N <= 10^3, Where 'N' is the number of elements in the given stack.


Test Case:

Input: [1,2,3,4,5] 
Output: [5,4,3,2,1]
"""

"""
Time Complexity: O(N^2), for each element in recursion we call fit element for all n elements
Space Complexity: O(N),  due to recursion stack 

"""
from typing import List

def reverseStack(stack: List[int]) -> None:
    # Write your code here.
    def fit_element(stack, element):
        if not stack:
            stack.append(element)
        else:
            temp = stack.pop()
            fit_element(stack, element)
            stack.append(temp)

    def reverse_stack(stack):
        if not stack:
            return 
        
        temp = stack.pop()
        reverse_stack(stack)
        fit_element(stack, temp)

    reverse_stack(stack)
    return stack