from Stack import MyStack

class MinStack:
    # Constructor
    def __init__(self):
        self.min_stack = MyStack()
        self.main_stack = MyStack()

    # Removes and returns value from min_stack
    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

    # Pushes values into min_stack
    def push(self, value):
        self.main_stack.push(value)
        if self.min_stack.is_empty() or self.min_stack.peek() > value :
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.peek())
            
    # Returns minimum value from newStack in O(1) Time
    def min(self):
        if not self.min_stack.is_empty():
            return self.min_stack.peek()
        # In case the stack is empty
        return None


"""
Approach 1: Saving the min of stack in a variable for O(1) access
class MinStack:
    # Constructor
    def __init__(self):
        # Write your code here
        self.stack_list = []
        self.stack_size = 0
        self.minimum_of_stack = None

    def pop(self):
        self.stack_size -= 1
        self.stack_list.pop()
    # Pushes value into new stack
    def push(self, value):
        # Write your code here
        self.stack_size += 1
        self.stack_list.append(value)
        if not self.minimum_of_stack or self.minimum_of_stack > value:
            self.minimum_of_stack = value

    # Returns minimum value from new stack in constant time
    def min(self):
        print(self.minimum_of_stack)
        return self.minimum_of_stack

    
"""