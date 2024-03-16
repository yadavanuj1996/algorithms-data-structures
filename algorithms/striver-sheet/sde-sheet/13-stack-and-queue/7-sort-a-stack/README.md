## Algorithm Summary:

- **Objective:** Sort a given stack of integers in descending order using recursion and limited stack operations.
- Implement a `sortStack` function to interface the sorting process.
- Implement `sort_stack` to recursively sort the stack by popping an element, sorting the remaining stack, and placing the popped element in the correct position using `fit_element`.
- `fit_element` recursively fits an element into the sorted stack by comparing it with the top element of the stack and adjusting accordingly.
- Call `sort_stack` from `sortStack` to initiate the sorting process.

## Complexity:
- **Time Complexity:** O(N^2) - Recursion involves potentially O(N) operations for each element in the stack.
- **Space Complexity:** O(N) - Due to recursion stack and space used by the stack representation.
