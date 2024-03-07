"""
Reverse Linked List (Recursive solution)

Problem Link:
https://leetcode.com/problems/reverse-linked-list

Statement
Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

Test Case:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

"""
Recursive solution
Time Complexity: O(N)
Space Complexity: O(1)
"""
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