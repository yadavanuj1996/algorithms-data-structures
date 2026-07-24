"""
TC: O(n)
SC: O(n) recursion stack
"""
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(first, second):
            if not second:
                return first

            temp = second.next
            second.next = first
            return reverse_list(second, temp)

        head = reverse_list(None, head)

        return head
