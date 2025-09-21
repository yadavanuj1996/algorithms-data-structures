# Striver sheet

### Link
https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/



# Striver Sheets Quick Revision Guide

Quick revision notes for coding interview problems from both A2Z DSA Course and SDE Sheet.

## Table of Contents
- [A2Z DSA Course Problems](#a2z-dsa-course-problems)
- [SDE Sheet Problems](#sde-sheet-problems)

---

## A2Z DSA Course Problems

### Arrays

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Find Second Largest Element | Array | Single Pass | Use two variables to track largest and second largest in one pass | O(n) | O(1) | [Solution](./a2z-sheet/3-arrays/1-easy/2-find-second-largest-element.py) |
| 2   | Check if Array is Sorted | Array | Linear Scan | Compare each element with next element in single pass | O(n) | O(1) | [Solution](./a2z-sheet/3-arrays/1-easy/3-check-if-array-is-sorted.py) |
| 3   | Remove Duplicates from Sorted Array | Array | Two Pointers | Use slow pointer for unique position, fast pointer for scanning | O(n) | O(1) | [Solution](./a2z-sheet/3-arrays/1-easy/4-remove-duplicates-from-sorted-array.py) |
| 4   | Left Rotate Array by One | Array | Temporary Variable | Store first element, shift all left, place first at end | O(n) | O(1) | [Solution](./a2z-sheet/3-arrays/1-easy/5-left-rotate-an-array.py) |
| 5   | Left Rotate Array by D Places | Array | Array Slicing | Use slice concatenation: arr = arr[d:] + arr[:d] | O(n) | O(n) | [Solution](./a2z-sheet/3-arrays/1-easy/6-left-rotate-array-by-d-places.py) |
| 6   | Move Zeros to End | Array | Two Pointers | First pointer tracks first zero, second finds next non-zero to swap | O(n) | O(1) | [Solution](./a2z-sheet/3-arrays/1-easy/7-move-zeros-to-end.py) |
| 7   | Longest Subarray with Sum K | Array | Sliding Window | Two pointers: expand right when sum < k, shrink left when sum > k | O(n) | O(1) | [Solution](./a2z-sheet/3-arrays/1-easy/13-longest-subarray-with-given-sum-k.py) |
| 8   | Two Sum | Array | Hash Map | Store target-current in dict, check if current exists in map | O(n) | O(n) | [Solution](./a2z-sheet/3-arrays/2-medium/1-two-sum.py) |
| 9   | Count Subarrays with Given Sum | Array | Prefix Sum + Hash Map | If prefixSum - k exists in map, we found a valid subarray | O(n) | O(n) | [Solution](./a2z-sheet/3-arrays/2-medium/14-count-subarrays-with-given-sum/14-count-subarrays-with-given-sum.py) |
| 10  | Pascal's Triangle | Array | Mathematical Formula | Use nCr formula optimized: ans = ans * (row-col+1) / col | O(n²) | O(n²) | [Solution](./a2z-sheet/3-arrays/3-hard/1-pascal-traingle/1-pascal-traingle.py) |

### Binary Search

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Binary Search | Binary Search | Divide & Conquer | Compare with mid, eliminate half search space each iteration | O(log n) | O(1) | [Solution](./a2z-sheet/4-binary-search/1-binary-search-in-sorter-arr.py) |
| 2   | Lower Bound | Binary Search | Modified Binary Search | Find smallest index where arr[i] >= x, update result when found | O(log n) | O(1) | [Solution](./a2z-sheet/4-binary-search/2-implement-lower-bound.py) |
| 3   | Upper Bound | Binary Search | Modified Binary Search | Find smallest index where arr[i] > x, similar to lower bound | O(log n) | O(1) | [Solution](./a2z-sheet/4-binary-search/3-implement-higher-bound.py) |
| 4   | Search Insert Position | Binary Search | Lower Bound Variant | Use lower bound logic to find insertion position for target | O(log n) | O(1) | [Solution](./a2z-sheet/4-binary-search/4-search-insert-position.py) |
| 5   | Find First/Last Occurrence | Binary Search | Boundary Search | Use modified binary search to find leftmost and rightmost positions | O(log n) | O(1) | [Solution](./a2z-sheet/4-binary-search/6-find-first-or-last-occurence.py) |
| 6   | Single Element in Sorted Array | Binary Search | Index Parity Check | In pairs, even index should equal next; if not, single element is left | O(log n) | O(1) | [Solution](./a2z-sheet/4-binary-search/12-single-element-in-sorted-array/12-single-element-in-sorted-array.py) |
| 7   | Find Peak Element | Binary Search | Slope Analysis | Always move towards the side with larger neighbor | O(log n) | O(1) | [Solution](./a2z-sheet/4-binary-search/13-find-peak-element/13-find-peak-element.py) |

### Strings

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Remove Outermost Parentheses | String | Counter Tracking | Skip first '(' and last ')' of each primitive group using counter | O(n) | O(n) | [Solution](./a2z-sheet/5-strings/basic/1-remove-outermost-parenthesis/1-remove-outermost-parenthesis.py) |
| 2   | Reverse Words in String | String | Two Pointers | Parse words from right to left, build result by reversing word order | O(n) | O(n) | [Solution](./a2z-sheet/5-strings/basic/2-reverse-words-in-string/2-reverse-words-in-string.py) |
| 3   | Largest Odd Number in String | String | Greedy | Find rightmost odd digit, return substring from start to that position | O(n) | O(1) | [Solution](./a2z-sheet/5-strings/basic/3-largest-odd-num-in-string/3-largest-odd-num-in-string.py) |
| 4   | Longest Common Prefix | String | Vertical Scanning | Compare characters column-wise across all strings until mismatch | O(m*n) | O(1) | [Solution](./a2z-sheet/5-strings/basic/4-longes-common-prefix.py) |
| 5   | Rotate String | String | String Concatenation | Check if goal exists in s+s (contains all possible rotations) | O(n) | O(n) | [Solution](./a2z-sheet/5-strings/basic/6-rotate-string/6-rotate-string.py) |
| 6   | Valid Anagram | String | Frequency Count | Compare character frequency maps of both strings | O(n) | O(n) | [Solution](./a2z-sheet/5-strings/basic/7-check-two-strings-are-anagram/7-check-two-strings-are-anagram.py) |
| 7   | Reverse Every Word | String | Split & Reverse | Split by spaces, reverse each word individually, join back | O(n) | O(n) | [Solution](./a2z-sheet/5-strings/medium/8-reverse-every-word-in-string.py) |

### Linked Lists

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Reverse Linked List (Iterative) | Linked List | Three Pointers | Track prev, current, next. Reverse links one by one | O(n) | O(1) | [Solution](./a2z-sheet/6-linked-list/3-medium-problems-LL/2-reverse-linked-list-iterative/2-reverse-linked-list-iterative.py) |
| 2   | Reverse Linked List (Recursive) | Linked List | Recursion | Recursively reverse from tail, connect current node to reversed list | O(n) | O(n) | [Solution](./a2z-sheet/6-linked-list/3-medium-problems-LL/3-reverse-linked-list-recursive/3-reverse-linked-list-recursive.py) |
| 3   | Detect Loop in Linked List | Linked List | Floyd's Cycle Detection | Use slow and fast pointers, if they meet there's a cycle | O(n) | O(1) | [Solution](./a2z-sheet/6-linked-list/3-medium-problems-LL/4-detect-loop-in-linked-list/4-detect-loop-in-linked-list.py) |
| 4   | Find Starting Point of Loop | Linked List | Floyd's Algorithm | After detecting cycle, reset one pointer to head, move both one step | O(n) | O(1) | [Solution](./a2z-sheet/6-linked-list/3-medium-problems-LL/5-find-starting-point-in-linked-list/5-find-starting-point-in-linked-list.py) |
| 5   | Length of Loop | Linked List | Floyd's + Counting | After finding cycle start, count nodes until back to same node | O(n) | O(1) | [Solution](./a2z-sheet/6-linked-list/3-medium-problems-LL/6-length-of-loop-linked-list/6-length-of-loop-linked-list.py) |
| 6   | Check if Linked List is Palindrome | Linked List | Two Pointers + Reverse | Find middle, reverse second half, compare with first half | O(n) | O(1) | [Solution](./a2z-sheet/6-linked-list/3-medium-problems-LL/7-check-if-linked-list-is-palindrome/7-check-if-linked-list-is-palindrome.py) |
| 7   | Segregate Odd Even Nodes | Linked List | Two Separate Lists | Maintain separate odd and even lists, connect at end | O(n) | O(1) | [Solution](./a2z-sheet/6-linked-list/3-medium-problems-LL/8-segregate-odd-even-nodes-linked-list/8-segregate-odd-even-nodes-linked-list.py) |
| 8   | Remove Nth Node from End | Linked List | Two Pointers with Gap | Move fast pointer n steps ahead, then both together until end | O(n) | O(1) | [Solution](./a2z-sheet/6-linked-list/3-medium-problems-LL/9-remove-nth-node-from-end/9-remove-nth-node-from-end.py) |
| 9   | Delete Middle Node | Linked List | Slow/Fast Pointers | Use tortoise-hare to find middle, delete that node | O(n) | O(1) | [Solution](./a2z-sheet/6-linked-list/3-medium-problems-LL/10-delete-middle-node-linked-list/10-delete-middle-node-linked-list.py) |
| 10  | Sort List with 0s, 1s, 2s | Linked List | Count & Reconstruct | Count 0s, 1s, 2s, then rebuild list in sorted order | O(n) | O(1) | [Solution](./a2z-sheet/6-linked-list/3-medium-problems-LL/12-sort-0-1-2-linked-list/12-sort-0-1-2-linked-list.py) |
| 11  | Intersection Point of Two Lists | Linked List | Length Difference | Calculate length difference, align pointers, find intersection | O(n+m) | O(1) | [Solution](./a2z-sheet/6-linked-list/3-medium-problems-LL/13-intersection-point-y-linked-list/13-intersection-point-y-linked-list.py) |
| 12  | Add One to Number as Linked List | Linked List | Reverse + Add + Reverse | Reverse list, add one with carry, reverse back | O(n) | O(1) | [Solution](./a2z-sheet/6-linked-list/3-medium-problems-LL/14-add-one-to-number-linked-list/14-add-one-to-number-linked-list.py) |
| 13  | Add Two Numbers as Linked Lists | Linked List | Simulation with Carry | Add corresponding digits with carry, create new result list | O(max(n,m)) | O(max(n,m)) | [Solution](./a2z-sheet/6-linked-list/3-medium-problems-LL/15-add-2-numbers-linked-list/15-add-2-numbers-linked-list.py) |
| 14  | Delete All Occurrences in DLL | Doubly Linked List | Linear Traversal | Traverse and update both prev and next pointers when deleting | O(n) | O(1) | [Solution](./a2z-sheet/6-linked-list/4-medium-problems-DLL/1-delete-all-occurences-key-dll/1-delete-all-occurences-key-dll.py) |
| 15  | Find Pairs with Given Sum in DLL | Doubly Linked List | Two Pointers | Use head and tail pointers, move based on sum comparison | O(n) | O(1) | [Solution](./a2z-sheet/6-linked-list/4-medium-problems-DLL/2-find-pairs-with-given-sum/2-find-pairs-with-given-sum.py) |

### Recursion

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Pow(x, n) | Recursion | Fast Exponentiation | If n is even: x^n = (x^(n/2))^2, if odd: x^n = x * x^(n-1) | O(log n) | O(log n) | [Solution](./a2z-sheet/7-recursion/1-get-a-strong-hold/2-pow-x-n.py) |
| 2   | Count Good Numbers | Recursion | Modular Arithmetic | Use fast exponentiation with modulo, count even/odd positions separately | O(log n) | O(log n) | [Solution](./a2z-sheet/7-recursion/1-get-a-strong-hold/3-count-good-numbers.py) |
| 3   | Sort Stack using Recursion | Recursion | Stack Operations | Remove top, sort remaining stack, insert top in sorted position | O(n²) | O(n) | [Solution](./a2z-sheet/7-recursion/1-get-a-strong-hold/4-sort-stack-using-recursion.py) |
| 4   | Reverse Stack using Recursion | Recursion | Stack Operations | Remove top, reverse remaining, insert at bottom of reversed stack | O(n²) | O(n) | [Solution](./a2z-sheet/7-recursion/1-get-a-strong-hold/5-reverse-stack-using-recursion/5-reverse-stack-using-recursion.py) |
| 5   | Generate All Binary Strings | Recursion | Include/Exclude | At each position: try both '0' and '1', backtrack after each choice | O(2^n) | O(n) | [Solution](./a2z-sheet/7-recursion/2-subsequences-pattern/1-generate-all-binary-strings.py) |
| 6   | Generate All Subsequences | Recursion | Include/Exclude | At each element: generate subsequences with and without current element | O(2^n) | O(n) | [Solution](./a2z-sheet/7-recursion/2-subsequences-pattern/3-print-all-subsequences-power-set.py) |
| 7   | Count Subsequences with Sum K | Recursion | Include/Exclude + Count | Count valid combinations, return count instead of storing all | O(2^n) | O(n) | [Solution](./a2z-sheet/7-recursion/2-subsequences-pattern/5-count-all-subsequence-with-sum-k/5-count-all-subsequence-with-sum-k.py) |
| 8   | Check Subsequence with Sum K | Recursion | Include/Exclude + Early Stop | Return true on first valid subsequence found, early termination | O(2^n) | O(n) | [Solution](./a2z-sheet/7-recursion/2-subsequences-pattern/6-subsequence-with-a-sum/6-subsequence-with-a-sum.py) |
| 9   | Combination Sum | Recursion | Unlimited Use | At each element: include unlimited times OR skip to next element | O(2^t) | O(target) | [Solution](./a2z-sheet/7-recursion/2-subsequences-pattern/7-combination-sum/7-combination-sum.py) |
| 10  | Combination Sum II | Recursion | Skip Duplicates | Sort array, skip consecutive duplicates at same recursion level | O(2^n) | O(n) | [Solution](./a2z-sheet/7-recursion/2-subsequences-pattern/8-combination-sum-ii/8-combination-sum-ii.py) |
| 11  | Subset Sum | Recursion | Include/Exclude | Generate all possible subset sums using pick/not-pick pattern | O(2^n) | O(2^n) | [Solution](./a2z-sheet/7-recursion/2-subsequences-pattern/9-subset-sum/9-subset-sum.py) |
| 12  | Subsets II | Recursion | Skip Duplicates | Sort array, skip duplicates at same level to avoid duplicate subsets | O(2^n) | O(2^n) | [Solution](./a2z-sheet/7-recursion/2-subsequences-pattern/10-subset-sum ii/10-subset-sum ii.py) |
| 13  | Subsets III | Recursion | Include/Exclude | Generate all unique subsets using standard backtracking template | O(2^n) | O(2^n) | [Solution](./a2z-sheet/7-recursion/2-subsequences-pattern/11-subset-sum iii/11-subset-sum iii.py) |
| 14  | Letter Combinations | Recursion | Mapping + Backtracking | Map digits to letters, build combinations by trying all letter options | O(4^n) | O(n) | [Solution](./a2z-sheet/7-recursion/2-subsequences-pattern/12-letter-combination-phone-no/12-letter-combination-phone-no.py) |
| 15  | Palindrome Partitioning | Recursion | Backtracking | At each position, try all possible palindromic partitions and recurse | O(2^n * n) | O(n) | [Solution](./a2z-sheet/7-recursion/3-hard-all-combos/1-palindrome-partitioning/1.palindrome-partitioning.py) |
| 16  | Word Search | Recursion | DFS + Backtracking | For each cell, try all 4 directions, mark visited, backtrack after exploring | O(m*n*4^L) | O(L) | [Solution](./a2z-sheet/7-recursion/3-hard-all-combos/2-word-search/2-word-search.py) |
| 17  | Rat in a Maze | Recursion | DFS + Backtracking | Explore all 4 directions (U,D,L,R), mark visited, backtrack after each path | O(4^(m*n)) | O(m*n) | [Solution](./a2z-sheet/7-recursion/3-hard-all-combos/4-rat-in-a-maze/4-rat-in-a-maze.py) |

### Greedy Algorithms

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Assign Cookies | Greedy | Two Pointers | Sort both arrays, assign smallest available cookie to smallest appetite | O(n log n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/easy/1-assign-cookies.py) |
| 2   | Fractional Knapsack | Greedy | Value/Weight Ratio | Sort by value/weight ratio, pick highest ratio items first | O(n log n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/easy/2-fractional-knapsack.py) |
| 3   | Find Min Number of Coins | Greedy | Denomination Order | Start with largest denomination, use as many as possible, then smaller ones | O(d) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/easy/3-find-min-no-of-coins.py) |
| 4   | Lemonade Change | Greedy | Change Management | Greedily use larger bills first (give change with $10 before $5) | O(n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/easy/4-lemonade-change.py) |
| 5   | Valid Parenthesis Checker | Greedy | Counter Balance | Use counter to track balance, never let it go negative | O(n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/easy/5-valid-parenthesis-checker/5-valid-parenthesis-checker.py) |
| 6   | N Meetings in One Room | Greedy | Activity Selection | Sort by end time, greedily pick meetings that end earliest | O(n log n) | O(n) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/1-n-meetings-in-one-room.py) |
| 7   | Jump Game | Greedy | Reachability | Track farthest reachable position, update at each step | O(n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/2-jump-game.py) |
| 8   | Jump Game II | Greedy | Min Jumps | Count jumps when reaching end of current jump range | O(n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/3-jum-game-ii/3-jum-game-ii.py) |
| 9   | Min Platforms for Railway | Greedy | Event Sorting | Sort arrivals and departures separately, use two pointers to count platforms | O(n log n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/4-min-no-of-platform-for-rail/4-min-no-of-platform-for-rail.py) |
| 10  | Job Sequencing Problem | Greedy | Deadline Sorting | Sort by profit descending, schedule each job as late as possible | O(n²) | O(n) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/5-job-sequencing-problem/5-job-sequencing-problem.py) |
| 11  | Candy Distribution | Greedy | Two Pass | Left pass: more rating = more candy, Right pass: maintain constraint | O(n) | O(n) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/6-candy/6-candy.py) |
| 12  | Insert Interval | Greedy | Merge Logic | Add non-overlapping before, merge overlapping, add non-overlapping after | O(n) | O(n) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/9-insert-intervsl.py) |
| 13  | Merge Intervals | Greedy | Sort + Merge | Sort by start time, merge consecutive overlapping intervals | O(n log n) | O(n) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/10-merge-intervals.py) |
| 14  | Non-overlapping Intervals | Greedy | Activity Selection | Sort by end time, count how many intervals to remove to avoid overlap | O(n log n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/11-non-overlapping-intervals/11-non-overlapping-intervals.py) |

