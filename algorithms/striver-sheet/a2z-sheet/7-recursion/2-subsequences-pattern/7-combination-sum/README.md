![IMG_7206](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/a7300cf1-3665-4c5c-a235-9747d473cef1)

![IMG_7207](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/0b3d3f32-3159-41fb-b52d-b48b792cdb01)

## Algorithm Summary
- Initialize an empty list to store valid combinations.
- Define a recursive function `combination_sum(index, sum, arr)` to explore combinations.
  - At each step, the function evaluates whether the current combination satisfies the target sum or if it has exhausted the available candidates.
  - If the target sum is achieved, the current combination is appended to the result list.
  - If the sum becomes negative or the index exceeds the length of the candidates list, the function backtracks.
  - Recursively explore two possibilities:
    - Include the current candidate in the combination and adjust the sum accordingly.
    - Move to the next candidate without including the current one.
- Start the recursive function with initial parameters: index = 0, sum = target, and an empty combination array.
- Return the list of valid combinations found during the exploration.
