from LinkedList import LinkedList
from Node import Node
# Floyd's Cycle-Finding Algorithm
def detect_loop(lst):
    # Write your code here
    current_node = lst.get_head()
    current_node_with_skip = lst.get_head()
    is_loop_detected = False
    while current_node and current_node_with_skip and current_node_with_skip.next_element:
        current_node = current_node.next_element
        current_node_with_skip = current_node_with_skip.next_element.next_element

        if current_node == current_node_with_skip:
            is_loop_detected = True
            break
    
    print(is_loop_detected)
    return is_loop_detected



"""
FIXME: FInd out why this approach does not work
detect loop using head 
def detect_loop(lst):
    # Write your code here
    is_loop_detected = False
    current_node = lst.get_head()
    current_node = current_node.next_element
    while current_node is not None:
        if current_node == lst.get_head():
            is_loop_detected = True
            break
        current_node = current_node.next_element
    
    print(is_loop_detected)
    return is_loop_detected


lst = LinkedList()
lst.insert_at_tail(1)
lst.insert_at_tail(2)
lst.insert_at_tail(3)
lst.print_list()
node_1 = lst.search(1)
node_3 = lst.search(3)
node_3.next_element=node_1
detect_loop(lst)


"""