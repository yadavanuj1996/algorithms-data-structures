from LinkedList import LinkedList
from Node import Node

def insert_at_tail(lst, value):
    # Write - Your - Code
    new_node = Node(value)
    current_node = lst.get_head()
    if current_node is None:
        lst.head_node = new_node
    else:
        while current_node.next_element is not None:
            current_node = current_node.next_element
        current_node.next_element = new_node
    print(lst)
    return lst