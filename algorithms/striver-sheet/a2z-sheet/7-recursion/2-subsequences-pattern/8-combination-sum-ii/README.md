![IMG_7242](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/672dd79e-4820-4882-9491-fdc053959944)

## Approach
1. Sort the list of candidates to ensure that duplicates are adjacent.
2. Implement a recursive function `combination_sum_use_once` to find combinations:
   - Start with an empty array to hold the current combination.
   - Iterate through the candidates starting from the given index.
   - For each candidate:
     - Pick the candidate and subtract its value from the target sum.
     - Recursively call the function with the updated index (index + 1), updated sum (sum - candidate value), and the combination with the candidate appended.
     - If the sum becomes zero, add the current combination to the result list.
     - To avoid duplicate combinations, skip candidates that are duplicates of the current candidate. This is done by incrementing the index until a different candidate is found. This ensures that only the first occurrence of each candidate is used in a particular recursive call, preventing duplicate combinations.
3. Call the recursive function with initial parameters (index = 0, sum = target, current combination = []) and return the result list.
