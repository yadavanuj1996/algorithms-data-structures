"""

Implement Queue using Stacks

Problem Link:
https://leetcode.com/problems/implement-queue-using-stacks/description/

Statement
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all
the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

otes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and 
is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list 
or deque (double-ended queue) as long as you use only a stack's standard operations.


Constraints:
- 1 <= x <= 9
- At most 100 calls will be made to push, pop, peek, and empty.
- All the calls to pop and peek are valid.

Test Case:
Input:
N/A

Output:
Simply implement the fns
"""

"""
Solution 1
Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque

class MyQueue:

    def __init__(self):
        self.stack_1 = deque()        
        self.stack_2 = deque()        

    def push(self, x: int) -> None:
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        
        self.stack_1.append(x)

        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        

    def pop(self) -> int:
        return self.stack_1.pop()
        

    def peek(self) -> int:
        return self.stack_1[-1]

    def empty(self) -> bool:
        return not self.stack_1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
