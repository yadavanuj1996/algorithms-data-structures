Certainly! Here are the algorithm points:

- **Algorithm Steps**:

1. **Initialize Pointers**: 
   - Create three pointers `zero`, `one`, and `two` to keep track of the last node of lists containing 0s, 1s, and 2s respectively.
   - Initialize three dummy nodes `zero_head`, `one_head`, and `two_head` as heads of these lists.

2. **Partitioning**:
   - Traverse the input linked list.
   - For each node encountered:
     - If the node's data is 0, append it to the end of the list containing 0s.
     - If the node's data is 1, append it to the end of the list containing 1s.
     - If the node's data is 2, append it to the end of the list containing 2s.

3. **Connecting Lists**:
   - Connect the lists of 0s, 1s, and 2s in the correct order by updating the `next` pointers:
     - Set `zero.next` to the head of the list containing 1s.
     - Set `one.next` to the head of the list containing 2s.

4. **Clean-up**:
   - Set `one_head` and `two_head` to `None` to release unused memory.

5. **Output**:
   - Return the head of the sorted linked list containing 0s, 1s, and 2s.

These algorithm points outline the steps involved in sorting a linked list containing 0s, 1s, and 2s in ascending order using the provided algorithm.
