"""

Stack Implementation Using Array

Problem Link:
https://www.codingninjas.com/studio/problems/stack-implementation-using-array_3210209?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

Statement
Stack is a data structure that follows the LIFO (Last in First out) principle. Design and implement a stack to implement the following functions:

1. Push(num): Push the given number in the stack if the stack is not full.

2. Pop: Remove and print the top element from the stack if present, else print -1.

3. Top: Print the top element of the stack if present, else print -1.

4. isEmpty: Print 1 if the stack is empty, else print 0.

5. isFull: Print 1 if the stack is full, else print 0.


You have been given ‘m’ operations which you need to perform in the stack. Your task is to implement all the functions of the stack.
Constraints:
- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.

Test Case:
Input:
2 6
1 1
1 2
2
3
4
5

Output:
2 
1
0
0
"""
from sys import *
from collections import *
from math import *
from typing import List

class Stack:
    def __init__(self, n: int):
        # Write your code here
        self.arr = []
        self.max_length = n

    def push(self, num: int):
        # Write your code here
        if len(self.arr) < self.max_length:
            self.arr.append(num)

    def pop(self) -> int:
        # Write your code here
        return self.arr.pop() if self.arr else -1

    def top(self) -> int:
        # Write your code here
        return self.arr[-1] if self.arr else -1

    def isEmpty(self) -> int:
        # Write your code here
        return 1 if len(self.arr) == 0 else 0

    def isFull(self) -> int:
        return 1 if len(self.arr) == self.max_length else 0
        
