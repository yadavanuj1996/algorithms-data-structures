from Node import Node
from LinkedList import LinkedList
# O(n) search
def search(lst, value):
    # Write your code here
    current_node = lst.get_head()
    if current_node is None:
        return False    

    element_found = False
    while current_node is not None:
        if current_node.data == value:
            element_found = True
            break
        current_node = current_node.next_element
    print(element_found)
    return element_found