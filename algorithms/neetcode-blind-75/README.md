# Neetcode blind 75 Cheat Sheet

Quick revision notes for coding interview problems.

## Problem Index

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space |
|-----|--------------|----------|---------|-----------|------|-------|
| 1   | Two Sum | Array | Hash Map | Store target-cur_no in dict, and for each iteration check if current num exists in dict | O(n) | O(n) |
| 2   | Best Time to Buy and Sell Stock | Array | Single Pass | Track min price seen so far, update max profit at each step | O(n) | O(1) |
| 3   | Contains Duplicate | Array | Hash Set | Use set to track seen numbers, return True immediately if duplicate found | O(n) | O(n) |
| 4   | Product of Array Except Self | Array | Prefix/Suffix | First pass: store left products (prefix), Second pass: multiply with right products (suffix) in-place | O(n) | O(1) |
| 5   | Maximum Subarray | Array | Kadane's Algorithm | At each position decide: start new subarray OR extend current (nums[i] vs cur_sum + nums[i]) | O(n) | O(1) |
| 6   | Maximum Product Subarray | Array | Prefix/Suffix | Run prefix and suffix products separately, reset to 1 on zero, track max at each step | O(n) | O(1) |
| 7   | Find Minimum in Rotated Sorted Array | Binary Search | Modified Binary Search | Identify sorted half, extract minimum from sorted side, search unsorted half | O(log n) | O(1) |
| 8   | Search in Rotated Sorted Array | Binary Search | Modified Binary Search | Identify sorted half, check if target in sorted range, search appropriate half | O(log n) | O(1) |
| 9   | 3Sum | Array | Two Pointers | Sort array, fix first element, use two pointers for remaining two. Skip duplicates at all three positions | O(n²) | O(1) |
| 10  | Container With Most Water | Array | Two Pointers | Move pointer with smaller height. Skip all heights ≤ current height for optimization | O(n) | O(1) |
| 11  | Number of 1 Bits | Bit Manipulation | Bit Counting | Count set bits by checking n % 2, then right shift with n // 2 or n >> 1 | O(log n) | O(1) |
| 12  | Counting Bits | Bit Manipulation | Bit Counting | For each number 0 to n, count 1-bits using modulo and right shift operations | O(n log n) | O(1) |
| 13  | Missing Number | Array | Math Formula | Use arithmetic series sum formula: expected_sum - actual_sum. Handle edge cases (missing 0 or n) | O(n) | O(1) |
