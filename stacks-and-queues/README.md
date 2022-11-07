# Stack
In Python, there is pre-built Stack class by importing them into your program

### Operations
- push(element)
- pop()
- peek()
- is_empty()
- size()

## Code Implementation
```
class Stack:
  def __init__(self):
    self.stack_list = []
    self.stack_size = 0
    
  def is_empty(self):
    return self.stack_size == 0
    
  def peek(self):
    if self.is_empty():
      return None
     return self.stack_list[-1]
     
  def size(self):
    return self.stack_size
        
  
  def push(self, value):
    self.stack_size += 1
    self.stack_list.append(value)

  def pop(self):
    if self.is_empty():
      return None
    self.stack_size -= 1
    return self.stack_list.pop()

```

<img width="977" alt="Screenshot 2022-11-07 at 1 59 51 PM" src="https://user-images.githubusercontent.com/22169012/200262221-98896755-2d7b-4265-98c4-ad4facd44863.png">



## Queue
Queues are implemented in many ways. They can be represented by using lists, Linked Lists, or even Stacks. 
But most commonly lists are used as the easiest way to implement Queues.

With typical arrays, however, the time complexity is O(n) when dequeuing an element from the beginning of the queue.
This is because when an element is removed, the addresses of all the subsequent elements must be shifted by 1, which makes it less efficient. With linked lists and doubly linked lists, the operations become faster.


### Operations
- enqueue(element)
- dequeue()
- is_empty()
- front()
- rear()

```
from DoublyLinkedList import DoublyLinkedList

class MyQueue:
    def __init__(self):
        self.items = DoublyLinkedList()

    def is_empty(self):
        return self.items.length == 0

    def front(self):
        if self.is_empty():
            return None
        return self.items.get_head()

    def rear(self):
        if self.is_empty():
            return None
        return self.items.tail_node()

    def size(self):
        return self.items.length
    
    def enqueue(self, value):
        return self.items.insert_tail(value)

    def dequeue(self):
        return self.items.remove_head()

    def print_list(self):
        return self.items.__str__()
```

<img width="977" alt="Screenshot 2022-11-07 at 2 04 50 PM" src="https://user-images.githubusercontent.com/22169012/200263208-f909f945-0157-44d7-ba7e-01c2e051f0fd.png">


