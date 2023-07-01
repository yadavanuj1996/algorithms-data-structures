"""
Palindrome Linked List Problem

Statement
Given the head of a linked list, your task is to check whether the linked list is a palindrome or not.
Return TRUE if the linked list is a palindrome; otherwise, return FALSE.

Constraints:
Let n be the number of nodes in a linked list.
- 1 <= n <= 500
- 0 <= node.value <= 9

Test Case:
Input:
7 → 3 → 3 → 3 → 7

Output: 
True

"""
from linked_list import LinkedList

def palindrome(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    revert_data = reverse_linked_list(slow)
    check = compare_two_halves(head, revert_data)

    revert_data = reverse_linked_list(revert_data)

    if check:
        return True
    return False


def compare_two_halves(first_half, second_half):
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        else:
            first_half = first_half.next
            second_half = second_half.next
    return True

# Template for traversing a linked list

def reverse_linked_list(slow_ptr):
    prev = None
    next = None
    curr = slow_ptr
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

"""
Steps of solution:
- Initialize the slow and fast pointers to the head of the linked list.
- Traverse the linked list using both pointers at different speeds. At each iteration, the slow pointer increments by one node, and the fast pointer increments by two nodes.
- Continue doing so until the fast pointer reaches the end of the linked list. At this point, the slow pointer will be pointing to the middle of the linked list.
- Reverse the second half of the linked list and compare it with the first half.
- If both halves of the list match, the linked list is a palindrome. Otherwise, it is not.
"""