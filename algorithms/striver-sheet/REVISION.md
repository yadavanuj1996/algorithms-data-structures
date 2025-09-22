# Striver Sheet - Algorithm Core Code Snippets

This file contains the core algorithm implementations for quick revision. Each snippet contains the essential algorithm without the complete solution structure.

## Arrays

### 1. Find Second Largest Element
```python
# Core algorithm: Two variables to track largest and second largest
large = float('-inf')
second_large = float('-inf')

for i in range(n):
    if arr[i] > large:
        second_large = large  # Update second before updating largest
        large = arr[i]
    elif arr[i] > second_large and arr[i] != large:
        second_large = arr[i]
```

### 2. Check if Array is Sorted
```python
# Core algorithm: Compare adjacent elements
for i in range(1, n):
    if arr[i] < arr[i-1]:
        return False
return True
```

### 3. Remove Duplicates from Sorted Array
```python
# Core algorithm: Two pointers approach
i = 0  # Slow pointer for unique position
for j in range(1, n):  # Fast pointer for scanning
    if arr[j] != arr[i]:
        i += 1
        arr[i] = arr[j]
return i + 1  # Length of unique array
```

### 4. Left Rotate Array by One
```python
# Core algorithm: Store first, shift all left
temp = arr[0]
for i in range(n-1):
    arr[i] = arr[i+1]
arr[n-1] = temp
```

### 5. Left Rotate Array by D Places
```python
# Core algorithm: Array slicing
arr = arr[d:] + arr[:d]
```

### 6. Move Zeros to End
```python
# Core algorithm: Two pointers for zero and non-zero
i = 0  # Points to first zero
for j in range(n):  # Scans for non-zero
    if arr[j] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
```

### 7. Longest Subarray with Sum K
```python
# Core algorithm: Sliding window with two pointers
left = right = 0
current_sum = 0
max_len = 0

while right < n:
    current_sum += arr[right]

    while current_sum > k and left <= right:
        current_sum -= arr[left]
        left += 1

    if current_sum == k:
        max_len = max(max_len, right - left + 1)

    right += 1
```

### 8. Two Sum
```python
# Core algorithm: Hash map for complement lookup
hash_map = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in hash_map:
        return [hash_map[complement], i]
    hash_map[num] = i
```

### 9. Count Subarrays with Given Sum
```python
# Core algorithm: Prefix sum with hash map
prefix_sum = 0
count = 0
hash_map = {0: 1}  # Initialize for subarrays starting from index 0

for num in arr:
    prefix_sum += num
    if (prefix_sum - k) in hash_map:
        count += hash_map[prefix_sum - k]

    hash_map[prefix_sum] = hash_map.get(prefix_sum, 0) + 1
```

### 10. Pascal's Triangle
```python
# Core algorithm: Mathematical formula for each row
def generate_row(row):
    result = [1]
    element = 1

    for col in range(1, row):
        element = element * (row - col) // col
        result.append(element)

    return result

# Generate full triangle
triangle = []
for i in range(num_rows):
    triangle.append(generate_row(i + 1))
```

## Binary Search

### 1. Binary Search
```python
# Core algorithm: Divide search space in half
left, right = 0, len(arr) - 1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```

### 2. Lower Bound
```python
# Core algorithm: Find smallest index where arr[i] >= x
left, right = 0, n
result = n

while left < right:
    mid = (left + right) // 2
    if arr[mid] >= x:
        result = mid
        right = mid
    else:
        left = mid + 1
return result
```

### 3. Single Element in Sorted Array
```python
# Core algorithm: Index parity check using XOR
left, right = 0, n - 1

while left < right:
    mid = (left + right) // 2
    # If mid is even and nums[mid] == nums[mid+1], or
    # mid is odd and nums[mid] == nums[mid-1], single element is on right
    if nums[mid] == nums[mid ^ 1]:
        left = mid + 1
    else:
        right = mid
return nums[left]
```