### Binary Trees

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Preorder Traversal | Tree Traversal | Root-Left-Right | Process root first, then recursively traverse left and right | O(n) | O(h) | [Solution](./a2z-sheet/13-binary-tree/5-preorder-traversal-of-binary-tree.py) |
| 2   | Inorder Traversal | Tree Traversal | Left-Root-Right | Traverse left, process root, traverse right (gives sorted order for BST) | O(n) | O(h) | [Solution](./a2z-sheet/13-binary-tree/6-inorder-traversal-of-binary-tree.py) |
| 3   | Postorder Traversal | Tree Traversal | Left-Right-Root | Process children before parent, useful for deletion/cleanup operations | O(n) | O(h) | [Solution](./a2z-sheet/13-binary-tree/7-postorder-traversal-of-binary-tree.py) |

### Binary Search Trees

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Search in BST | BST Operations | Binary Search Property | Go left if target < node.val, right if target > node.val | O(log n) | O(1) | [Solution](./a2z-sheet/14-binary-search-tree/1-concepts/2-search-in-bst.py) |
| 2   | Min Value in BST | BST Properties | Leftmost Node | Keep going left until you reach the leftmost node (smallest value) | O(log n) | O(1) | [Solution](./a2z-sheet/14-binary-search-tree/1-concepts/3-min-in-bst.py) |
| 3   | Ceil in BST | BST Operations | Lower Bound | Track smallest value >= target while traversing using BST property | O(log n) | O(1) | [Solution](./a2z-sheet/14-binary-search-tree/2-practice-problems/1-ceial-in-bst.py) |
| 4   | Insert Node in BST | BST Operations | Recursive Insertion | Find correct position using BST property, create new leaf node | O(log n) | O(log n) | [Solution](./a2z-sheet/14-binary-search-tree/2-practice-problems/3-insert-node-in-bst.py) |
| 5   | Delete Node in BST | BST Operations | Case Analysis | 3 cases: no child (remove), 1 child (replace), 2 children (inorder successor) | O(log n) | O(log n) | [Solution](./a2z-sheet/14-binary-search-tree/2-practice-problems/4-delete-node-bst/4-delete-node-bst.py) |
| 6   | Kth Smallest Element | BST Properties | Inorder Traversal | Inorder gives sorted order, return kth element during traversal | O(k) | O(log n) | [Solution](./a2z-sheet/14-binary-search-tree/2-practice-problems/5-k-smallest-element-bst/5-k-smallest-element-bst.py) |
| 7   | Validate BST | BST Properties | Range Validation | Each node must be within (min, max) range, update range recursively | O(n) | O(log n) | [Solution](./a2z-sheet/14-binary-search-tree/2-practice-problems/6-check-if-tree-is-bst.py) |
| 8   | LCA in BST | BST Properties | Path Splitting | First node where paths to p and q split (one goes left, other right) | O(log n) | O(1) | [Solution](./a2z-sheet/14-binary-search-tree/2-practice-problems/7-lca-in-binary-search-tree/7-lca-in-binary-search-tree.py) |

