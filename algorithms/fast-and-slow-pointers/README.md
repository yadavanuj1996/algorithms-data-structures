# Fast and Slow Pointers

Similar to the two pointers pattern, the fast and slow pointers pattern uses two pointers to traverse an iterable data structure at different speeds. It’s usually used to identify distinguishable features of directional data structures, such as a linked list or an array.

The pointers can be used to traverse the array or list in either direction, however, one moves faster than the other. Generally, the slow pointer moves forward by a factor of one, and the fast pointer moves by a factor of two in each step. However, the speed can be adjusted according to the problem statement.

Unlike the two pointers approach, which is concerned with data values, the fast and slow pointers approach is used to determine data structure traits using indices in arrays or node pointers in linked lists. The approach is commonly used to detect cycles in the given data structure, so it’s also known as Floyd’s cycle detection algorithm.

The key idea is that the pointers start at the same location, but they move forward at different speeds. If there is a cycle, the two are bound to meet at some point in the traversal. To understand the concept, think of two runners on a track. While they start from the same point, they have different running speeds. If the race track is a circle, the faster runner will overtake the slower one after completing a lap. On the other hand, if the track is straight, the faster runner will end the race before the slower one, hence never meeting on the track again. The fast and slow pointers pattern uses the same intuition.

<img width="587" alt="Screenshot 2023-07-01 at 6 27 39 PM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/e824d0c6-bd33-42b0-a898-c973a5a1e5a4">


## Does my problem match this pattern?

### Yes, if either of these conditions is fulfilled:
- Either as an intermediate step, or as the final solution, the problem requires identifying:
    - the first x % of the elements in a linked list, or,
    - the element at the k-way point in a linked list, for example, the middle element, or the element at the start of the second quartile, etc.
    - the k th last element in a linked list
- Solving the problem requires detecting the presence of a cycle in a linked list.
- Solving the problem requires detecting the presence of a cycle in a sequence of symbols.

### No, if either of these conditions is fulfilled:
- The input data cannot be traversed in a linear fashion, that is, it’s neither in an array, nor in a linked list, nor in a string of characters.
- The problem can be solved with two pointers traversing an array or a linked list at the same pace.

## Real-world problems
- Symlink verification
- Compiling an object-oriented program


