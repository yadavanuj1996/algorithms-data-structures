![IMG_6820](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/68a6c490-133b-46d0-a334-957d215358fc)

### Algorithm Steps:

1. Initialize pointers `even` and `odd` to the first and second nodes, respectively.
2. Set `odd_head` to the second node to mark the start of odd-indexed nodes.
3. Iterate through the list while both `odd` and `odd.next` are not None.
4. Inside the loop:
   - Update `even.next` to skip the next node (odd-indexed).
   - Update `odd.next` to skip the next node (even-indexed).
   - Move `even` and `odd` pointers to the next even and odd nodes, respectively.
5. Link the last even node's `next` to the head of the odd-indexed nodes (`odd_head`).
6. Return the modified head node of the list.

```
Note: The algorithm assumes even indices start from 0, contrary to conventional indexing. (I have done opposite the problem
statement)
```