### Graphs

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| **Basic Traversals** |
| 1   | BFS Traversal | Graph Traversal | Level-order | Use queue, mark visited before adding to avoid re-processing | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/1-learning/5-bfs.py) |
| 2   | DFS Traversal | Graph Traversal | Depth-first | Use recursion or stack, mark visited during processing | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/1-learning/6-dfs.py) |
| 3   | Connected Components | Graph Traversal | DFS/BFS | Run DFS/BFS from each unvisited node, count number of calls | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/1-learning/4-connected-compnents.py) |
| **BFS/DFS Problems** |
| 4   | Number of Provinces | Connected Components | Union-Find/DFS | Each province is a connected component in adjacency matrix | O(V²) | O(V) | [Solution](./a2z-sheet/15-graphs/2-problems-on-bfs-dfs/1-no-of-provinces/1-no-of-provinces.py) |
| 4.1 | Connected Components (Alt) | Connected Components | DFS/BFS | Alternative implementation for counting connected components | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/2-problems-on-bfs-dfs/2-connected-compnents.py) |
| 5   | Rotten Oranges | Multi-source BFS | BFS with Time | Start BFS from all rotten oranges simultaneously, track time levels | O(m*n) | O(m*n) | [Solution](./a2z-sheet/15-graphs/2-problems-on-bfs-dfs/3-rotten-oranges/3-rotten-oranges.py) |
| 6   | Flood Fill | DFS/BFS | Color Change | DFS/BFS to change connected pixels of same color to new color | O(m*n) | O(m*n) | [Solution](./a2z-sheet/15-graphs/2-problems-on-bfs-dfs/4-flood-fill/4-flood-fill.py) |
| 7   | Cycle Detection (Undirected BFS) | Cycle Detection | BFS with Parent | If adjacent node is visited AND not parent, cycle found | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/2-problems-on-bfs-dfs/5-cycle-detection-undirected-graph-bfs.py) |
| 8   | Cycle Detection (Undirected DFS) | Cycle Detection | DFS with Parent | If adjacent node is visited AND not parent, cycle found | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/2-problems-on-bfs-dfs/6-cycle-detection-undirected-graph-dfs.py) |
| 9   | 0-1 Matrix | Multi-source BFS | Distance Calculation | BFS from all 0s simultaneously to find distance to nearest 0 | O(m*n) | O(m*n) | [Solution](./a2z-sheet/15-graphs/2-problems-on-bfs-dfs/7-0-1-matrix/7-0-1-matrix.py) |
| 10  | Surrounded Regions | DFS/BFS | Border Traversal | Mark boundary-connected 'O's as safe, convert rest to 'X' | O(m*n) | O(m*n) | [Solution](./a2z-sheet/15-graphs/2-problems-on-bfs-dfs/8-surrounded-regions/8-surrounded-regions.py) |
| 11  | Number of Enclaves | DFS/BFS | Boundary Analysis | Count land cells not reachable from boundary | O(m*n) | O(m*n) | [Solution](./a2z-sheet/15-graphs/2-problems-on-bfs-dfs/9-no-of-enclaves/9-no-of-enclaves.py) |
| 12  | Word Ladder I | BFS | Level-wise Search | BFS with word transformations, each level represents one step | O(M²*N) | O(M*N) | [Solution](./a2z-sheet/15-graphs/2-problems-on-bfs-dfs/10-word-ladder-i/10-word-ladder-i.py) |
| 13  | Bipartite Graph | DFS/BFS | 2-Coloring | Try to color graph with 2 colors, no adjacent same colors | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/2-problems-on-bfs-dfs/13-bipartite-graph/13-bipartite-graph.py) |
| **Topological Sort** |
| 13.1| Cycle Detection (Alt Method) | Cycle Detection | Schedule Detection | Alternative cycle detection for directed graphs | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/2-problems-on-bfs-dfs/14-cycle-detection-schedule-second.py) |
| 14  | Topological Sort (DFS) | Topological Sort | Finish Time | Add to result when finishing DFS (all neighbors processed) | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/3-topo-sort-and-problems/1-topological-sort-dfs.py) |
| 14.1| Cycle Detection (Undirected Alt) | Cycle Detection | BFS Alternative | Alternative BFS method for cycle detection in undirected graphs | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/3-topo-sort-and-problems/3-cycle-detection-undirected-graph-bfs.py) |
| 15  | Topological Sort (BFS - Kahn's) | Topological Sort | Indegree | Start with 0 indegree nodes, reduce indegree of neighbors | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/3-topo-sort-and-problems/2-topological-sort-bfs-kahn-algorithm.py) |
| 16  | Cycle Detection (Directed DFS) | Cycle Detection | DFS with Colors | Use 3 colors: white (unvisited), gray (visiting), black (visited) | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/3-topo-sort-and-problems/4-cycle-detection-in-directed-graph-dfs.py) |
| 17  | Course Schedule II | Topological Sort | Dependency Resolution | Use Kahn's algorithm to detect cycle and find valid ordering | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/3-topo-sort-and-problems/5-cycle-detection-course-schedule-ii.py) |
| 18  | Find Eventual Safe States | Topological Sort | Reverse Graph | Safe nodes have no outgoing edges in terminal-oriented graph | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/3-topo-sort-and-problems/6-find-eventual-safe-states/6-find-eventual-safe-states.py) |
| **Shortest Path** |
| 19  | Shortest Path (Unweighted) | BFS | Level Traversal | BFS naturally gives shortest path in unweighted graphs | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/4-shortest-path-algorithm-problems/1-shortest-path-undir-graph-unit-weight.py) |
| 20  | Shortest Path in DAG | Topological Sort + DP | Relaxation | Topologically sort, then relax edges in order | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/4-shortest-path-algorithm-problems/2-shortest-path-in-DAG/2-shortest-path-in-DAG.py) |
| 21  | Dijkstra's Algorithm | Priority Queue | Greedy Relaxation | Always process closest unvisited node, update distances | O(E log V) | O(V) | [Solution](./a2z-sheet/15-graphs/4-shortest-path-algorithm-problems/3-dijkstras-algorithm/3-dijkstras-algorithm.py) |
| 22  | Shortest Path in Binary Maze | BFS/Dijkstra | Path Finding | BFS for unweighted, Dijkstra for weighted maze traversal | O(m*n) | O(m*n) | [Solution](./a2z-sheet/15-graphs/4-shortest-path-algorithm-problems/5-shortest-path-in-binary-maze/5-shortest-path-in-binary-maze.py) |
| 23  | Path with Minimum Effort | Binary Search + DFS | Binary Search Answer | Binary search on max effort, check feasibility with DFS | O(m*n*log(max)) | O(m*n) | [Solution](./a2z-sheet/15-graphs/4-shortest-path-algorithm-problems/6-path-with-min-effort/6-path-with-min-effort.py) |
| 24  | Cheapest Flights K Stops | Modified Dijkstra | State Space | Track (node, stops) pairs, limit exploration by stops | O(E*K) | O(V*K) | [Solution](./a2z-sheet/15-graphs/4-shortest-path-algorithm-problems/7-cheapest-flight-within-k-stops/7-cheapest-flight-within-k-stops.py) |
| 25  | Network Delay Time | Dijkstra | Single Source | Find max time to reach all nodes from source using Dijkstra | O(E log V) | O(V) | [Solution](./a2z-sheet/15-graphs/4-shortest-path-algorithm-problems/8-network-delay-time/8-network-delay-time.py) |
| 26  | Bellman-Ford Algorithm | Edge Relaxation | Negative Weights | Relax all edges V-1 times, detect negative cycles | O(V*E) | O(V) | [Solution](./a2z-sheet/15-graphs/4-shortest-path-algorithm-problems/11-bellman-ford-algorithm/11-bellman-ford-algorithm.py) |
| 27  | Floyd-Warshall Algorithm | All Pairs DP | Via Vertex | Try all intermediate vertices k for paths i->j | O(V³) | O(V²) | [Solution](./a2z-sheet/15-graphs/4-shortest-path-algorithm-problems/12-floyd-warshal-algorithm/12-floyd-warshal-algorithm.py) |
| 28  | Find City with Smallest Threshold | Floyd-Warshall | Distance Analysis | Count reachable cities within threshold for each city | O(V³) | O(V²) | [Solution](./a2z-sheet/15-graphs/4-shortest-path-algorithm-problems/13-find-city-with-smallest-threshold/13-find-city-with-smallest-threshold.py) |
| **MST & Union-Find** |
| 29  | Prim's Algorithm | Greedy MST | Cut Property | Always add minimum weight edge connecting tree to non-tree | O(E log V) | O(V) | [Solution](./a2z-sheet/15-graphs/5-mst-disjoint-sets-problems/2-prims-algorithm/2-prims-algorithm.py) |
| 30  | Kruskal's Algorithm | Union-Find MST | Cycle Avoidance | Sort edges, add if doesn't create cycle using Union-Find | O(E log E) | O(V) | [Solution](./a2z-sheet/15-graphs/5-mst-disjoint-sets-problems/5-krushkal-algorithm/5-krushkal-algorithm.py) |
| 31  | Number of Operations to Connect | Union-Find | Component Counting | Count components, need (components-1) operations to connect | O(E*α(V)) | O(V) | [Solution](./a2z-sheet/15-graphs/5-mst-disjoint-sets-problems/6-no-of-operations-network-connected/6-no-of-operations-network-connected.py) |
| 32  | Most Stones Removed | Union-Find | Connected Components | Stones in same row/col are connected, remove all but one per component | O(N*α(N)) | O(N) | [Solution](./a2z-sheet/15-graphs/5-mst-disjoint-sets-problems/7-most-stones-removed-same-row-col/7-most-stones-removed-same-row-col.py) |
| 33  | Number of Islands II | Union-Find | Dynamic Connectivity | Add lands dynamically, merge adjacent components using Union-Find | O(K*α(M*N)) | O(M*N) | [Solution](./a2z-sheet/15-graphs/5-mst-disjoint-sets-problems/9-number-of-island-ii/9-number-of-island-ii.py) |

