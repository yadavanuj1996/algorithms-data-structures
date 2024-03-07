
"""
Find length of Loop

Problem Link:
https://www.codingninjas.com/studio/problems/find-length-of-loop_8160455

Statement
You’re given a linked list. The last node might point to null, or it might point to a node in the list,
thus forming a cycle.
Find out whether the linked list has a cycle or not, and the length of the cycle if it does.
If there is no cycle, return 0, otherwise return the length of the cycle.


Constraints:
- 1 <= n <= 100000
- 1 <= Data in linked list node <= 10^9
- 0 <= p <= n

Test Case:

Input: 
4
4 10 3 5
2

Output: 
3
"""

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.


def lengthOfLoop(head: Node) -> int:
    # Write your code here
    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # cycle exists case
        if slow == fast:
            cycle_len = 1
            slow = slow.next

            while not slow == fast:
                cycle_len +=1
                slow = slow.next
            
            return cycle_len

    
    return 0


    





