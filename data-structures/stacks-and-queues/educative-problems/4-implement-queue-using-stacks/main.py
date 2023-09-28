from Stack import MyStack

class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        # Write your code here


    # Inserts Element in the Queue
    def enqueue(self, value):
        # Write your code here
        temp_stack = MyStack()
        while not self.main_stack.is_empty():
            temp_stack.push(self.main_stack.pop())
        
        self.main_stack.push(value)

        while not temp_stack.is_empty():
            self.main_stack.push(temp_stack.pop())
        
        return True

    # Removes Element From Queue
    def dequeue(self):
        # Write your code here
        return self.main_stack.pop()