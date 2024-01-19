"""
Sort a Stack

Problem Link:
https://www.codingninjas.com/studio/problems/sort-a-stack_985275?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTabValue=PROBLEM

Statement
You’re given a stack consisting of 'N' integers. Your task is to sort this stack in descending order using recursion.

We can only use the following functions on this stack S.

is_empty(S) : Tests whether stack is empty or not.
push(S) : Adds a new element to the stack.
pop(S) : Removes top element from the stack.
top(S) : Returns value of the top element. Note that this function does not remove elements from the stack.

Note :
1) Use of any loop constructs like while, for..etc is not allowed. 
2) The stack may contain duplicate integers.
3) The stack may contain any integer i.e it may either be negative, positive or zero.


Constraints:
- 1 <= 'T' <= 100
- 1 <=  'N' <= 100
- 1 <= |'V'| <= 10^9

Test Case:

Input:
1
5
5 -2 9 -7 3

Output:
9 5 3 -2 -7

"""
from os import *
from sys import *
from collections import *
from math import *
"""
Time Complexity: O(N^2)
Space Complexity: O(N)
"""
def sortStack(stack):
    # given data structure is a python list 
    # as list have all the similar operations available so use them
    sort_stack(stack)
    
def sort_stack(stack):
    if not stack:
        return 
    
    temp = stack.pop()
    sort_stack(stack)
    fit_element(stack, temp)

def fit_element(stack, element):
    # Base case: if stack is empty
    if not stack:
        stack.append(element)
        return
    
    if stack[-1] < element:
        stack.append(element)
    else:
        temp = stack.pop()
        fit_element(stack, element)
        stack.append(temp)








    













