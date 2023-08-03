"""
Reverse Linked List

Statement
Given the head of a singly linked list, reverse the linked list and return its updated head.

Constraints:
Let n be the number of nodes in a linked list.
- 1 <= n <= 500
- -5000 <= node.value <= 5000

Test Case:
Input:
6 → 8 → 7

Output: 
7 -> 8 -> 6

"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
from linked_list import LinkedList
from linked_list_node import LinkedListNode
            
def reverse(head):
    prev_node = None
    current_node = head
    next_node = current_node.next
    
    while current_node:
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
        next_node = current_node.next if current_node else None

    return prev_node


# This function reverse linked list and return the new head pointer
def reverse_linked_list(head):
    temp = None
    current_node = head
    while current_node:
        next_node = current_node.next
        current_node.next = temp
        temp = current_node
        current_node = next_node
    
    return temp

"""
- Solution Summary

- Initialize a temporary variable temp to None.
- Set current_node to the input head.
- While current_node is not None:
    - Save the next node of current_node into next_node.
    - Reverse the link of current_node to point back to the previous node (temp).
    - Update temp to be the current node.
    - Move current_node to the next node (next_node).
- Return temp as the new head of the reversed linked list.
"""

