"""
Middle of the Linked List Problem

Statement:
Given the head of a singly linked list, return the middle node of the linked list. 
If the number of nodes in the linked list is even, there will be two middle nodes, so return the second one.


Constraints:
- head != Null

Test Case: 
Note: We have to return the node not the value that node contains
Input:
1 -> 2 -> Null

Output:
2
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

from linked_list import LinkedList

def get_middle_node(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow


def main():
    input_linked_list = LinkedList()
    input_linked_list.create_linked_list([1, 2, 3, 4, 5])
    head = input_linked_list.head
    print(get_middle_node(input_linked_list.head).data)

if __name__ == "__main__":
    main()



"""
Steps of solution
- Create two pointers, slow and fast, initially at the head of the linked list.
- Traverse the linked list while moving the slow pointer one step forward and the fast pointer two steps forward.
- When the fast pointer reaches the last node or NULL, the slow pointer will point to the middle node of the linked list.
- Return the node that the slow pointer points to.
"""