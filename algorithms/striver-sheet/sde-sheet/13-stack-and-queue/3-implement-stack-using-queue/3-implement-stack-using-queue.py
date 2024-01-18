"""
Implement Stack using Queues

Problem Link:
https://leetcode.com/problems/implement-stack-using-queues/description/

Statement
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
- void push(int x) Pushes element x to the top of the stack.
- int pop() Removes the element on the top of the stack and returns it.
- int top() Returns the element on the top of the stack.
- boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, 
size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list 
or deque (double-ended queue) as long as you use only a queue's standard operations.


Constraints:
- 1 <= x <= 9
- At most 100 calls will be made to push, pop, top, and empty.
- All the calls to pop and top are valid.
 
Test Case:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]

Output
[null, null, null, 2, 2, false]
"""

"""
Time Complexity: O(N)
Space Complexity: O(N)
"""
from collections import deque

class MyStack:

    def __init__(self):
        self.queue_1 = deque()
        self.queue_2 = deque()

    def push(self, x: int) -> None:
        self.queue_2.append(x)
        while self.queue_1:
            self.queue_2.append(self.queue_1.popleft())
        # Swapping the q1 and q2
        temp = self.queue_1
        self.queue_1 = self.queue_2
        self.queue_2 = temp


    def pop(self) -> int:
        return self.queue_1.popleft()

    def top(self) -> int:
        return self.queue_1[0]

    def empty(self) -> bool:
        return not self.queue_1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()