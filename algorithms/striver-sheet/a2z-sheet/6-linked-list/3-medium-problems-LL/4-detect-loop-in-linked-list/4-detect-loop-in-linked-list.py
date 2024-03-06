
"""
Linked List Cycle

Problem Link:
https://leetcode.com/problems/linked-list-cycle/

Statement
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of the
node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.


Test Case:

Input: 4 -> 3 -> 2 -> back to 3 (loop)
Output: true
"""

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = head
        second = head

        while first and second.next and second.next.next:
            first = first.next
            second = second.next.next

            if first == second:
                return True
        
        return False
              