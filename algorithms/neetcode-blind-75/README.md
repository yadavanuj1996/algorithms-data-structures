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
| 6   | Maximum Product Subarray | Array | Prefix/Suffix | Track prefix product L→R and suffix product R→L. When hit 0, reset to 1. Max product is max of all prefix/suffix values | O(n) | O(1) |
| 7   | Find Minimum in Rotated Sorted Array | Binary Search | Modified Binary Search | If nums[mid] > nums[right]: rotation point (min) is in right half, else in left half. Keep searching until left == right | O(log n) | O(1) |
| 8   | Search in Rotated Sorted Array | Binary Search | Modified Binary Search | Identify sorted half, check if target in sorted range, search appropriate half | O(log n) | O(1) |
| 9   | 3Sum | Array | Two Pointers | SORT array first! Fix first element, then solve 2Sum on remaining sorted array using two pointers from both ends. Skip duplicates for all three positions | O(n²) | O(1) |
| 10  | Container With Most Water | Array | Two Pointers | Start with pointers at both ends of array. Move pointer with smaller height (wider base won't help with shorter height) | O(n) | O(1) |
| 11  | Number of 1 Bits | Bit Manipulation | Bit Counting | Count set bits by checking n % 2, then right shift with n // 2 or n >> 1 | O(log n) | O(1) |
| 12  | Counting Bits | Bit Manipulation | Bit Counting | For each number 0 to n, count 1-bits using modulo and right shift operations | O(n log n) | O(1) |
| 13  | Missing Number | Array | XOR Trick | XOR all indices (0 to n) with all array values. Missing number will remain as XOR cancels out pairs | O(n) | O(1) |
   
  



  
## Problem Links

| No. | Problem Name | LeetCode Link |
|-----|--------------|---------------|
| 1   | Two Sum | https://leetcode.com/problems/two-sum/ |
| 2   | Best Time to Buy and Sell Stock | https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ |
| 3   | Contains Duplicate | https://leetcode.com/problems/contains-duplicate/ |
| 4   | Product of Array Except Self | https://leetcode.com/problems/product-of-array-except-self/ |
| 5   | Maximum Subarray | https://leetcode.com/problems/maximum-subarray/ |
| 6   | Maximum Product Subarray | https://leetcode.com/problems/maximum-product-subarray/ |
| 7   | Find Minimum in Rotated Sorted Array | https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ |
| 8   | Search in Rotated Sorted Array | https://leetcode.com/problems/search-in-rotated-sorted-array/ |
| 9   | 3Sum | https://leetcode.com/problems/3sum/ |
| 10  | Container With Most Water | https://leetcode.com/problems/container-with-most-water/ |
| 11  | Sum of Two Integers | https://leetcode.com/problems/sum-of-two-integers/ |
| 12  | Number of 1 Bits | https://leetcode.com/problems/number-of-1-bits/ |
| 13  | Counting Bits | https://leetcode.com/problems/counting-bits/ |
| 14  | Missing Number | https://leetcode.com/problems/missing-number/ |
| 15  | Reverse Bits | https://leetcode.com/problems/reverse-bits/ |
| 16  | Climbing Stairs | https://leetcode.com/problems/climbing-stairs/ |
| 17  | Coin Change | https://leetcode.com/problems/coin-change/ |
