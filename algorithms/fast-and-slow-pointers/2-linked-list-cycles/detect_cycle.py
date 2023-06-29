"""
Linked List Cycle Problem

Statement:
Check whether or not a linked list contains a cycle. If a cycle exists, return TRUE. Otherwise, return FALSE. 
The cycle means that at least one node can be reached again by traversing the next pointer.

Constraints:
Let n be the number of nodes in a linked list.
- 0 <= n <= 500
- -10^5 <= node.data <= 10^5
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

from linked_list import LinkedList

def detect_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast.next and fast.next.next:
        if slow == fast:
            return True
        
        fast = fast.next.next
        slow = slow.next
    return False

"""
def main():
    input_linked_list = LinkedList()
    input_linked_list.create_linked_list([2, 4, 6, 8])
    head = input_linked_list.head
    node = head
    temp_node = None
    while node.next is not None:
        if node.data == 4:
            temp_node = node
        node = node.next

    node.next = temp_node
    #print(input_linked_list)
    print(detect_cycle(input_linked_list.head))

if __name__ == "__main__":
    main()

"""

"""
Steps of solution
- Initialize both fast and slow pointers to the head of the linked list.
- Move the slow pointer one node ahead and the fast pointer two nodes ahead.
- Check if both pointers point to the same node at any point. If yes, then return TRUE.
- Else, if the fast pointer reaches the end of the linked list, return FALSE.
"""