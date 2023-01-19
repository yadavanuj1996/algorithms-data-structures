# Linked List
- Python does not have a built-in linked list structure, we use lists for managing Linked List.
- Structure of A Singly Linked List 
![Screenshot 2022-11-05 at 2 36 54 PM](https://user-images.githubusercontent.com/22169012/200112260-6e6fe5ad-accb-4981-b7db-908ebc3b8acc.png)
  - Each node holds data along with a forward pointer to the next node in the list
  ```
  class Node:
    def __init__(self, data):
        self.data = data  # Data field
        self.next_element = None  # Pointer to next node
  ```
  - LinkedList Class
    - The linked list itself is a collection of Node objects which we defined above. To keep track of the list, we need a pointer to the first node in the list.
    - The implementation is fairly simple. When the list is first initialized it has no nodes, so the head is set to None.
    ```
    class LinkedList:
    def __init__(self):
        self.head_node = None  # Pointer to first node
    ```

## Linked Lists vs. Lists
![Screenshot 2022-11-05 at 2 42 35 PM](https://user-images.githubusercontent.com/22169012/200112496-8c185f02-0db4-4fbe-9f53-a0a89b9ad2fb.png)
- Insertion at tail for arrays like data structures is in O(n), but in python, the append method for lists is able to do it in O(1).
- Deletion at tail for arrays like data structures is in O(n), but in python, the pop method for lists is able to do it in O(1).

### Primary Operations in Linked List:
- get_head() - returns the head of the list
- insert_at_tail(data) - inserts an element at the end of the linked list
- insert_at_head(data) - inserts an element at the start/head of the linked list
- delete(data) - deletes an element with your specified value from the linked list
- delete_at_head() - deletes the first element of the list
- search(data) - searches for an element with the specified value in the linked list
- is_empty() - returns true if the linked list is empty



## Doubly Linked List
```
class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
        self.previous_element = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_head(self):
        if (self.head != None):
            return self.head.data
        else:
            return False

    def is_empty(self):
        if(self.head is None):  # Check whether the head is None
            return True
        else:
            return False

    def insert_tail(self, element):
        temp_node = Node(element)
        if(self.is_empty()):
            self.head = temp_node
            self.tail = temp_node
        else:
            self.tail.next_element = temp_node
            temp_node.previous_element = self.tail
            self.tail = temp_node
        self.length+=1
        return temp_node.data


    def remove_head(self):
        if(self.is_empty()):
            return False
        nodeToRemove = self.head;
        if (self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.head = nodeToRemove.next_element
            self.head.previous_element = None
            nodeToRemove.next_element = None
        self.length-=1
        return nodeToRemove.data
  

    def tail_node(self):
        if (self.head != None):
            return self.tail.data
        else:
            return False
   
    def __str__(self):
        val=""
        if(self.is_empty()):
            return ""
        temp = self.head
        val = "[" + str(temp.data) + ", "
        temp = temp.next_element

        while (temp.next_element):
            val = val + str(temp.data) + ", "
            temp = temp.next_element
        val = val + str(temp.data) + "]"
        return val

```
