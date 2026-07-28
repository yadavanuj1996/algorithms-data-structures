## Intuition

Think of it as the "soldier problem": before the single element, pairs line up at (even, odd) index
offsets, e.g. `A A B B C D D` at indices `0 1 2 3 4 5 6` — every pair starts at an even index. Once the
single element ("broken soldier") is passed, pairs shift to start at odd indices instead.

So for any even `mid`, if `nums[mid] == nums[mid+1]`, the pairing is still intact there, meaning the single
element must be further right — search `[mid+2, right]`. If they differ, the single element is at `mid` or
to its left — search `[left, mid]`. The loop narrows `left`/`right` until they meet, and that index holds
the answer.

## Algorithm Summary

- Initialize `left = 0` and `right = n - 1`.
- While `left < right`:
  - Compute `mid = (left + right) // 2`, and if `mid` is odd, decrement it by 1 so `mid` is always even.
  - If `nums[mid] == nums[mid+1]`, the pair is intact — set `left = mid + 2`.
  - Otherwise, the single element is at or before `mid` — set `right = mid`.
- Return `nums[left]` (equivalently `nums[right]`), the single non-duplicate element.

