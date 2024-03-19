## Subset Sum Problem Solver

### Algorithm
1. The function calculates the length of the list `a`.
2. It defines a recursive function `find_subset_with_given_sum` to explore all possible subsets.
3. At each step:
   - It includes the current element in the subset (`sum + a[index]`), or
   - Excludes the current element from the subset (`sum`).
4. Base Cases:
   - If the current sum exceeds the target sum `k`, it returns `False`.
   - If the index reaches the end of the list `a`, it checks if the current sum equals `k`. If yes, it returns `True`; otherwise, it returns `False`.
5. Finally, it calls the `find_subset_with_given_sum` function from the main function `isSubsetPresent`.
   
### Complexity
- **Time Complexity**: Exponential (O(2^n)) due to exploring all possible subsets.
- **Space Complexity**: Linear (O(n)) due to recursion depth.

Note: 
# pick
if find_subset_with_given_sum(index+1, sum+a[index]):
    return True
# unpick
if find_subset_with_given_sum(index+1, sum):
    return True

We are using if with the fn cause if we get True in pick case we do not need to run rest of the
fn calls of unpick it will save multiple recursion tree calls.