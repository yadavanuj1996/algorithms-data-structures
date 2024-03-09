- **Algorithm Approach**:
Use a modified tortoise and hare algorithm.
- Initialize fast from head.next.next (start from node 3) and start with head node
- Initializes two pointers, `slow` and `fast`, with `slow` moving one step at a time and `fast` moving two steps at a time.
- Traverses the linked list until `fast` reaches the end or the node before the end.
- `slow` will be pointing to the node just before the middle node (or the middle node if the list has an odd number of nodes).
- Removes the middle node by updating the `next` pointer of the node pointed to by `slow`.