### Dynamic Programming

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| **1D DP** |
| 1   | Climbing Stairs | 1D DP | Fibonacci | Each step can be reached from previous 1 or 2 steps: dp[i] = dp[i-1] + dp[i-2] | O(n) | O(n) | [Solution](./a2z-sheet/16-dynamic-programming/2-1D-DP/1-climbing-stairs.py) |
| 2   | Frog Jump | 1D DP | Min Cost Path | Min cost to reach stone: dp[i] = min(dp[i-1] + cost1, dp[i-2] + cost2) | O(n) | O(n) | [Solution](./a2z-sheet/16-dynamic-programming/2-1D-DP/2-frog-jumps.py) |
| 3   | Frog Jump with K Distance | 1D DP | Variable Jumps | Try all possible jumps from 1 to k, take minimum cost path | O(n*k) | O(n) | [Solution](./a2z-sheet/16-dynamic-programming/2-1D-DP/3-frog-jump-with-k-distance/3-frog-jump-with-k-distance.py) |
| 4   | Maximum Sum Non-Adjacent | 1D DP | Pick/Not Pick | At each house: max(rob current + dp[i-2], skip current + dp[i-1]) | O(n) | O(n) | [Solution](./a2z-sheet/16-dynamic-programming/2-1D-DP/4-Maximum-sum-of-non-adjacent-element.py) |
| 5   | House Robber II | 1D DP | Circular Array | Run house robber twice: [0...n-2] and [1...n-1], take maximum | O(n) | O(1) | [Solution](./a2z-sheet/16-dynamic-programming/2-1D-DP/5-house-robber-ii/5-house-robber-ii.py) |
| **2D/Grid DP** |
| 6   | Ninja Training | 2D DP | State Tracking | Track max points with last activity performed to avoid consecutive repeats | O(n*4) | O(n*4) | [Solution](./a2z-sheet/16-dynamic-programming/3-2d-3d-dp-and-dp-on-grids/1-ninjas-training/ninjas-training.py) |
| 7   | Grid Unique Paths | 2D DP | Path Counting | dp[i][j] = dp[i-1][j] + dp[i][j-1], count paths from top-left to bottom-right | O(m*n) | O(m*n) | [Solution](./a2z-sheet/16-dynamic-programming/3-2d-3d-dp-and-dp-on-grids/2-grid-unique-paths/2-grid-unique-paths.py) |
| 8   | Grid Unique Paths II | 2D DP | Path Counting with Obstacles | Same as unique paths but set dp[i][j] = 0 for obstacles | O(m*n) | O(m*n) | [Solution](./a2z-sheet/16-dynamic-programming/3-2d-3d-dp-and-dp-on-grids/3-grid-unique-paths-ii.py) |
| 9   | Min Path Sum | 2D DP | Path Optimization | dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]) | O(m*n) | O(m*n) | [Solution](./a2z-sheet/16-dynamic-programming/3-2d-3d-dp-and-dp-on-grids/4-min-path-sum-in-grid.py) |
| **Subsequence DP** |
| 10  | Subset Sum Equal to Target | Subsequence DP | 0/1 Knapsack | For each element: include (target-num) OR exclude (same target) | O(n*target) | O(n*target) | [Solution](./a2z-sheet/16-dynamic-programming/4-dp-on-subsequences/1-subset-sum-equal-to-target/1-subset-sum-equal-to-target.py) |
| 11  | Partition Equal Subset Sum | Subsequence DP | Subset Sum | Check if subset with sum = total_sum/2 exists using subset sum DP | O(n*sum) | O(n*sum) | [Solution](./a2z-sheet/16-dynamic-programming/4-dp-on-subsequences/2-partition-equal-subset-sum/2-partition-equal-subset-sum.py) |
| 12  | Partition with Min Difference | Subsequence DP | Subset Sum Variant | Find all possible sums, then minimize |sum1 - sum2| = |total - 2*sum1| | O(n*sum) | O(n*sum) | [Solution](./a2z-sheet/16-dynamic-programming/4-dp-on-subsequences/3-partition-set-with-min-diff/3-partition-set-with-min-diff.py) |
| 13  | 0/1 Knapsack | Subsequence DP | Classic Knapsack | For each item: max(include: value + dp[weight-w], exclude: dp[weight]) | O(n*W) | O(n*W) | [Solution](./a2z-sheet/16-dynamic-programming/4-dp-on-subsequences/6-01-knapsack/6-01-knapsack.py) |
| 14  | Minimum Coins | Subsequence DP | Unbounded Knapsack | For each coin: min(1 + dp[amount-coin]) if coin <= amount | O(coins*amount) | O(amount) | [Solution](./a2z-sheet/16-dynamic-programming/4-dp-on-subsequences/7-minimum-coins/7-minimum-coins.py) |
| 15  | Coin Change II | Subsequence DP | Counting Ways | For each coin: dp[amount] += dp[amount-coin] if coin <= amount | O(coins*amount) | O(amount) | [Solution](./a2z-sheet/16-dynamic-programming/4-dp-on-subsequences/9-coin-change-ii/9-coin-change-ii.py) |
| **String DP** |
| 16  | Longest Common Subsequence | String DP | 2D Matching | If chars match: 1 + dp[i-1][j-1], else: max(dp[i-1][j], dp[i][j-1]) | O(n*m) | O(n*m) | [Solution](./a2z-sheet/16-dynamic-programming/5-dp-on-strings/1-longest-common-subsequence/1-longest-common-subsequence.py) |
| 17  | Print All LCS | String DP | Backtracking | Build LCS by backtracking from dp table using optimal choices | O(n*m) | O(n*m) | [Solution](./a2z-sheet/16-dynamic-programming/5-dp-on-strings/2-print-all-longest-common-subsequence/2-print-all-longest-common-subsequence.py) |
| 18  | Longest Common Substring | String DP | Continuous Matching | If chars match: 1 + dp[i-1][j-1], else: 0 (reset streak) | O(n*m) | O(n*m) | [Solution](./a2z-sheet/16-dynamic-programming/5-dp-on-strings/3-longest-common-substring/3-longest-common-substring.py) |
| 19  | Longest Palindromic Subsequence | String DP | LCS Variant | LPS(s) = LCS(s, reverse(s)) - find LCS with string and its reverse | O(n²) | O(n²) | [Solution](./a2z-sheet/16-dynamic-programming/5-dp-on-strings/4-longest-palindromic-subsequence/4-longest-palindromic-subsequence.py) |
| 20  | Min Insertions to Make Palindrome | String DP | LPS Application | Insertions needed = n - LPS(s), where LPS is longest palindromic subsequence | O(n²) | O(n²) | [Solution](./a2z-sheet/16-dynamic-programming/5-dp-on-strings/5-minimum-insertions-make-string-palindrome/5-minimum-insertions-make-string-palindrome.py) |
| 21  | Min Insert/Delete to Convert String | String DP | LCS Application | Operations = (n - LCS) + (m - LCS) where LCS is longest common subsequence | O(n*m) | O(n*m) | [Solution](./a2z-sheet/16-dynamic-programming/5-dp-on-strings/6-min-insert-del-convert-string copy/6-min-insert-del-convert-string .py) |
| 22  | Shortest Common Supersequence | String DP | LCS + Construction | Build shortest string containing both as subsequences using LCS | O(n*m) | O(n*m) | [Solution](./a2z-sheet/16-dynamic-programming/5-dp-on-strings/7-shortest-common-superseq/7-shortest-common-superseq.py) |
| 6   | Min Path Sum | 2D DP | Path Optimization | dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]) | O(m*n) | O(m*n) | [Solution](./a2z-sheet/16-dynamic-programming/3-2d-3d-dp-and-dp-on-grids/4-min-path-sum-in-grid.py) |
| 7   | Subset Sum Equal to Target | Subsequence DP | 0/1 Knapsack | For each element: include (target-num) OR exclude (same target) | O(n*target) | O(n*target) | [Solution](./a2z-sheet/16-dynamic-programming/4-dp-on-subsequences/1-subset-sum-equal-to-target/1-subset-sum-equal-to-target.py) |
| 8   | Partition Equal Subset Sum | Subsequence DP | Subset Sum | Check if subset with sum = total_sum/2 exists using subset sum DP | O(n*sum) | O(n*sum) | [Solution](./a2z-sheet/16-dynamic-programming/4-dp-on-subsequences/2-partition-equal-subset-sum/2-partition-equal-subset-sum.py) |
| 9   | Partition with Min Difference | Subsequence DP | Subset Sum Variant | Find all possible sums, then minimize \|sum1 - sum2\| = \|total - 2*sum1\| | O(n*sum) | O(n*sum) | [Solution](./a2z-sheet/16-dynamic-programming/4-dp-on-subsequences/3-partition-set-with-min-diff/3-partition-set-with-min-diff.py) |
| 10  | 0/1 Knapsack | Subsequence DP | Classic Knapsack | For each item: max(include: value + dp[weight-w], exclude: dp[weight]) | O(n*W) | O(n*W) | [Solution](./a2z-sheet/16-dynamic-programming/4-dp-on-subsequences/6-01-knapsack/6-01-knapsack.py) |
| 11  | Minimum Coins | Subsequence DP | Unbounded Knapsack | For each coin: min(1 + dp[amount-coin]) if coin <= amount | O(coins*amount) | O(amount) | [Solution](./a2z-sheet/16-dynamic-programming/4-dp-on-subsequences/7-minimum-coins/7-minimum-coins.py) |
| 12  | Coin Change II | Subsequence DP | Counting Ways | For each coin: dp[amount] += dp[amount-coin] if coin <= amount | O(coins*amount) | O(amount) | [Solution](./a2z-sheet/16-dynamic-programming/4-dp-on-subsequences/9-coin-change-ii/9-coin-change-ii.py) |

