![IMG_7202](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/cb9877fd-2f4f-4b04-9140-5c2210528137)
![IMG_7203](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/9ac7f0f5-ea34-447c-9a8d-de5162e7b3ef)
![IMG_7204](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/828f9f1e-867e-4d88-bad8-43ce6a60dfd7)

### Algorithm Summary
To solve this problem efficiently, we use a prefix sum technique combined with a dict.

1. **Initialization**: Initialize `pre_sum` to 0, which represents the prefix sum, and `old_pre_sums` as a hashmap with a default value of 0 for prefix sums. Also, initialize `count` to 0.
   
2. **Iterate Through Array**:
   - Update `pre_sum` by adding the current element.
   - Increment `count` by the number of times `pre_sum - k` has been encountered before. This indicates the number of subarrays ending at the current index with sum equal to `k`.
   - Update `old_pre_sums` with the current prefix sum, incrementing the count if the sum is already encountered, or adding a new entry if it's the first occurrence.

3. **Return Count**: Finally, return `count`, which represents the total number of subarrays with sum equal to `k`.

### Time Complexity
- The algorithm iterates through the `nums` array once, resulting in O(n) time complexity, where n is the length of the input array.
- Each lookup and update operation in the hashmap (`old_pre_sums`) takes O(1) time.
- Hence, the overall time complexity is O(n).

### Space Complexity
- The algorithm uses additional space for the hashmap (`old_pre_sums`), which can store up to n unique prefix sums.
- Therefore, the space complexity is O(n), where n is the length of the input array.
