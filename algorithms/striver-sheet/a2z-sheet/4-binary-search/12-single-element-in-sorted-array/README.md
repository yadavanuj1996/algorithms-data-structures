## Intuition

The problem specifies that all elements in the array occur twice except one. To approach this, consider the
array's structure: if no single number is encountered yet, each number would appear in pairs at even and odd 
indices, such as (0,1), (2,3), (4,5), and so on. This pattern is disrupted once the single number is reached
in the array.

For instance, if we examine an odd index and find that the preceding index does not contain the same number, it implies that the single number was already encountered before this index. Consequently, we can narrow down our search space to the left half of the array. This approach helps efficiently locate the single non-duplicate element.
## Algorithm Summary

- Check if the length of `nums` is 1 or if the first element of `nums` is not equal to the second element. If true, return the first element.
- Check if the last element of `nums` is not equal to the second last element. If true, return the last element.
- Initialize `low` to 1 and `high` to `n-2`.
- Enter a binary search loop while `low` is less than or equal to `high`.
  - Calculate the `mid` index as the floor division of the sum of `low` and `high` by 2.
  - If the element at `mid` is not equal to the elements adjacent to it (neither `nums[mid] == nums[mid-1]` nor `nums[mid] == nums[mid+1]`), return `nums[mid]`.
  - If `mid` is even and the element at `mid` is equal to the next element, update `low` to `mid+1`.
  - If `mid` is odd and the element at `mid` is equal to the previous element, update `low` to `mid+1`.
  - Otherwise, update `high` to `mid-1`.

