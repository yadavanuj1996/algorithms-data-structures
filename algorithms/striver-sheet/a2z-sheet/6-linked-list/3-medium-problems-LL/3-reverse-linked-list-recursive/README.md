### Algorithm Steps (Recursive solution)
- Define a helper function reverse_list to reverse the linked list recursively.
- Inside the helper function:
  - If the second node is None, return the first node.
  - Save the next node as temp.
  - Reverse the pointer of the second node to the first node.
  - Recur with the second node as the new first node and temp as the new second node.
- Update the head node using the reverse_list helper function.
- Return the new head node.

![IMG_6819](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/a566fb18-4256-4c02-9501-b815f6e693f9)
