from LinkedList import LinkedList
from Node import Node

# Function to find the nth node from end of Linked List
def find_nth(lst, n):
    # Write your code here
    result = None
    n = n-1
    current_node = lst.get_head()
    n_from_end_node = lst.get_head()

    for i in range(n):
        if not current_node or not current_node.next_element:
            result = -1
            break
            
        current_node = current_node.next_element

    if result == -1:
        print(result)
        return result
        
    while current_node:
        if not current_node.next_element:
            result = n_from_end_node
        current_node = current_node.next_element
        n_from_end_node = n_from_end_node.next_element
    
    print(result.data)
    return result.data

lst = LinkedList()
lst.insert_at_tail(22)

find_nth(lst, 3)