### Graphs

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | BFS Traversal | Graph Traversal | Level-order | Use queue, mark visited before adding to queue to avoid re-processing | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/1-learning/5-bfs.py) |
| 2   | DFS Traversal | Graph Traversal | Depth-first | Use recursion or stack, mark visited during processing | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/1-learning/6-dfs.py) |
| 3   | Connected Components | Graph Traversal | DFS/BFS | Run DFS/BFS from each unvisited node, count number of calls | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/1-learning/4-connected-compnents.py) |
| 4   | Cycle Detection (Undirected BFS) | Cycle Detection | BFS with Parent | If adjacent node is visited AND not parent, cycle found | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/2-problems-on-bfs-dfs/5-cycle-detection-undirected-graph-bfs.py) |
| 5   | Cycle Detection (Undirected DFS) | Cycle Detection | DFS with Parent | If adjacent node is visited AND not parent, cycle found | O(V+E) | O(V) | [Solution](./a2z-sheet/15-graphs/2-problems-on-bfs-dfs/6-cycle-detection-undirected-graph-dfs.py) |

### Greedy Algorithms

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Assign Cookies | Greedy | Two Pointers | Sort both arrays, assign smallest available cookie to smallest appetite | O(n log n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/easy/1-assign-cookies.py) |
| 2   | Lemonade Change | Greedy | Cashier Problem | Greedily use larger bills first (give change with $10 before $5) | O(n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/easy/4-lemonade-change.py) |
| 3   | N Meetings in One Room | Greedy | Activity Selection | Sort by end time, greedily pick meetings that end earliest | O(n log n) | O(n) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/1-n-meetings-in-one-room.py) |
| 4   | Jump Game | Greedy | Reach Analysis | Track farthest reachable position, update at each step | O(n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/2-jump-game.py) |
| 5   | Fractional Knapsack | Greedy | Value/Weight Ratio | Sort by value/weight ratio, pick highest ratio items first | O(n log n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/easy/2-fractional-knapsack.py) |
| 6   | Find Minimum Coins | Greedy | Largest First | Use largest denomination first, keep subtracting until amount becomes 0 | O(n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/easy/3-find-min-no-of-coins.py) |
| 7   | Valid Parenthesis Checker | Greedy | Stack Matching | Use stack to match opening and closing parentheses | O(n) | O(n) | [Solution](./a2z-sheet/12-greedy-algorithms/easy/5-valid-parenthesis-checker/5-valid-parenthesis-checker.py) |
| 8   | Jump Game II | Greedy | Range Expansion | Track current range and next reachable range, count jumps | O(n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/3-jum-game-ii/3-jum-game-ii.py) |
| 9   | Minimum Platforms | Greedy | Event Scheduling | Sort arrivals and departures, use two pointers to track overlaps | O(n log n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/4-min-no-of-platform-for-rail/4-min-no-of-platform-for-rail.py) |
| 10  | Job Sequencing | Greedy | Deadline Sorting | Sort by profit, place jobs at latest possible slot before deadline | O(n log n) | O(n) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/5-job-sequencing-problem/5-job-sequencing-problem.py) |
| 11  | Candy Distribution | Greedy | Two Passes | Left pass for ascending ratings, right pass for descending ratings | O(n) | O(n) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/6-candy/6-candy.py) |
| 12  | Insert Interval | Greedy | Merge Overlaps | Insert new interval and merge all overlapping intervals | O(n) | O(n) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/9-insert-intervsl.py) |
| 13  | Merge Intervals | Greedy | Sort and Merge | Sort by start time, merge overlapping intervals | O(n log n) | O(n) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/10-merge-intervals.py) |
| 14  | Non-overlapping Intervals | Greedy | Activity Selection | Sort by end time, count minimum removals to make non-overlapping | O(n log n) | O(1) | [Solution](./a2z-sheet/12-greedy-algorithms/medium-hard/11-non-overlapping-intervals/11-non-overlapping-intervals.py) |

