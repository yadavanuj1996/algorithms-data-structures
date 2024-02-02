"""
Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/description/

Statement:
Given the head of a singly linked list, return the middle node of the linked list. 
If there are two middle nodes, return the second middle node.

Test Case:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.


Constraints:
- The number of nodes in the list is in the range [1, 100].
- 1 <= Node.val <= 100

"""

"""
Time Complexity: O(N), where N is the number of nodes in the linked list.
Space Complexity: O(1), since the algorithm uses only a constant amount of extra space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        second = head

        while not (second == None or second.next == None):
            first = first.next
            second = second.next.next
        
        return first
        