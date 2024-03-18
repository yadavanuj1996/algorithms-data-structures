## Algorithm Summary: Reverse Stack

### Approach:
1. Define two helper functions: `reverse_stack` and `fit_element`.
2. `reverse_stack` recursively pops each element from the stack and stores it temporarily.
3. Once the stack is empty, `reverse_stack` calls `fit_element` for each stored element.
4. `fit_element` recursively fits each element back into the stack in reversed order.

### Time Complexity:
- O(n^2), where n is the number of elements in the stack.
  - `reverse_stack` and `fit_element` are both recursive functions called for each element in the stack.
  - Each function iterates over the stack, resulting in O(n) time complexity for each function, leading to O(n^2) overall.

### Space Complexity:
- O(n), where n is the number of elements in the stack.
  - The recursion depth is proportional to the number of elements in the stack.
  - Each recursive call consumes a constant amount of space on the function call stack.

![IMG_7069](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/8caa14a4-ed86-4f40-8aba-42a7fd5f897e)
