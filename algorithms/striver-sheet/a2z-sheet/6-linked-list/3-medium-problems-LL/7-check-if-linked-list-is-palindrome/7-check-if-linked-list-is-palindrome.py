
"""
Palindrome Linked List

Problem Link:
https://leetcode.com/problems/palindrome-linked-list

Statement
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.



Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9

Test Case:

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false
"""

"""
Approach 1: Using an stack (to store the reverse of ll values in stack and compare it with the original list)
Time Complexity: O(N) , actually O(2N) as two iterations are taken but we will drop the constant factor
Space Complexity: O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = deque()
        cur_node = head
        # This loop will add the node values of linked list in reverse order in stack
        while cur_node:
            stack.append(cur_node.val)
            cur_node = cur_node.next
        
        cur_node = head
        while cur_node:
            if not cur_node.val == stack.pop():
                return False
                
            cur_node = cur_node.next
        
        return True
"""

"""
Approach 2
Time Complexity: O(N)
Space Complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    # simple recursive fn to reverse a linked link from a certain node
    def reverse_list(self, prev_node, cur_node):
        if not cur_node:
            # return the new head of the linked list
            return prev_node

        temp = cur_node.next
        cur_node.next = prev_node
        return reverse_list(cur_node, temp)
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # using tortoise and hare to find the middle node
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # compare the first half of linked list with the reversed second half of linked list
        tail = self.reverse_list(None, slow)
        cur_node = head
        res = True
        while tail:
            if not cur_node.val == tail.val:
                res = False
                break

            tail = tail.next
            cur_node = cur_node.next
        # once the comparision is over revert back the earlier reversed half linked list as we do 
        # want to change the input
        self.reverse_list(None, tail)
        
        return res
        

        
            
        