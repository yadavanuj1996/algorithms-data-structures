"""
Sort linked list of 0s 1s 2s

Problem Link:
https://www.codingninjas.com/studio/problems/sort-linked-list-of-0s-1s-2s_1071937

Statement
Given a linked list of 'N' nodes, where each node has an integer value that can be 0, 1, or 2. You need to 
sort the linked list in non-decreasing order and the return the head of the sorted list.

Example:
Given linked list is 1 -> 0 -> 2 -> 1 -> 2. 
The sorted list for the given linked list will be 0 -> 1 -> 1 -> 2 -> 2.

Constraints:
- 1 <= N <= 10^3
- 0 <= data <= 2 

Test Case:

Sample Input 1:
7
1 0 2 1 0 2 1

Sample Output 1:
0 0 1 1 1 2 2

"""

"""
Time Complexity: O(N), Single iteration required
Space Complexity: O(1)
"""
'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''
        
def sortList(head):
    cur_node = head
    zero_head = Node(-1)
    zero = zero_head
    one_head = Node(-1)
    one = one_head
    two_head = Node(-1)
    two = two_head

    while cur_node:
        if cur_node.data == 0:
            zero.next = Node(cur_node.data)
            zero = zero.next
        elif cur_node.data == 1:
            one.next = Node(cur_node.data)
            one = one.next
        elif cur_node.data == 2:
            two.next = Node(cur_node.data)
            two = two.next
        
        cur_node = cur_node.next
    
    zero_head = zero_head.next
    zero.next = one_head.next
    one.next = two_head.next

    one_head = None
    two_head = None

    return zero_head

