
"""
Linked List Cycle II

Problem Link:
https://leetcode.com/problems/linked-list-cycle-ii

Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.



Test Case:

Input: 4 -> 3 -> 2 -> 5 -> 8 -> back to 3 (loop)
Output: 3
"""

"""
Approach 1: 
Time Complexity: O(N)
Space Complexity: O(N)

# Using a set to store all the nodes and checking if that node is again being visited
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Write your code here
        memory_address = set()
        while head:
            if head in memory_address:
                return head
            memory_address.add(head)
            head = head.next
        
        return None
        

"""

"""
Approach 2: Fast and slow pointers / tortoise hare algorithm for finding entry of a loop in linked list
Time Complexity: O(N)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while slow and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while not slow == fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow

        
        return None
       
