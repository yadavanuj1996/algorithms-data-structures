
![IMG_6814_2](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/e2671ad0-a8dd-4734-b0ff-693a5a1ca34c)

- Objective:
  - Determine if a given singly-linked list contains a cycle.
- Algorithm:
  - Initialize two pointers, first and second, both starting at the head of the linked list.
  - Traverse the linked list with a while loop, ensuring first and second are not None and second.next and second.next.next exist.
  - Move the first pointer one step forward and the second pointer two steps forward in each iteration.
  - If first and second meet (point to the same node), a cycle exists, and the function returns True.
  - If no cycle is found after traversing the entire list, return False.

- Time Complexity: O(n) - where  n is the number of nodes in the linked list.
- Space Complexity:  O(1) - Constant extra space usage regardless of the linked list's size.

