# Deque

This is pre defined Python implementation of Deque that is provided by collection module.

Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over a list in the cases where 
we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append 
and pop operations as compared to a list that provides O(n) time complexity.


<img width="702" alt="Screenshot 2023-12-31 at 7 37 32 AM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/8cb66565-c874-417b-9ec7-491a05e7680b">

### Note: In collection module deque the front in on right side and rear on left, thus use appendLeft and append accordingly
- Declaration of deque
```
from collections import deque
dq = deque([1, 2, 3])
```

#### Operation on Deque
- append():- This function is used to insert the value in its argument to the right end of the deque.
- appendleft():- This function is used to insert the value in its argument to the left end of the deque.
- pop():- This function is used to delete an argument from the right end of the deque.
- popleft():- This function is used to delete an argument from the left end of the deque.
- len(dequeue):- Return the current size of the dequeue.
- dq[0] :- We can access the front element of the deque using indexing with de[0].
- dq[-1] :- We can access the back element of the deque using indexing with de[-1].

<img width="525" alt="Screenshot 2023-12-31 at 7 42 33 AM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/74ceca65-7aeb-411c-91a6-5e181a8abeec">
