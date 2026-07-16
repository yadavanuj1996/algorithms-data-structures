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
| 14  | Reverse Bits | Bit Manipulation | Bit-by-bit Reconstruction | Loop 32 times, shift result left then OR in last bit of n, right shift n each iteration | O(1) | O(1) |
| 15  | Climbing Stairs | Dynamic Programming | Bottom-Up DP (Backwards) | Start with both n and n-1 base cases = 1. Loop from n-2 to 0: ways(i) = ways(i+1) + ways(i+2). Use 2 vars to optimize space | O(n) | O(1) |
| 16  | Coin Change | Dynamic Programming | Pick / Not-Pick with Memoization | solve(i, target): "pick" reuses same coin so stay on index i and subtract coin (1 + solve(i, target-coins[i])), "not pick" moves to i-1. Base: index 0 => target/coins[0] if divisible else inf. Answer inf => -1 | O(n * amount) | O(n * amount) |
| 17  | Longest Increasing Subsequence | Dynamic Programming | Bottom-Up DP with Nested Pointers | Outer pointer j (0→n), inner pointer i (0→j). When nums[i] < nums[j], update dp[j] = max(dp[i]+1, dp[j]) | O(n²) | O(n) |
| 18  | Longest Common Subsequence | Dynamic Programming | Top-Down DP with Memoization | Start from both string ends. If chars match: 1 + solve remaining strings. If chars differ: skip char from either string, take maximum result | O(n*m) | O(n*m) |
| 19  | Word Break | Dynamic Programming | Top-Down DP with Memoization | memo[i] = can s[0..i] be segmented using wordDict. For each index, try matching every word in dict starting at that position. If match found, recurse from index+word_len. Memoize result at each index | O(n * m * k) | O(n) |
| 20  | Combination Sum | Backtracking | Pick / Not-Pick Recursion | Same element can be reused, so on "pick" stay on the same index (don't move ahead), add the number to the current array and add its value to the current sum. On "not pick" move to the next index without adding anything. When the sum equals the target, save the current array into the result | O(k * 2^(n + k)) | O(n + k²) |
| 21  | House Robber | Dynamic Programming | Pick / Not-Pick with Memoization | rob(i): "pick" = nums[i] + rob(i-2) (skip adjacent), "not pick" = rob(i-1). Take max. Memoize by index | O(n) | O(n) |
| 22  | House Robber II | Dynamic Programming | Two Linear Runs (Circular) | Houses are circular so first and last are adjacent. Run House Robber twice: on [0..n-2] (exclude last) and [1..n-1] (exclude first), take the max. Handle single-house edge case | O(n) | O(n) |
| 23  | Decode Ways | Dynamic Programming | Bottom-Up DP | dp[i] = ways to decode s[0..i]. dp[i] += dp[i-1] if s[i] != '0' (single digit); dp[i] += dp[i-2] if 10 <= int(s[i-1:i+1]) <= 26 (two-digit code). Handle dp[0], dp[1] base cases | O(n) | O(n) |
| 24  | Unique Paths | Dynamic Programming | Grid DP with Memoization | paths(i, j) = paths(i+1, j) + paths(i, j+1). Base: reaching bottom-right (m-1, n-1) => 1, out of bounds => 0. Memoize each cell | O(m * n) | O(m * n) |
| 25  | Jump Game | Greedy | Furthest Reachable | Track furthest index reachable so far. If current index i > reachable, return False. Else reachable = max(reachable, i + nums[i]). Survive the loop => True | O(n) | O(1) |
| 26  | Clone Graph | Graph | NOT ATTEMPTED |  |  | |  |
| 27  | Course Schedule | Graph | DFS Cycle Detection | Build adjacency list (course -> prereqs). DFS each node tracking the current path (visited). If a node is revisited while still on the path (not yet completed) => cycle => can't finish. Mark completed after exploring all neighbours | O(V + E) | O(V + E) |
| 28  | Pacific Atlantic Water Flow | Graph | Reverse-Flow DFS from Borders | Instead of testing every cell "can it reach both oceans" (expensive), invert it: water flows downhill, so in reverse it climbs to neighbours with height >= current. Seed one visited-set per ocean from its border cells (Pacific = top row + left col, Atlantic = bottom row + right col) and DFS inward. A cell in BOTH sets can drain to both oceans => add to result. Two passes, each cell visited at most twice | O(m * n) | O(m * n) |
| 55  | Longest Palindromic Substring | String | Expand Around Center | For each index i, expand outward for odd (expand(i,i)) and even (expand(i,i+1)) palindromes. While s[left]==s[right] keep expanding left-1, right+1. After loop, slice s[left+1:right] gives the palindrome | O(n²) | O(1) |

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
| 11  | Number of 1 Bits | https://leetcode.com/problems/number-of-1-bits/ |
| 12  | Counting Bits | https://leetcode.com/problems/counting-bits/ |
| 13  | Missing Number | https://leetcode.com/problems/missing-number/ |
| 14  | Reverse Bits | https://leetcode.com/problems/reverse-bits/ |
| 15  | Climbing Stairs | https://leetcode.com/problems/climbing-stairs/ |
| 16  | Coin Change | https://leetcode.com/problems/coin-change/ |
| 17  | Longest Increasing Subsequence | https://leetcode.com/problems/longest-increasing-subsequence/ |
| 18  | Longest Common Subsequence | https://leetcode.com/problems/longest-common-subsequence/ |
| 19  | Word Break | https://leetcode.com/problems/word-break/ |
| 20  | Combination Sum | https://leetcode.com/problems/combination-sum/ |
| 21  | House Robber | https://leetcode.com/problems/house-robber/ |
| 22  | House Robber II | https://leetcode.com/problems/house-robber-ii/ |
| 23  | Decode Ways | https://leetcode.com/problems/decode-ways/ |
| 24  | Unique Paths | https://leetcode.com/problems/unique-paths/ |
| 25  | Jump Game | https://leetcode.com/problems/jump-game/ |
| 26  | Clone Graph | https://leetcode.com/problems/clone-graph/ |
| 27  | Course Schedule | https://leetcode.com/problems/course-schedule/ |
| 28  | Pacific Atlantic Water Flow | https://leetcode.com/problems/pacific-atlantic-water-flow/ |
| 55  | Longest Palindromic Substring | https://leetcode.com/problems/longest-palindromic-substring/ |




Revise:
1. Coin change - faced issues
2. LCS tabulation (not attempted)
3. Bits problems