### 4. Find Peak Element
```python
# Core algorithm: Compare with next element
left, right = 0, n - 1

while left < right:
    mid = (left + right) // 2
    if nums[mid] < nums[mid + 1]:
        left = mid + 1  # Peak is on right (upward slope)
    else:
        right = mid     # Peak is on left or at mid
return left
```

## Linked Lists

### 1. Reverse Linked List (Iterative)
```python
# Core algorithm: Three pointers
prev = None
curr = head

while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp

return prev  # New head
```

### 2. Detect Loop in Linked List
```python
# Core algorithm: Floyd's cycle detection (tortoise and hare)
slow = fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        return True  # Loop found
return False
```

### 3. Find Starting Point of Loop
```python
# Core algorithm: Reset slow to head after detecting loop
# First detect the loop
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        break

# Move slow to head, keep fast at meeting point
slow = head
while slow != fast:
    slow = slow.next
    fast = fast.next

return slow  # Starting point of loop
```

### 4. Check if Linked List is Palindrome
```python
# Core algorithm: Find middle, reverse second half, compare
# Find middle
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

# Reverse second half
prev = None
while slow:
    next_temp = slow.next
    slow.next = prev
    prev = slow
    slow = next_temp

# Compare first half with reversed second half
left, right = head, prev
while right:  # Right will be shorter or equal
    if left.val != right.val:
        return False
    left = left.next
    right = right.next
return True
```

## Recursion

### 1. Pow(x, n)
```python
# Core algorithm: Fast exponentiation
def myPow(x, n):
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    current_power = x

    while n > 0:
        if n % 2 == 1:  # If n is odd
            result *= current_power
        current_power *= current_power
        n //= 2

    return result
```

### 2. Generate All Binary Strings
```python
# Core algorithm: Include/exclude pattern
def generate(s, index):
    if index == n:
        result.append(s)
        return

    # Try '0'
    generate(s + '0', index + 1)
    # Try '1'
    generate(s + '1', index + 1)
```

### 3. Count Subsequences with Sum K
```python
# Core algorithm: Include/exclude with count
def count_subsequences(arr, index, current_sum, target):
    if index == len(arr):
        return 1 if current_sum == target else 0

    # Include current element
    include = count_subsequences(arr, index + 1, current_sum + arr[index], target)
    # Exclude current element
    exclude = count_subsequences(arr, index + 1, current_sum, target)

    return include + exclude
```

### 4. Combination Sum
```python
# Core algorithm: Unlimited use of elements
def combination_sum(candidates, index, target, current):
    if target == 0:
        result.append(current[:])
        return
    if index >= len(candidates) or target < 0:
        return

    # Include current element (can use unlimited times)
    current.append(candidates[index])
    combination_sum(candidates, index, target - candidates[index], current)
    current.pop()

    # Move to next element
    combination_sum(candidates, index + 1, target, current)
```

## Greedy Algorithms

### 1. N Meetings in One Room
```python
# Core algorithm: Sort by end time, greedily pick
meetings = [(start[i], end[i], i+1) for i in range(n)]
meetings.sort(key=lambda x: x[1])  # Sort by end time

selected = [meetings[0]]
last_end = meetings[0][1]

for i in range(1, n):
    if meetings[i][0] > last_end:  # No overlap
        selected.append(meetings[i])
        last_end = meetings[i][1]
```

### 2. Jump Game
```python
# Core algorithm: Track farthest reachable
farthest = 0
for i in range(len(nums)):
    if i > farthest:
        return False
    farthest = max(farthest, i + nums[i])
return True
```

### 3. Jump Game II
```python
# Core algorithm: BFS-like approach
jumps = 0
current_end = 0
farthest = 0

for i in range(len(nums) - 1):
    farthest = max(farthest, i + nums[i])

    if i == current_end:
        jumps += 1
        current_end = farthest
```

