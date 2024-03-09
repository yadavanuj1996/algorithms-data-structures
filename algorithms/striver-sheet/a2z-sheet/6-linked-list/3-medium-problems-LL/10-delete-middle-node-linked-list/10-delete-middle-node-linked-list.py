
"""
Delete the Middle Node of a Linked List

Problem Link:
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

Statement
You are given the head of a linked list. Delete the middle node, and return the head of the modified
linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, 
where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 1 <= Node.val <= 10^5

Test Case:

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Input: head = [1,2,3,4]
Output: [1,2,4]

"""


"""
Approach 1: count the linked list length
Time Complexity: O(N),  accurately O(N+N/2)
Space Complexity: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # one node in linked list
        if not head.next:
            return None
        # Simple tortoise and hare algorithm with a twist of fast starting from 3rd node 
        # rather than head
        slow = head
        fast = head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head
"""

"""
Time Complexity: O(N),
Space Complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # one node in linked list
        if not head.next:
            return None
        # Simple tortoise and hare algorithm with a twist of fast starting from 3rd node 
        # rather than head
        slow = head
        fast = head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head