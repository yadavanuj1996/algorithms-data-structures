
"""
Reverse Linked List

Link: https://leetcode.com/problems/reverse-linked-list/

Statement:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Test Case:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Constraints:

- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000


Tags: 
linked-list
"""

"""
Time Complexity: 
Space Complexity: 
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        prev_node = None
        current_node = head
        
        next_node = current_node.next
        
        while current_node:
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            next_node = current_node.next if current_node else None

        return prev_node
