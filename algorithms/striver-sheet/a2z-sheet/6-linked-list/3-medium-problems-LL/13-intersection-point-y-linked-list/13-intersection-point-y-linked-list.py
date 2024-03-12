
"""
Intersection of Two Linked Lists

Problem Link:
https://leetcode.com/problems/intersection-of-two-linked-lists

Statement
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

Constraints:
- The number of nodes of listA is in the m.
- The number of nodes of listB is in the n.
- 1 <= m, n <= 3 * 10^4
- 1 <= Node.val <= 10^5
- 0 <= skipA < m
- 0 <= skipB < n
- intersectVal is 0 if listA and listB do not intersect.
- intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Test Case:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'

"""

"""
Approach 1: Hashing / storing node memory address in unordered set
Time Complexity: O(n+m), Reason: Iterating through list 1 first takes O(n), then iterating through list 2 takes O(m). 
Space Complexity: O(n), Reason: Storing list 1 node addresses in unordered_set.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur_node_a = headA
        cur_node_b = headBN
        visited = set()

        while cur_node_a:
            visited.add(cur_node_a)
            cur_node_a = cur_node_a.next
        
        while cur_node_b:
            if cur_node_b in visited:
                return cur_node_b

            cur_node_b = cur_node_b.next
        
        return None

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Optimized approach with swapping iterating pointers to other heads approach
Time Complexity: O(n+m), where n & m are length of the 2 linked list respectivley.
Space Complexity: O(1),  No extra space required
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # edge case where either linked list is empty
        if not headA or not headB:
            return None

        cur_node_a = headA
        cur_node_b = headB

        while not cur_node_a == cur_node_b:
            cur_node_a = cur_node_a.next if cur_node_a else headB
            cur_node_b = cur_node_b.next if cur_node_b else headA

        return cur_node_a







        
       
