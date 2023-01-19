from Node import Node

class LinkedList:
    def __init__(self):
        self.head_node=None

    def get_head(self):
        return self.head_node
    
    def is_empty(self):
        return True if not self.head_node else False
    
    def print_list(self):
        if(self.is_empty()):
            print("Linked List is empty")
            return False
        
        temp=self.head_node
        while temp is not None:
            print(temp.data)
            if temp.next_element is not None:
                print("->")
            else:
                print("-> None")
            temp = temp.next_element
        return True
