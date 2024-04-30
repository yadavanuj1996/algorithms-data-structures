![IMG_8793](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/1a1f7008-b9a6-4130-9532-d3a4d6b96e40)

This algorithm implements a string matching technique using the Z-algorithm to find the first occurrence of a "needle" string within a "haystack" string.

### Key Points:
1. **Combining Strings**: The algorithm concatenates the `needle` and `haystack` strings with a special character (`$`) in between. This combined string (`comb_str`) is used for Z-algorithm computation.

2. **Z-algorithm**: This algorithm preprocesses the combined string (`comb_str`) to compute an array `z`, where `z[i]` represents the length of the longest substring starting from `comb_str[i]` that matches a prefix of `comb_str`. 

3. **Initialization**:
   - `l` and `r` are initialized to track the rightmost boundary of a substring window within `comb_str` that matches a prefix.
   - `z[i]` is initialized to `0`.

4. **Z-algorithm Execution**:
   - If `i > r`, it means `i` is outside the current window `[l, r]`. In this case, a new window centered at `i` is established. The algorithm then extends this window by comparing characters until a mismatch is found or the end of the string is reached.
   - If `i ≤ r`, the value of `z[i]` can be determined based on a corresponding start index (`correspond_start_index`) within the current window.

5. **Checking for Needle Match**:
   - After constructing the `z` array, the algorithm iterates through `z` to find any value that matches the length of the `needle`.
   - If a match is found (`z[i] == len(needle)`), it calculates the starting index of the `needle` in the original `haystack` string by subtracting the lengths of `needle` and the special character (`$`).

6. **Result**:
   - If a match is found, it returns the starting index of the first occurrence of `needle` in `haystack`.
   - If no match is found, it returns `-1`.

### Complexity:
- The Z-algorithm preprocessing (`O(n)`) dominates the time complexity, where `n` is the combined length of `needle` and `haystack`.
  
### Improvements:
- The Z-algorithm could be optimized further for space complexity by using two-pointers (`l`, `r`) to avoid storing the entire `comb_str` explicitly. This could reduce the space complexity from `O(n)` to `O(1)`.