### Binary Trees

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Preorder Traversal | Tree Traversal | Root-Left-Right | Process root first, then recursively traverse left and right | O(n) | O(h) | [Solution](./a2z-sheet/13-binary-tree/5-preorder-traversal-of-binary-tree.py) |
| 2   | Inorder Traversal | Tree Traversal | Left-Root-Right | Traverse left, process root, traverse right (gives sorted order for BST) | O(n) | O(h) | [Solution](./a2z-sheet/13-binary-tree/6-inorder-traversal-of-binary-tree.py) |
| 3   | Postorder Traversal | Tree Traversal | Left-Right-Root | Process children before parent, useful for deletion/cleanup | O(n) | O(h) | [Solution](./a2z-sheet/13-binary-tree/7-postorder-traversal-of-binary-tree.py) |
| 4   | Level Order Traversal | Tree Traversal | BFS | Use queue to visit nodes level by level, group by level | O(n) | O(n) | [Solution](./sde-sheet/18-binary-tree-ii/1-level-order-traversal.py) |
| 5   | Height of Binary Tree | Tree Property | DFS | Max depth from left and right subtrees + 1 | O(n) | O(h) | [Solution](./sde-sheet/18-binary-tree-ii/2-height-of-binary-tree/2-height-of-binary-tree.py) |
| 6   | Diameter of Binary Tree | Tree Property | DFS | Max of left diameter, right diameter, or path through root | O(n) | O(h) | [Solution](./sde-sheet/18-binary-tree-ii/3-diameter-of-binary-tree/3-diameter-of-binary-tree.py) |
| 7   | Balanced Binary Tree | Tree Property | Height Check | Check if height difference between subtrees ≤ 1 for all nodes | O(n) | O(h) | [Solution](./sde-sheet/18-binary-tree-ii/4-balanced-binary-tree/4-balanced-binary-tree.py) |
| 8   | LCA in Binary Tree | Tree Traversal | Bottom-up Search | If current node is target or child has target, return current | O(n) | O(h) | [Solution](./sde-sheet/18-binary-tree-ii/5-lca-in-binary-tree/5-lca-in-binary-tree.py) |
| 9   | ZigZag Traversal | Tree Traversal | Level Order + Direction | Level order but alternate direction using deque/reverse | O(n) | O(n) | [Solution](./sde-sheet/18-binary-tree-ii/7-zig-zag-traversal-of-binary-tree/7-zig-zag-traversal-of-binary-tree.py) |
| 10  | Boundary Traversal | Tree Traversal | Three Parts | Left boundary + leaves + right boundary (in reverse) | O(n) | O(h) | [Solution](./sde-sheet/18-binary-tree-ii/8-boundary-traversal-of-binary-tree/8-boundary-traversal-of-binary-tree.py) |
| 11  | Maximum Path Sum | Tree DP | Post-order | For each node, max path is max(left+node+right, global max) | O(n) | O(h) | [Solution](./sde-sheet/19-binary-tree-iii/1-maximum-path-sum/1-maximum-path-sum.py) |
| 12  | Construct Tree from Inorder+Postorder | Tree Construction | Recursion | Use postorder for root, inorder for left/right split | O(n) | O(n) | [Solution](./sde-sheet/19-binary-tree-iii/3-create-binary-tree-inorder-postorder/3-create-binary-tree-inorder-postorder.py) |
| 13  | Symmetric Binary Tree | Tree Property | DFS | Check if left subtree mirrors right subtree | O(n) | O(h) | [Solution](./sde-sheet/19-binary-tree-iii/4-symmetric-binary-tree/4-symmetric-binary-tree.py) |
| 14  | Flatten Tree to Linked List | Tree Transformation | Modified Postorder | Convert right subtree, left subtree, then connect | O(n) | O(h) | [Solution](./sde-sheet/19-binary-tree-iii/6-check-to-mirror-binary-tree/6-convert-to-mirror-binary-tree.py) |
| 15  | Children Sum Property | Tree Property | DFS | Check if parent equals sum of children for all nodes | O(n) | O(h) | [Solution](./sde-sheet/19-binary-tree-iii/7-check-children-sum-property/7-check-children-sum-property.py) |

### Binary Search Trees

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Search in BST | BST Operations | Binary Search | Go left if target < node.val, right if target > node.val | O(log n) | O(1) | [Solution](./a2z-sheet/14-binary-search-tree/1-concepts/2-search-in-bst.py) |
| 2   | Min in BST | BST Properties | Leftmost Node | Keep going left until you reach leftmost node | O(log n) | O(1) | [Solution](./a2z-sheet/14-binary-search-tree/1-concepts/3-min-in-bst.py) |
| 3   | Ceil in BST | BST Operations | Lower Bound | Track smallest value >= target while traversing | O(log n) | O(1) | [Solution](./a2z-sheet/14-binary-search-tree/2-practice-problems/1-ceial-in-bst.py) |
| 4   | Insert Node in BST | BST Operations | Recursive Insertion | Find correct position using BST property, create new node | O(log n) | O(log n) | [Solution](./a2z-sheet/14-binary-search-tree/2-practice-problems/3-insert-node-in-bst.py) |
| 5   | Delete Node BST | BST Operations | Case Analysis | 3 cases: no child (remove), 1 child (replace), 2 children (inorder successor) | O(log n) | O(log n) | [Solution](./a2z-sheet/14-binary-search-tree/2-practice-problems/4-delete-node-bst/4-delete-node-bst.py) |
| 6   | Kth Smallest Element BST | BST Properties | Inorder Traversal | Inorder gives sorted order, return kth element during traversal | O(k) | O(log n) | [Solution](./a2z-sheet/14-binary-search-tree/2-practice-problems/5-k-smallest-element-bst/5-k-smallest-element-bst.py) |
| 7   | Validate BST | BST Properties | Range Validation | Each node must be within (min, max) range, update range recursively | O(n) | O(log n) | [Solution](./a2z-sheet/14-binary-search-tree/2-practice-problems/6-check-if-tree-is-bst.py) |
| 8   | LCA in BST | BST Properties | Path Splitting | First node where paths to p and q split (one goes left, other right) | O(log n) | O(1) | [Solution](./a2z-sheet/14-binary-search-tree/2-practice-problems/7-lca-in-binary-search-tree/7-lca-in-binary-search-tree.py) |

