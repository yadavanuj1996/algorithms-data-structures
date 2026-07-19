# Neetcode blind 75 Cheat Sheet

Quick revision notes for coding interview problems, organized by the Blind 75 categories.

Each solved problem lists its pattern, the key trick, and time/space complexity. `NOT ATTEMPTED` marks problems still pending.

## Arrays & Hashing

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Hash Set | Use set to track seen numbers, return True immediately if duplicate found | O(n) | O(n) |
| [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Frequency Map | If lengths differ, return False. Build a char->count map for each string, then compare the two maps for equality. (Or use one map: increment for s, decrement for t, all counts must be 0) | O(m + n) | O(m + n) |
| [Two Sum](https://leetcode.com/problems/two-sum/) | Hash Map | Store target-cur_no in dict, and for each iteration check if current num exists in dict | O(n) | O(n) |
| [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | NOT ATTEMPTED | — | — | — |
| [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Frequency Map + Sort | Build a num->count map, sort items by count descending, take the first k keys. (Optimal O(n) uses bucket sort: index buckets by frequency 1..n, then read buckets from high to low until k collected) | O(n log n) | O(n) |
| [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | NOT ATTEMPTED | — | — | — |
| [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Prefix/Suffix | First pass: store left products (prefix), Second pass: multiply with right products (suffix) in-place | O(n) | O(1) |
| [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Hash Set (Sequence Start) | Put all nums in a set. Only start counting from a sequence START (num-1 not in set), then walk num+1, num+2... while present, tracking the longest run. The start-check ensures each number is visited at most twice => O(n) overall despite the inner while | O(n) | O(n) |

## Two Pointers

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Two Pointers | Keep only alphanumeric chars (lowercased), then two pointers from both ends moving inward: if chars differ return False, else shrink. (Can skip non-alphanumeric in-place to get O(1) space instead of building a filtered string) | O(n) | O(n) |
| [3Sum](https://leetcode.com/problems/3sum/) | Two Pointers | SORT array first! Fix first element, then solve 2Sum on remaining sorted array using two pointers from both ends. Skip duplicates for all three positions | O(n²) | O(1) |
| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Two Pointers | Start with pointers at both ends of array. Move pointer with smaller height (wider base won't help with shorter height) | O(n) | O(1) |

## Sliding Window

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Single Pass | Track min price seen so far, update max profit at each step | O(n) | O(1) |
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Sliding Window | Expand right pointer adding chars to a count map. When the new char's count > 1, shrink from left (decrement counts) until no duplicate. Track max window size (r-l+1) each step | O(n) | O(min(n, charset)) |
| [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Sliding Window + Max Freq | Window is valid when (window_len - count of most frequent char) <= k, meaning the other chars can be replaced within k changes. Expand right and update max_freq; when invalid, shrink left. Answer = longest valid window | O(n) | O(charset) |
| [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Sliding Window + Need Count | Build required-char counts from t and track how many required chars are currently satisfied (have >= need). Expand right; once all requirements met, shrink left while still valid, recording the smallest window. Return the min window covering all of t | O(m + n) | O(charset) |

## Stack

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Matching Stack | Push opening brackets; on a closing bracket check it matches the top opening (pop if so). Valid only if every closer matched and the stack is empty at the end. (Cleanest: map closer->opener) | O(n) | O(n) |

## Binary Search

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Modified Binary Search | If nums[mid] > nums[right]: rotation point (min) is in right half, else in left half. Keep searching until left == right | O(log n) | O(1) |
| [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Modified Binary Search | Identify sorted half, check if target in sorted range, search appropriate half | O(log n) | O(1) |

## Linked List

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Pointer Reversal | Walk the list keeping prev and cur; each step save next, point cur.next back to prev, then advance prev=cur, cur=next. Return prev as the new head. (Recursive form: pass (prev, cur) and flip pointers on the way down) | O(n) | O(1) iterative / O(n) recursive |
| [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | NOT ATTEMPTED | — | — | — |
| [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Fast & Slow Pointers | Move slow by 1 and fast by 2. If there's a cycle they eventually meet; if fast (or fast.next) hits None, the list ends => no cycle | O(n) | O(1) |
| [Reorder List](https://leetcode.com/problems/reorder-list/) | NOT ATTEMPTED | — | — | — |
| [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Two Pointers (Gap of n) | Advance fast n steps first. If fast is None, the head itself is the target (return head.next). Else move slow and fast together until fast.next is None; slow now sits just before the target, so slow.next = slow.next.next | O(n) | O(1) |
| [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | NOT ATTEMPTED | — | — | — |

## Trees

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | NOT ATTEMPTED | — | — | — |
| [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | DFS Recursion | Depth of a node = 1 + max(depth of left subtree, depth of right subtree). Base case: null node => 0. Recurse and bubble up the max | O(n) | O(h) recursion stack |
| [Same Tree](https://leetcode.com/problems/same-tree/) | Parallel DFS | Recurse both trees in lockstep. Both null => True; one null or values differ => False; else recurse left-with-left AND right-with-right | O(n) | O(h) recursion stack |
| [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | NOT ATTEMPTED | — | — | — |
| [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | BST Property Walk | Use the ordering: if both p and q are less than node, go left; if both greater, go right; otherwise they split (or one equals node) => this node is the LCA | O(h) | O(1) iterative / O(h) recursive |
| [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | BFS (Level Tracking) | BFS with a queue, grouping nodes by level. Either process the whole queue size at a time (one level per outer iteration), or tag each node with its level and append to res[level]. Enqueue left then right children | O(n) | O(n) |
| [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Min/Max Bounds DFS | Recurse carrying an open (min, max) range each node must fall strictly inside. Going left tightens the max to node.val; going right tightens the min to node.val. Any node outside its range => invalid. (Alt: inorder traversal must be strictly increasing) | O(n) | O(h) |
| [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Inorder Traversal | Inorder (left, node, right) of a BST visits values in sorted order, so the kth visited node is the answer. Collect into a list and return res[k-1], or stop early once k nodes are counted | O(n) | O(n) |
| [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Recursive Split | preorder[0] is always the root. Find it in inorder: everything left of it is the left subtree, everything right is the right subtree. Split both arrays by that count and recurse. (Optimal: pass index ranges + a value->inorder-index hash map to avoid slicing/search, giving O(n)) | O(n²) | O(n²) |
| [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | DFS (Return vs Update) | Each DFS returns the best straight-line path going DOWN one side (node + max(left, right), clamping negatives to 0). Separately, update a global max with the best path THROUGH the node (node + left + right) since a path can bend at a node but can't be returned upward | O(n) | O(h) |
| [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | NOT ATTEMPTED | — | — | — |

## Heap / Priority Queue

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | NOT ATTEMPTED | — | — | — |

## Backtracking

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Combination Sum](https://leetcode.com/problems/combination-sum/) | Pick / Not-Pick Recursion | Same element can be reused, so on "pick" stay on the same index (don't move ahead), add the number to the current array and add its value to the current sum. On "not pick" move to the next index without adding anything. When the sum equals the target, save the current array into the result | O(k * 2^(n + k)) | O(n + k²) |
| [Word Search](https://leetcode.com/problems/word-search/) | Grid DFS + Backtrack | From each cell matching word[0], DFS in 4 directions matching one char per step. Mark the cell visited before recursing and unmark after (backtrack) so the same letter isn't reused within one path but stays free for other paths. Return True the moment cur_index reaches word length | O(m * n * 4^L) | O(L) recursion (+ O(m*n) visited) |

## Tries

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Nodes with 26 Children | Each node holds 26 child links + an is_end flag. insert: walk chars creating missing child nodes, mark last node as end. search: walk chars, fail if any link missing, at the end require is_end True. startsWith: same walk but no is_end check | insert/search O(L) | O(total chars) |
| [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | NOT ATTEMPTED | — | — | — |
| [Word Search II](https://leetcode.com/problems/word-search-ii/) | NOT ATTEMPTED | — | — | — |

## Graphs

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Grid DFS (Flood Fill) | Scan every cell; when you hit an unvisited '1', increment the island count and DFS/flood-fill all connected land (4 directions), marking cells visited so each island is counted once. Each cell visited at most once | O(m * n) | O(m * n) |
| [Clone Graph](https://leetcode.com/problems/clone-graph/) | NOT ATTEMPTED | — | — | — |
| [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Reverse-Flow DFS from Borders | Instead of testing every cell "can it reach both oceans" (expensive), invert it: water flows downhill, so in reverse it climbs to neighbours with height >= current. Seed one visited-set per ocean from its border cells (Pacific = top row + left col, Atlantic = bottom row + right col) and DFS inward. A cell in BOTH sets can drain to both oceans => add to result. Two passes, each cell visited at most twice | O(m * n) | O(m * n) |
| [Course Schedule](https://leetcode.com/problems/course-schedule/) | DFS Cycle Detection | Build adjacency list (course -> prereqs). DFS each node tracking the current path (visited). If a node is revisited while still on the path (not yet completed) => cycle => can't finish. Mark completed after exploring all neighbours | O(V + E) | O(V + E) |
| [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | NOT ATTEMPTED | — | — | — |
| [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | NOT ATTEMPTED | — | — | — |

## Advanced Graphs

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | NOT ATTEMPTED | — | — | — |

## 1-D Dynamic Programming

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Bottom-Up DP (Backwards) | Start with both n and n-1 base cases = 1. Loop from n-2 to 0: ways(i) = ways(i+1) + ways(i+2). Use 2 vars to optimize space | O(n) | O(1) |
| [House Robber](https://leetcode.com/problems/house-robber/) | Pick / Not-Pick with Memoization | rob(i): "pick" = nums[i] + rob(i-2) (skip adjacent), "not pick" = rob(i-1). Take max. Memoize by index | O(n) | O(n) |
| [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Two Linear Runs (Circular) | Houses are circular so first and last are adjacent. Run House Robber twice: on [0..n-2] (exclude last) and [1..n-1] (exclude first), take the max. Handle single-house edge case | O(n) | O(n) |
| [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Expand Around Center | For each index i, expand outward for odd (expand(i,i)) and even (expand(i,i+1)) palindromes. While s[left]==s[right] keep expanding left-1, right+1. After loop, slice s[left+1:right] gives the palindrome | O(n²) | O(1) |
| [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | NOT ATTEMPTED | — | — | — |
| [Decode Ways](https://leetcode.com/problems/decode-ways/) | Bottom-Up DP | dp[i] = ways to decode s[0..i]. dp[i] += dp[i-1] if s[i] != '0' (single digit); dp[i] += dp[i-2] if 10 <= int(s[i-1:i+1]) <= 26 (two-digit code). Handle dp[0], dp[1] base cases | O(n) | O(n) |
| [Coin Change](https://leetcode.com/problems/coin-change/) | Pick / Not-Pick with Memoization | solve(i, target): "pick" reuses same coin so stay on index i and subtract coin (1 + solve(i, target-coins[i])), "not pick" moves to i-1. Base: index 0 => target/coins[0] if divisible else inf. Answer inf => -1 | O(n * amount) | O(n * amount) |
| [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Prefix/Suffix | Track prefix product L→R and suffix product R→L. When hit 0, reset to 1. Max product is max of all prefix/suffix values | O(n) | O(1) |
| [Word Break](https://leetcode.com/problems/word-break/) | Top-Down DP with Memoization | memo[i] = can s[0..i] be segmented using wordDict. For each index, try matching every word in dict starting at that position. If match found, recurse from index+word_len. Memoize result at each index | O(n * m * k) | O(n) |
| [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Bottom-Up DP with Nested Pointers | Outer pointer j (0→n), inner pointer i (0→j). When nums[i] < nums[j], update dp[j] = max(dp[i]+1, dp[j]) | O(n²) | O(n) |

## 2-D Dynamic Programming

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Unique Paths](https://leetcode.com/problems/unique-paths/) | Grid DP with Memoization | paths(i, j) = paths(i+1, j) + paths(i, j+1). Base: reaching bottom-right (m-1, n-1) => 1, out of bounds => 0. Memoize each cell | O(m * n) | O(m * n) |
| [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Top-Down DP with Memoization | Start from both string ends. If chars match: 1 + solve remaining strings. If chars differ: skip char from either string, take maximum result | O(n*m) | O(n*m) |

## Greedy

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Kadane's Algorithm | At each position decide: start new subarray OR extend current (nums[i] vs cur_sum + nums[i]) | O(n) | O(1) |
| [Jump Game](https://leetcode.com/problems/jump-game/) | Furthest Reachable | Track furthest index reachable so far. If current index i > reachable, return False. Else reachable = max(reachable, i + nums[i]). Survive the loop => True | O(n) | O(1) |

## Bit Manipulation

| Problem | Pattern | Key Trick | Time | Space |
|---------|---------|-----------|------|-------|
| [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Bit Counting | Count set bits by checking n % 2, then right shift with n // 2 or n >> 1 | O(log n) | O(1) |
| [Counting Bits](https://leetcode.com/problems/counting-bits/) | Bit Counting | For each number 0 to n, count 1-bits using modulo and right shift operations | O(n log n) | O(1) |
| [Missing Number](https://leetcode.com/problems/missing-number/) | XOR Trick | XOR all indices (0 to n) with all array values. Missing number will remain as XOR cancels out pairs | O(n) | O(1) |
| [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Bit-by-bit Reconstruction | Loop 32 times, shift result left then OR in last bit of n, right shift n each iteration | O(1) | O(1) |

---

Revise:
1. Coin change - faced issues
2. LCS tabulation (not attempted)
3. Bits problems
