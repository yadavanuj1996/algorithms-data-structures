![github vid update](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/ed6668f3-3283-4199-b3cb-3f11aa7d2261)

**Algorithm Summary**

- Initialize counters and stacks to keep track of left parentheses indices and star indices.
- Iterate through the input string:
  - If encountering a star, push its index onto the star stack.
  - If encountering a left parenthesis, push its index onto the left parenthesis stack.
  - If encountering a right parenthesis:
    - If there exists a left parenthesis in the left parenthesis stack, pop it to match with the current right parenthesis.
    - If there are no left parentheses, try to match with a star by popping a star index from the star stack.
    - If neither left parentheses nor stars are available, return False as the string cannot be balanced.
- After balancing right parentheses, check if there are any remaining left parentheses.
  - For each remaining left parenthesis, attempt to match with a star by comparing indices.
  - If a match is not found, return False.
- If all parentheses are balanced, return True.

### Time and Space Complexity
The algorithm runs in O(n) time complexity, where n is the length of the input string, and O(n) space complexity due to stack usage.