### 4. Candy Distribution
```python
# Core algorithm: Two passes (left-to-right, right-to-left)
candies = [1] * n

# Left to right pass
for i in range(1, n):
    if ratings[i] > ratings[i-1]:
        candies[i] = candies[i-1] + 1

# Right to left pass
for i in range(n-2, -1, -1):
    if ratings[i] > ratings[i+1]:
        candies[i] = max(candies[i], candies[i+1] + 1)
```

## Binary Trees

### 1. Preorder Traversal
```python
# Core algorithm: Root -> Left -> Right
def preorder(root):
    if not root:
        return

    result.append(root.val)  # Process root
    preorder(root.left)      # Traverse left
    preorder(root.right)     # Traverse right
```

### 2. Inorder Traversal
```python
# Core algorithm: Left -> Root -> Right
def inorder(root):
    if not root:
        return

    inorder(root.left)       # Traverse left
    result.append(root.val)  # Process root
    inorder(root.right)      # Traverse right
```

### 3. Postorder Traversal
```python
# Core algorithm: Left -> Right -> Root
def postorder(root):
    if not root:
        return

    postorder(root.left)     # Traverse left
    postorder(root.right)    # Traverse right
    result.append(root.val)  # Process root
```

## Binary Search Trees

### 1. Search in BST
```python
# Core algorithm: Use BST property to navigate
def searchBST(root, val):
    if not root or root.val == val:
        return root

    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)
```

### 2. Insert Node in BST
```python
# Core algorithm: Find correct position using BST property
def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)

    return root
```

### 3. Delete Node in BST
```python
# Core algorithm: Handle 3 cases
def deleteNode(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:  # Found the node to delete
        # Case 1: No child
        if not root.left and not root.right:
            return None
        # Case 2: One child
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        # Case 3: Two children - replace with inorder successor
        else:
            successor = find_min(root.right)
            root.val = successor.val
            root.right = deleteNode(root.right, successor.val)

    return root
```

## Graphs

### 1. BFS Traversal
```python
# Core algorithm: Level-order traversal using queue
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result
```

### 2. DFS Traversal
```python
# Core algorithm: Depth-first using recursion
def dfs(graph, node, visited, result):
    visited.add(node)
    result.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
```

### 3. Topological Sort (Kahn's Algorithm)
```python
# Core algorithm: Remove nodes with indegree 0
from collections import deque

def topological_sort(graph, indegree):
    queue = deque([i for i in range(len(indegree)) if indegree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result
```

### 4. Dijkstra's Algorithm
```python
# Core algorithm: Greedy shortest path using priority queue
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            distance = current_dist + weight
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(pq, (distance, v))

    return dist
```

## Dynamic Programming

### 1. Climbing Stairs
```python
# Core algorithm: Fibonacci pattern
dp = [0] * (n + 1)
dp[0] = dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]  # Ways to reach i = ways to reach i-1 + ways to reach i-2
```

### 2. House Robber
```python
# Core algorithm: Pick or not pick
dp = [0] * n
dp[0] = nums[0]
if n > 1:
    dp[1] = max(nums[0], nums[1])

for i in range(2, n):
    dp[i] = max(nums[i] + dp[i-2], dp[i-1])  # Rob current + i-2, or skip current
```

### 3. Unique Paths
```python
# Core algorithm: Sum of paths from top and left
dp = [[0] * n for _ in range(m)]

# Base cases
for i in range(m):
    dp[i][0] = 1
for j in range(n):
    dp[0][j] = 1

for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

### 4. 0/1 Knapsack
```python
# Core algorithm: Include or exclude each item
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weights[i-1] <= w:
            dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]
```

### 5. Longest Common Subsequence
```python
# Core algorithm: Match characters or take max from subproblems
dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

for i in range(1, len(text1) + 1):
    for j in range(1, len(text2) + 1):
        if text1[i-1] == text2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```