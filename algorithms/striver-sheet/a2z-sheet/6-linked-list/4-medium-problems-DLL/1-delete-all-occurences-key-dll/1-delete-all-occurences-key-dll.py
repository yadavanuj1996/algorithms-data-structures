"""
Delete all occurrences of a given key in a doubly linked list

Problem Link:
https://www.codingninjas.com/studio/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list_8160461

Statement
A doubly-linked list is a data structure that consists of sequentially linked nodes, and the nodes have 
reference to both the previous and the next nodes in the sequence of nodes.

You’re given a doubly-linked list and a key 'k'. Delete all the nodes having data equal to ‘k’.

Constraints:
- 0 <= n <= 100000
- 1 <= data in any node <= 10^9
- 1 <= k <= 10^9

Test Case:

Input: Linked List: 10 <-> 4 <-> 10 <-> 3 <-> 5 <-> 20 <-> 10 and ‘k’ = 10

Output: Modified Linked List: 4 <-> 3 <-> 5 <-> 20

Explanation: All the nodes having ‘data’ = 10 are removed from the linked list.
"""

"""
Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(1), since the algorithm uses only a constant amount of extra space regardless of the input size.
"""
class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def deleteAllOccurrences(head: Node, k: int) -> Node:
    # Write your code here
    cur_node = head

    while cur_node:
        if cur_node == head and cur_node.data == k:
            head = head.next
            cur_node = cur_node.next
            continue
        
        if cur_node.data == k:
            cur_node.prev.next = cur_node.next

        cur_node = cur_node.next
    
    return head
