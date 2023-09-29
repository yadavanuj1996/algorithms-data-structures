"""

Min Stack

Problem Link:
https://leetcode.com/problems/min-stack/description/

Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.


Constraints:
- -231 <= val <= 231 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 104 calls will be made to push, pop, top, and getMin.

Test Case:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


"""

from collections import deque

# Time Complexity: O(1) for all operation as required in problem
# Space Complexity O(n) , where n is the number of elements pushed into the stack, as both the stack and min_stack deques will grow with the number of elements pushed into the stack.


from collections import deque

class MinStack:
    
    def __init__(self):
        self.min_stack = deque()    
        self.stack = deque()    

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.min_stack) == 0 or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack):
            return self.min_stack[-1]


"""
Solution Summary:

- The class uses two deques, `stack` and `min_stack`, to implement a stack with the ability to get the minimum element efficiently.
- `push(val)` adds an element to the stack (`stack` deque). It also updates the `min_stack` by appending the new value if it's smaller than the current minimum, or by appending the current minimum again.
- `pop()` removes the top element from both `stack` and `min_stack`.
- `top()` returns the top element from `stack` without modifying the stack.
- `getMin()` returns the minimum element from `min_stack`, which is the minimum element in the stack.

Complexities:
- Time Complexity: O(1) for all operations (push, pop, top, getMin).
- Space Complexity: O(n) where n is the number of elements pushed into the stack, due to the space required for both `stack` and `min_stack`.

Solution Video:
https://www.youtube.com/watch?v=qkLl7nAwDPo
"""
