"""
Implement Queue using Arrays

Problem Link:
https://www.codingninjas.com/studio/problems/implement-queue-using-arrays_8390825?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

Statement
Queue is a linear data structure that follows the idea of First In First Out. That means insertion and
retrieval operations happen at opposite ends.

Implement a simple queue using arrays.

You are given 'query' queries which are either of the 2 types:

1 'e': Enqueue (add) element ‘e’ at the end of the queue.

2: Dequeue (retrieve) the element from the front of the queue. If the queue is empty, return -1.

You have been given ‘m’ operations which you need to perform in the stack. Your task is to implement all 
the functions of the stack.


Constraints:
- 1 <= ‘query’ <= 10^5
- 1 <= ‘e’ <= 10^6
- Both the enqueue() and dequeue() functions should solve in constant time, that is O(1) time complexity.

Test Case:
Input:


Output:
Simply implement the functions
"""

from typing import List

class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.arr= [0] * 100001
    
    #  Enqueue (add) element 'e' at the end of the queue.
    def enqueue(self, e: int) -> None:
        # Write your code here.
        self.arr[self.rear] = e
        self.rear += 1

    #  Dequeue (retrieve) the element from the front of the queue.
    def dequeue(self) -> int:
        # Write your code here.
        if self.front == self.rear:
            return -1
            
        self.front += 1
        return self.arr[self.front-1]
