## Approach 1 (Using stack):
Time complexity: O(N) 
Space Complexity: O(N)

![Screenshot 2024-03-08 at 2 36 09 AM](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/c7aa7d11-f373-4f93-9e59-0b3604653274)

### Algorithm Steps:
- Initialize an empty stack using a deque.
- Traverse the linked list and push each node's value onto the stack.
- Traverse the linked list again, comparing each node's value with the one popped from the stack.
- If at any point the values don't match, return False; otherwise, return True if the entire linked list forms a palindrome.

  Note: Reversed Order: By pushing the values of the linked list onto a stack, we essentially reverse the order of the elements.

  
## Approach 2:
Time complexity: O(N) 
Space Complexity: O(1)

Sure, here's a summary of the algorithm in bullet points:

- **Algorithm: Palindrome Linked List Check**

1. **Reverse Function**:
   - Define a helper function `reverse_list(prev_node, cur_node)` to reverse a linked list from a certain node.
   - Recursively reverse the linked list by swapping pointers between nodes.
   - Return the new head of the reversed linked list.

2. **Finding the Middle**:
   - Initialize two pointers, `slow` and `fast`, both starting from the head.
   - Employ the tortoise and hare algorithm to find the middle node of the linked list.
   - Move `slow` one step at a time and `fast` two steps at a time until `fast` reaches the end of the list.

3. **Comparing Halves**:
   - Reverse the second half of the linked list using the `reverse_list` function, starting from the middle node (`slow`).
   - Traverse the first half (`head`) and the reversed second half (`tail`).
   - Compare corresponding node values of both halves.
   - If any values don't match, set the result as `False` and break the loop.

4. **Reverting Changes**:
   - After comparison, revert the changes made to the linked list by reversing the second half back to its original state.

5. **Return Result**:
   - Return the final result, indicating whether the linked list is a palindrome.

This algorithm efficiently determines whether a given singly-linked list is a palindrome by using the tortoise and hare algorithm and comparing the first half with the reversed second half.
