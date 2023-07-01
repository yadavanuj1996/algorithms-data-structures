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

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
from linked_list import *

def palindrome(head):
    slow = get_middle_element(head)
    slow.next = reverse_linked_list(slow.next)

    first_half_iterator = head
    second_half_iterator = slow.next
 
    while second_half_iterator:
        if not first_half_iterator.data == second_half_iterator.data:
            return  False            
        
        first_half_iterator = first_half_iterator.next
        second_half_iterator = second_half_iterator.next

    
    return True
    
   

# Note this middle of linked list code is different than implemented in problem 3-middle-of-the-linked-lise
# In this problem if linked list has even nodes we will select the earlier one as mid.
def get_middle_element(head):
    slow = head
    fast = head
    size = 0
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        size = size + 1

    return slow


# This function reverse linked list and return the new head pointer
def reverse_linked_list(head):
    temp = None
    current_node = head
    while current_node:
        next_node = current_node.next
        current_node.next = temp
        temp = current_node
        current_node = next_node
    
    return temp

"""
def main():
    input_linked_list = LinkedList()
    input_linked_list.create_linked_list([1, 2, 3, 3, 2, 1])
    print(palindrome(input_linked_list.head))

if __name__ == "__main__":
    main()
"""

"""
Steps of solution:
- Initialize the slow and fast pointers to the head of the linked list.
- Traverse the linked list using both pointers at different speeds. At each iteration, the slow pointer increments by one node, and the fast pointer increments by two nodes.
- Continue doing so until the fast pointer reaches the end of the linked list. At this point, the slow pointer will be pointing to the middle of the linked list.
- Reverse the second half of the linked list and compare it with the first half.
- If both halves of the list match, the linked list is a palindrome. Otherwise, it is not.
"""