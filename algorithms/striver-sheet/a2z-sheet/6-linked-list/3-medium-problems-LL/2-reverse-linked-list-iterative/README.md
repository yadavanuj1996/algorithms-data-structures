### Algorithm Steps
- Input: head, the head node of a singly-linked list.
- Initialize first to None and second to head.
- Iterate while second is not None:
  - Save second.next as temp.
  - Update second.next to first.
  - Update first to second.
  - Update second to temp.
- Update head to first.
- Return head as the head of the reversed linked list.

![IMG_6819](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/a566fb18-4256-4c02-9501-b815f6e693f9)
