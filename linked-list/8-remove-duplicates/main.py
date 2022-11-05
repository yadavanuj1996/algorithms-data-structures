from LinkedList import LinkedList
from Node import Node

def remove_duplicates(lst):
    current_node = lst.get_head()
    if current_node and current_node.next_element:
        delete_duplicate_node(current_node.next_element, current_node, current_node.data)
    lst.print_list()

def delete_duplicate_node(current_node, prev_node, value):
    if not current_node:
        return

    if current_node and current_node.next_element:
        delete_duplicate_node(current_node.next_element, current_node, current_node.data)
        
    if current_node.data == value:
        prev_node.next_element = current_node.next_element
    else:
        prev_node = current_node

    delete_duplicate_node(current_node.next_element, prev_node,value)


lst = LinkedList()
lst.insert_at_tail(1)
lst.insert_at_tail(2)
lst.insert_at_tail(1)
lst.print_list()
remove_duplicates(lst)
lst.print_list()

"""
Approach 1 (Using simple recursion)
def remove_duplicates(lst):
    current_node = lst.get_head()
    if current_node and current_node.next_element:
        delete_duplicate_node(current_node.next_element, current_node, current_node.data)
    lst.print_list()

def delete_duplicate_node(current_node, prev_node, value):
    if not current_node:
        return

    if current_node and current_node.next_element:
        delete_duplicate_node(current_node.next_element, current_node, current_node.data)
        
    if current_node.data == value:
        prev_node.next_element = current_node.next_element
    else:
        prev_node = current_node

    delete_duplicate_node(current_node.next_element, prev_node,value)



"""