### Recursion

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Print All Subsequences | Recursion | Include/Exclude | At each element: generate subsequences with and without current element | O(2^n) | O(n) | [Solution](./a2z-sheet/7-recursion/2-subsequences-pattern/3-print-all-subsequences-power-set.py) |

### Stack & Queues

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Count Greater Elements to Right | Monotonic Stack | Query Processing | For each query index, count elements to right that are greater than element at index | O(N*Q) | O(Q) | [Solution](./a2z-sheet/9-stack-and-queues/3-monotonic-stack-and-queues/4-number-of-nge-to-right.py) |

### Advanced Strings

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Find First Occurrence (Z-Algorithm) | String Pattern | Z-Algorithm | Combine pattern + "$" + text, find positions where Z[i] equals pattern length | O(m+n) | O(m+n) | [Solution](./a2z-sheet/18-strings/5-z-function/5-z-function.py) |

---

## SDE Sheet Problems

### Arrays

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Pow(x, n) | Math | Fast Exponentiation | If n is even: x^n = (x^(n/2))^2, if odd: x^n = x * x^(n-1) | O(log n) | O(log n) | [Solution](./sde-sheet/3-arrays-part-III/2-pow-x-n.py) |
| 2   | Two Sum | Array | Hash Map | Store target-current in dict, check if current exists | O(n) | O(n) | [Solution](./sde-sheet/4-arrays-IV/1-two-sum.py) |

### Linked Lists

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Reverse Linked List | Linked List | Three Pointers | Track prev, current, next. Reverse links one by one | O(n) | O(1) | [Solution](./sde-sheet/5-linked-list/1-reverse-linked-list.py) |
| 2   | Find Middle of Linked List | Linked List | Two Pointers (Tortoise & Hare) | Slow pointer moves 1 step, fast moves 2 steps. When fast reaches end, slow is at middle | O(n) | O(1) | [Solution](./sde-sheet/5-linked-list/2-find-the-middle-of-linked-list/2-find-the-middle-of-linked-list.py) |

### Greedy Algorithms

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | N Meetings in One Room | Greedy | Activity Selection | Sort by end time, greedily pick meetings that end earliest | O(n log n) | O(n) | [Solution](./sde-sheet/8-greedy-algorithm/1-n-meetings-in-one-room.py) |
| 2   | Fractional Knapsack | Greedy | Value/Weight Ratio | Sort by value/weight ratio, pick highest ratio items first | O(n log n) | O(1) | [Solution](./sde-sheet/8-greedy-algorithm/4-fractional-knapsack.py) |
| 3   | Maximum Activities | Greedy | Activity Selection | Same as N meetings - sort by finish time, greedily select non-overlapping activities | O(n log n) | O(n) | [Solution](./sde-sheet/8-greedy-algorithm/6-activity-selection/6-activity-selection.py) |

### Recursion & Backtracking

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Subset Sums | Recursion | Include/Exclude | Generate all possible subset sums using pick/not-pick pattern | O(2^n) | O(2^n) | [Solution](./sde-sheet/9-recursion/1-subset-sums.py) |
| 2   | Subsets II | Recursion | Backtracking with Duplicates | Sort array, skip duplicates at same recursion level | O(2^n) | O(2^n) | [Solution](./sde-sheet/9-recursion/2-subset-II.py) |
| 3   | Palindrome Partitioning | Recursion | Backtracking | At each position, try all possible palindromic partitions | O(2^n * n) | O(n) | [Solution](./sde-sheet/9-recursion/5-palindrome-partitioning.py) |
| 4   | N-Queens | Backtracking | Constraint Satisfaction | Place queens one by one, backtrack when conflicts arise | O(n!) | O(n) | [Solution](./sde-sheet/10-recursion-backtracking/2-n-queens-problem.py) |

### Stack & Queue

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Implement Stack using Arrays | Stack | Array Implementation | Use array with top pointer, resize when needed | O(1) | O(n) | [Solution](./sde-sheet/13-stack-and-queue/1-implement-stack-using-arrays.py) |
| 2   | Implement Queue using Array | Queue | Circular Array | Use front and rear pointers, wrap around using modulo | O(1) | O(n) | [Solution](./sde-sheet/13-stack-and-queue/2-implement-queue-using-array.py) |
| 3   | Implement Stack using Queue | Stack | Queue Operations | Use one/two queues, move elements to simulate LIFO behavior | O(n) push | O(n) | [Solution](./sde-sheet/13-stack-and-queue/3-implement-stack-using-queue/3-implement-stack-using-queue.py) |
| 4   | Implement Queue using Stacks | Queue | Stack Operations | Use two stacks: one for enqueue, transfer to other for dequeue | O(1) amortized | O(n) | [Solution](./sde-sheet/13-stack-and-queue/4-implement-queue-using-stacks/4-implement-queue-using-stacks.py) |
| 5   | Valid Parentheses | Stack | Matching Pairs | Use stack to match opening brackets with closing ones | O(n) | O(n) | [Solution](./sde-sheet/13-stack-and-queue/5-valid-parentheses.py) |
| 6   | Next Greater Element | Stack | Monotonic Stack | Use stack to track elements waiting for next greater element | O(n) | O(n) | [Solution](./sde-sheet/13-stack-and-queue/6-next-greater-element/6-next-greater-element.py) |
| 7   | Sort a Stack | Stack | Recursion | Use recursion to sort: remove top, sort remaining, insert in sorted position | O(n²) | O(n) | [Solution](./sde-sheet/13-stack-and-queue/7-sort-a-stack/7-sort-a-stack.py) |

### Advanced Stack & Queue

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Next Smaller Element | Stack | Monotonic Stack | Similar to next greater, but maintain increasing stack | O(n) | O(n) | [Solution](./sde-sheet/14-stack-queues-ii/1-next-smaller-element.py) |
| 2   | LRU Cache | Design | Hash + Doubly LL | HashMap for O(1) access + DLL for O(1) insertion/deletion | O(1) | O(capacity) | [Solution](./sde-sheet/14-stack-queues-ii/2-lru-cache/2-lru-cache.py) |
| 3   | Largest Rectangle in Histogram | Stack | Next/Prev Smaller | For each bar, find area using next smaller and previous smaller elements | O(n) | O(n) | [Solution](./sde-sheet/14-stack-queues-ii/4-largest-rectangle-in-histogram/4-largest-rectangle-in-histogram.py) |
| 4   | Sliding Window Maximum | Queue | Deque | Use deque to maintain decreasing order of elements in current window | O(n) | O(k) | [Solution](./sde-sheet/14-stack-queues-ii/5-sliding-window-maximum/5-sliding-window-maximum.py) |
| 5   | Min Stack | Stack | Auxiliary Stack | Use additional stack to track minimum at each level | O(1) | O(n) | [Solution](./sde-sheet/14-stack-queues-ii/6-implement-min-stack/6-implement-min-stack.py) |
| 6   | Rotten Oranges | BFS | Multi-source BFS | Start BFS from all rotten oranges simultaneously, track time | O(m*n) | O(m*n) | [Solution](./sde-sheet/14-stack-queues-ii/7-rotten-oranges/7-rotten-oranges.py) |
| 7   | Stock Span Problem | Stack | Monotonic Stack | Use stack to store (price, index), find spans by comparing with previous greater elements | O(n) | O(n) | [Solution](./sde-sheet/14-stack-queues-ii/8-stock-span-problem/8-stock-span-problem.py) |

### String

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Reverse Words in String | String | Two Pointers | Parse words from right to left, build result string | O(n) | O(n) | [Solution](./sde-sheet/15-string/1-reverse-words-in-string/1-reverse-words-in-string.py) |

