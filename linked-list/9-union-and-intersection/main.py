from LinkedList import LinkedList
from Node import Node

# Returns a list containing the union of list1 and list2

def union(list1, list2):
    # Write your code here
    union_list = LinkedList()
    current_node = list1.get_head()
    while current_node:
        union_list.insert_at_tail(current_node.data)
        current_node = current_node.next_element

    current_node = list2.get_head()
    while current_node:
        union_list.insert_at_tail(current_node.data)
        current_node = current_node.next_element
    
    union_list.remove_duplicates()
    union_list.print_list()
    return union_list

# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    # Write your code here
    intersection_list = LinkedList()
    current_node = list1.get_head()
    while current_node:
        if list2.search(current_node.data):
            intersection_list.insert_at_tail(current_node.data)
        current_node = current_node.next_element
    intersection_list.print_list()
    return intersection_list

"""
list1 = LinkedList()
list1.insert_at_tail(1)
list1.insert_at_tail(2)
list1.insert_at_tail(3)

list2 = LinkedList()
list2.insert_at_tail(4)
list2.insert_at_tail(5)
list2.insert_at_tail(7)
list2.insert_at_tail(2)
list2.insert_at_tail(8)

intersection(list1, list2)
"""