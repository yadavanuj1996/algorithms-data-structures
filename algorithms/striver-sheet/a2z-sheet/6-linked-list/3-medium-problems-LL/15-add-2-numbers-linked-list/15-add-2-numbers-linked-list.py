
"""
Add Two Numbers

Problem Link:
https://leetcode.com/problems/add-two-numbers

Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9

Test Case:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""

"""
Time Complexity: O(max(m,n)), m is length of ll1 and n is length of ll2
Space Complexity: O(max(m,n))
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res_cur_node = None
        res_head = None

        while l1 or l2 or carry:
            sum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)

            carry = 1 if sum > 9 else 0
            sum = sum % 10 if sum > 9 else sum
            
            if not res_cur_node:
                res_cur_node = ListNode(sum)
                res_head = res_cur_node
            else:
                res_cur_node.next = ListNode(sum)
                res_cur_node = res_cur_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res_head
            