### Binary Search Tree

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Populate Next Right Pointers | Tree | Level-order Traversal | Connect nodes at same level using BFS or recursion | O(n) | O(1) | [Solution](./sde-sheet/20-binary-serach-tree/1-populate-next-right-pointers-of-tree.py) |
| 2   | Search in BST | BST | Binary Search Property | Navigate left/right based on value comparison | O(log n) | O(log n) | [Solution](./sde-sheet/20-binary-serach-tree/2-search-key-in-bst/2-search-key-in-bst.py) |
| 3   | Floor in BST | BST | Lower Bound | Track largest value <= target while traversing BST | O(log n) | O(log n) | [Solution](./sde-sheet/21-binary-search-tree-II/1-floor-in-bst.py) |

### Binary Tree Advanced

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | All Tree Traversals in One | Tree Traversal | Single Function | Use one recursive function to build all three traversal lists | O(n) | O(n) | [Solution](./sde-sheet/17-binary-tree/9-pre-post-in-order-single-traversal.py) |
| 2   | Root to Node Path | Tree Traversal | Path Tracking | Use recursion with path building to find all root-to-leaf paths | O(n) | O(h) | [Solution](./sde-sheet/17-binary-tree/11-root-to-node-path-binary-tree.py) |
| 3   | Left View Binary Tree | Tree View | Level-order First | For each level, first node encountered is part of left view | O(n) | O(h) | [Solution](./sde-sheet/17-binary-tree/6-left-view-binary-tree/6-left-view-binary-tree.py) |
| 4   | Bottom View Binary Tree | Tree View | Horizontal Distance | Track rightmost node at each horizontal distance using level-order | O(n) | O(n) | [Solution](./sde-sheet/17-binary-tree/7-bottom-view-of-binary-tree/7-bottom-view-of-binary-tree.py) |
| 5   | Top View Binary Tree | Tree View | Horizontal Distance | Track first node at each horizontal distance using level-order | O(n) | O(n) | [Solution](./sde-sheet/17-binary-tree/8-top-view-of-binary-tree/8-top-view-of-binary-tree.py) |
| 6   | Vertical Order Traversal | Tree Traversal | Coordinates | Sort nodes by (col, row, value) to get vertical column-wise order | O(n log n) | O(n) | [Solution](./sde-sheet/17-binary-tree/10-vertical-order-traversal/10-vertical-order-traversal.py) |
| 7   | Maximum Width Binary Tree | Tree Property | Level Indexing | Use position indices to calculate width, handle overflow with offset | O(n) | O(w) | [Solution](./sde-sheet/17-binary-tree/12-max-width-binary-tree/12-max-width-binary-tree.py) |

### Heaps

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Implement Min Heap | Heap | Array Implementation | Use array with heapify up/down, parent at (i-1)//2, children at 2*i+1, 2*i+2 | O(log n) | O(n) | [Solution](./sde-sheet/12-heaps/1-implement-min-heap/1-implement-min-heap.py) |

### Graph Algorithms

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | BFS | Graph Traversal | Level-order | Use queue to visit nodes level by level | O(V+E) | O(V) | [Solution](./sde-sheet/23-graph/2-bfs.py) |
| 2   | DFS | Graph Traversal | Depth-first | Use recursion or stack to go deep before exploring siblings | O(V+E) | O(V) | [Solution](./sde-sheet/23-graph/3-dfs.py) |
| 3   | Cycle Detection (Undirected BFS) | Cycle Detection | BFS with Parent | If adjacent is visited and not parent, cycle exists | O(V+E) | O(V) | [Solution](./sde-sheet/23-graph/4-cycle-detection-undirected-graph-bfs.py) |
| 4   | Cycle Detection (Undirected DFS) | Cycle Detection | DFS with Parent | If adjacent is visited and not parent, cycle exists | O(V+E) | O(V) | [Solution](./sde-sheet/23-graph/5-cycle-detection-undirected-graph-dfs.py) |
| 5   | Cycle Detection (Directed DFS) | Cycle Detection | DFS with Colors | Use 3 colors: white (unvisited), gray (visiting), black (visited) | O(V+E) | O(V) | [Solution](./sde-sheet/23-graph/6-cycle-detection-in-directed-graph-dfs.py) |
| 6   | Topological Sort (BFS - Kahn's) | Topological Sort | Indegree | Start with 0 indegree nodes, reduce indegree of neighbors | O(V+E) | O(V) | [Solution](./sde-sheet/23-graph/8-topological-sort-bfs-kahn-algorithm.py) |
| 7   | Topological Sort (DFS) | Topological Sort | Finish Time | Add to result when finishing DFS (all neighbors processed) | O(V+E) | O(V) | [Solution](./sde-sheet/23-graph/9-topological-sort-dfs.py) |

### Dynamic Programming

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Maximum Product Subarray | Array DP | Track Min/Max | Track both min and max product (negative numbers can flip min/max) | O(n) | O(1) | [Solution](./sde-sheet/25-dynamic-programming/1-max-product-subarray.py) |
| 2   | Min Path Sum (Grid) | 2D DP | Path Optimization | dp[i][j] = grid[i][j] + min(top, left) | O(m*n) | O(m*n) | [Solution](./sde-sheet/26-dynamic-programming-ii/1-min-path-sum-in-grid.py) |

### Trie

| No. | Problem Name | Category | Pattern | Key Trick | Time | Space | Solution |
|-----|--------------|----------|---------|-----------|------|-------|----------|
| 1   | Implement Trie | Trie | Prefix Tree | Use array of 26 children + end flag for each node | O(word_length) | O(total_chars) | [Solution](./sde-sheet/27-trie/1-implement-trie-prefix-tree.py) |
| 2   | Implement Trie II | Trie | Count Tracking | Add count variables to track word frequency and prefix count | O(word_length) | O(total_chars) | [Solution](./sde-sheet/27-trie/2-implement-trie-prefix-tree-II.py) |
| 3   | Longest String with All Prefixes | Trie | Prefix Chain | String is complete if all its prefixes exist in trie | O(total_chars) | O(total_chars) | [Solution](./sde-sheet/27-trie/3-longest-string-with-all-prefixes.py) |
| 4   | Complete String | Trie | Prefix Validation | Check if every prefix of string exists as complete word in trie | O(total_chars) | O(total_chars) | [Solution](./sde-sheet/27-trie/3-complete-string.py) |
| 5   | Number of Distinct Substrings | Trie | Suffix Insertion | Insert all suffixes into trie, count total nodes created | O(n²) | O(n²) | [Solution](./sde-sheet/27-trie/4-no-of-distinct-substrings-in-string.py) |
| 6   | Max XOR of Two Numbers | Trie | Bit Trie | Build binary trie, for each number find max XOR by going opposite bits | O(n*32) | O(n*32) | [Solution](./sde-sheet/27-trie/6-max-xor-of-two-nums-arr.py) |
| 7   | Max XOR with Element from Array | Trie | Offline Queries | Sort queries by limit, add numbers to trie as limit increases | O(q*32 + n*32) | O(n*32) | [Solution](./sde-sheet/27-trie/7-max-xor-with-element-of-array.py) |

---

## Quick Tips for Revision

### Common Patterns to Remember:
1. **Two Pointers**: Array problems with sorted input or need to find pairs
2. **Sliding Window**: Subarray problems with contiguous elements
3. **Hash Map**: When you need O(1) lookup for seen elements
4. **Stack**: For problems involving matching, next greater/smaller, parsing
5. **Queue/BFS**: Level-order traversal, shortest path in unweighted graphs
6. **DFS**: Exhaustive search, tree traversals, graph connectivity
7. **Dynamic Programming**: Optimization problems with overlapping subproblems
8. **Greedy**: When local optimal choice leads to global optimum
9. **Binary Search**: Search in sorted space or search for answers
10. **Trie**: String matching, prefix problems, autocomplete features

### Time Complexity Quick Reference:
- **O(1)**: Hash operations, stack/queue operations
- **O(log n)**: Binary search, balanced BST operations
- **O(n)**: Linear scan, BFS/DFS, one-pass algorithms
- **O(n log n)**: Efficient sorting, heap operations
- **O(n²)**: Nested loops, certain DP problems
- **O(2^n)**: Generating all subsets, exponential algorithms

### Space Complexity Quick Reference:
- **O(1)**: No extra space (apart from variables)
- **O(log n)**: Recursion depth for balanced trees
- **O(n)**: Arrays, hash maps, stack/queue
- **O(n²)**: 2D arrays, adjacency matrices
