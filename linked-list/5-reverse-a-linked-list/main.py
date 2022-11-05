from Node import Node
from LinkedList import LinkedList

# Recursive approach
def reverse(lst):
  current_node = lst.get_head()
  if current_node is None:
    print(None)
    return

  prev_node = None
  while current_node is not None and current_node.next_element is not None:
    temp_node = current_node.next_element
    current_node.next_element = prev_node
    prev_node = current_node
    current_node = temp_node

  current_node.next_element = prev_node
  lst.head_node = current_node
  lst.print_list()


# Recursive approach
"""
def reverse(lst):
  current_node = lst.get_head()
  reverse_list(lst, current_node, None)
  lst.print_list()

def reverse_list(lst, current_node, prev_node):
  if not current_node:
    lst.head_node = prev_node
    return
  temp_node = current_node.next_element
  current_node.next_element = prev_node
  return reverse_list(lst, temp_node, current_node)
"""  