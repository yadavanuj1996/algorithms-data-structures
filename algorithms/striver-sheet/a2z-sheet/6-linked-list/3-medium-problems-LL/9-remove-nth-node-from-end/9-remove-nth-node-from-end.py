
"""
Remove Nth Node From End of List

Problem Link:
https://leetcode.com/problems/remove-nth-node-from-end-of-list

Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Test Case:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []
"""


"""
Time Complexity: O(L),  accurately O(L)+O(L-N), We are calculating the length of the linked list and then iterating up to the (L-N)th node of the linked list, where L is the total length of the list.
Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_ll_count = 0
        cur_node = head
        while cur_node:
            total_ll_count += 1
            cur_node = cur_node.next
        
        if total_ll_count == n:
            head = head.next
            return head

        cur_node = head

        for _ in range (total_ll_count - n - 1):
            cur_node = cur_node.next
        
        cur_node.next = cur_node.next.next 

        return head
"""

"""
Time Complexity: O(N),  since the fast pointer will traverse the entire linked list, where N is the length of the linked list.
Space Complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next
        # Case to delete the first node of the linked list
        if not fast:
            head = head.next
            return head

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return head

