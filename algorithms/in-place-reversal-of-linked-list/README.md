# In-place Reversal of a Linked List
The in-place reversal of a linked list pattern allows us to reverse a linked list without any additional memory, using only the given nodes.

## Does my problem match this pattern?
- Yes, if both of these conditions are fulfilled:
    - The problem requires reversing a given linked list, either as the end goal, or as an intermediate step of the solution.
    - The modifications to the linked list must be made in place, that is, we’re not allowed to use more than O(1) additional space in memory.
    
Additionally, this pattern also applies when the problem requires reversing selected portions of a given linked list.

- No, if any of these conditions is fulfilled:
    - The input data is not in the form of a linked list.
    - We specifically need to use additional memory.
    - We aren’t allowed to modify the input linked list.

