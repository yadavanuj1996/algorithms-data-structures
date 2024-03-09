Sure, here's a succinct summary of the algorithm for a GitHub readme:

- **Algorithm**: Remove Nth Node From End of List
- **Input**: 
  - `head`: Head node of a singly-linked list.
  - `n`: Position of the node to remove from the end of the list.
- **Output**: 
  - Head of the linked list after removal.

**Steps**:

1. Initialize two pointers, `slow` and `fast`, both pointing to the head of the linked list.
2. Move the `fast` pointer n steps ahead.
3. Handle the case where the node to be removed is the head of the linked list:
   - If `fast` becomes `None`, set the head to head.next and return.
4. Move both `slow` and `fast` pointers until `fast` reaches the last node of the list.
5. At this point, `slow` is at the node just before the node to be removed.
6. Adjust the pointers to remove the nth node from the end:
   - Set `slow.next` to `slow.next.next`, effectively bypassing the nth node.
7. Return the head of the linked list.

**Complexity**:
- Time: O(L), where L is the length of the linked list.
- Space: O(1), using constant extra space.