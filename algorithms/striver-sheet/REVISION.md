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

### 3. Upper Bound
```python
# Core algorithm: Find smallest index where arr[i] > x
left, right = 0, n

while left < right:
    mid = (left + right) // 2
    if arr[mid] > x:
        right = mid
    else:
        left = mid + 1
return left
```

### 4. Search Insert Position
```python
# Core algorithm: Use lower bound logic
left, right = 0, len(nums)

while left < right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid
return left
```

### 5. Find First/Last Occurrence
```python
# Core algorithm: Modified binary search for boundaries
def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
```

### 6. Single Element in Sorted Array
```python
# Core algorithm: Index parity check using XOR
left, right = 0, n - 1

while left < right:
    mid = (left + right) // 2
    # XOR trick: if mid is even and nums[mid] == nums[mid+1], or
    # mid is odd and nums[mid] == nums[mid-1], single element is on right
    if nums[mid] == nums[mid ^ 1]:
        left = mid + 1
    else:
        right = mid
return nums[left]
```

### 7. Find Peak Element
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

## Strings

### 1. Remove Outermost Parentheses
```python
# Core algorithm: Counter to track primitive groups
count = 0
result = ""

for ch in s:
    if ch == "(" and count == 0:
        count += 1  # Start of new primitive, don't add
    elif ch == "(" and count > 0:
        result += ch  # Add inner opening parenthesis
        count += 1
    elif ch == ")" and count == 1:
        count -= 1  # End of primitive, don't add
    elif ch == ")" and count > 1:
        result += ch  # Add inner closing parenthesis
        count -= 1
```

### 2. Reverse Words in String
```python
# Core algorithm: Parse from right to left
words = s.strip().split()
return ' '.join(reversed(words))

# Alternative approach - manual parsing
i = len(s) - 1
result = []

while i >= 0:
    # Skip spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Extract word
    if i >= 0:
        word_end = i
        while i >= 0 and s[i] != ' ':
            i -= 1
        result.append(s[i+1:word_end+1])
```

### 3. Largest Odd Number in String
```python
# Core algorithm: Find rightmost odd digit
for i in range(len(num) - 1, -1, -1):
    if int(num[i]) % 2 == 1:
        return num[:i+1]
return ""
```

### 4. Longest Common Prefix
```python
# Core algorithm: Vertical scanning
if not strs:
    return ""

for i in range(len(strs[0])):
    char = strs[0][i]
    for j in range(1, len(strs)):
        if i >= len(strs[j]) or strs[j][i] != char:
            return strs[0][:i]
return strs[0]
```

### 5. Rotate String
```python
# Core algorithm: Check if goal exists in s+s
return len(goal) == len(s) and goal in s + s
```

### 6. Valid Anagram
```python
# Core algorithm: Character frequency count
from collections import Counter
return Counter(s) == Counter(t)

# Alternative - sorting
return sorted(s) == sorted(t)
```

### 7. Reverse Every Word
```python
# Core algorithm: Split, reverse each word, join
words = s.split(' ')
reversed_words = [word[::-1] for word in words]
return ' '.join(reversed_words)
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

### 2. Reverse Linked List (Recursive)
```python
# Core algorithm: Recursion with base case
def reverse_recursive(head):
    if not head or not head.next:
        return head

    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head
```

### 3. Detect Loop in Linked List
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

### 4. Find Starting Point of Loop
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

### 5. Length of Loop
```python
# Core algorithm: Count steps in the loop
# First detect loop and find meeting point
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        break

# Count loop length
count = 1
temp = slow.next
while temp != slow:
    count += 1
    temp = temp.next

return count
```

### 6. Check if Linked List is Palindrome
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

### 7. Segregate Odd Even Nodes
```python
# Core algorithm: Maintain odd and even pointers
odd = head
even = head.next
even_head = even

while even and even.next:
    odd.next = even.next
    odd = odd.next
    even.next = odd.next
    even = even.next

odd.next = even_head  # Connect odd tail to even head
```

### 8. Remove Nth Node from End
```python
# Core algorithm: Two pointers with gap
dummy = ListNode(0)
dummy.next = head
fast = slow = dummy

# Move fast n+1 steps ahead
for _ in range(n + 1):
    fast = fast.next

# Move both until fast reaches end
while fast:
    fast = fast.next
    slow = slow.next

slow.next = slow.next.next  # Remove node
return dummy.next
```

### 9. Delete Middle Node
```python
# Core algorithm: Slow/fast pointers with previous tracking
prev = None
slow = fast = head

while fast and fast.next:
    prev = slow
    slow = slow.next
    fast = fast.next.next

prev.next = slow.next  # Delete middle node
```

### 10. Sort List with 0s, 1s, 2s
```python
# Core algorithm: Count frequencies, then overwrite
count_0 = count_1 = count_2 = 0
temp = head

# Count frequencies
while temp:
    if temp.val == 0:
        count_0 += 1
    elif temp.val == 1:
        count_1 += 1
    else:
        count_2 += 1
    temp = temp.next

# Overwrite values
temp = head
while count_0 > 0:
    temp.val = 0
    temp = temp.next
    count_0 -= 1

while count_1 > 0:
    temp.val = 1
    temp = temp.next
    count_1 -= 1

while count_2 > 0:
    temp.val = 2
    temp = temp.next
    count_2 -= 1
```

### 11. Intersection Point of Two Lists
```python
# Core algorithm: Calculate length difference
def get_length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

len_a = get_length(headA)
len_b = get_length(headB)
diff = abs(len_a - len_b)

# Move longer list pointer ahead
if len_a > len_b:
    for _ in range(diff):
        headA = headA.next
else:
    for _ in range(diff):
        headB = headB.next

# Find intersection
while headA and headB:
    if headA == headB:
        return headA
    headA = headA.next
    headB = headB.next

return None
```

### 12. Add One to Number as Linked List
```python
# Core algorithm: Reverse, add 1 with carry, reverse back
# Reverse the linked list
prev = None
curr = head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp

# Add 1 with carry
carry = 1
curr = prev
while curr and carry:
    curr.val += carry
    carry = curr.val // 10
    curr.val %= 10
    if carry and not curr.next:
        curr.next = ListNode(carry)
        carry = 0
    curr = curr.next

# Reverse back
prev = None
curr = prev
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
```

### 13. Add Two Numbers as Linked Lists
```python
# Core algorithm: Process both lists with carry
dummy = ListNode(0)
curr = dummy
carry = 0

while l1 or l2 or carry:
    sum_val = carry

    if l1:
        sum_val += l1.val
        l1 = l1.next

    if l2:
        sum_val += l2.val
        l2 = l2.next

    carry = sum_val // 10
    curr.next = ListNode(sum_val % 10)
    curr = curr.next

return dummy.next
```

### 14. Delete All Occurrences in DLL
```python
# Core algorithm: Update prev and next pointers
curr = head

while curr:
    if curr.data == key:
        # Handle head deletion
        if curr == head:
            head = curr.next
            if head:
                head.prev = None
        else:
            curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev

    curr = curr.next

return head
```

### 15. Find Pairs with Given Sum in DLL
```python
# Core algorithm: Two pointers from both ends
left = head
right = tail  # Assuming tail is given

pairs = []
while left and right and left != right and left.prev != right:
    sum_val = left.data + right.data

    if sum_val == target:
        pairs.append((left.data, right.data))
        left = left.next
        right = right.prev
    elif sum_val < target:
        left = left.next
    else:
        right = right.prev

return pairs
```

## Recursion

### 1. Pow(x, n)
```python
# Core algorithm: Fast exponentiation
def myPow(x, n):
    if n == 0:
        return 1
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

### 2. Count Good Numbers
```python
# Core algorithm: Fast exponentiation with modulo
MOD = 10**9 + 7

def count_good_numbers(n):
    even_positions = (n + 1) // 2  # 0, 2, 4, ... (5 choices each)
    odd_positions = n // 2         # 1, 3, 5, ... (4 choices each)

    return (pow(5, even_positions, MOD) * pow(4, odd_positions, MOD)) % MOD
```

### 3. Sort Stack using Recursion
```python
# Core algorithm: Remove top, sort rest, insert in position
def sort_stack(stack):
    if not stack:
        return

    top = stack.pop()
    sort_stack(stack)
    insert_in_sorted_position(stack, top)

def insert_in_sorted_position(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
        return

    top = stack.pop()
    insert_in_sorted_position(stack, element)
    stack.append(top)
```

### 4. Reverse Stack using Recursion
```python
# Core algorithm: Remove top, reverse rest, insert at bottom
def reverse_stack(stack):
    if not stack:
        return

    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, element):
    if not stack:
        stack.append(element)
        return

    top = stack.pop()
    insert_at_bottom(stack, element)
    stack.append(top)
```

### 5. Generate All Binary Strings
```python
# Core algorithm: Include/exclude pattern
def generate_binary(n, current="", result=[]):
    if len(current) == n:
        result.append(current)
        return

    # Try '0'
    generate_binary(n, current + '0', result)
    # Try '1'
    generate_binary(n, current + '1', result)
```

### 6. Generate All Subsequences
```python
# Core algorithm: Include/exclude each element
def generate_subsequences(arr, index, current, result):
    if index == len(arr):
        result.append(current[:])
        return

    # Include current element
    current.append(arr[index])
    generate_subsequences(arr, index + 1, current, result)
    current.pop()

    # Exclude current element
    generate_subsequences(arr, index + 1, current, result)
```

### 7. Count Subsequences with Sum K
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

### 8. Check Subsequence with Sum K
```python
# Core algorithm: Include/exclude with early termination
def has_subsequence_sum(arr, index, current_sum, target):
    if current_sum == target:
        return True
    if index >= len(arr):
        return False

    # Include current element
    if has_subsequence_sum(arr, index + 1, current_sum + arr[index], target):
        return True

    # Exclude current element
    return has_subsequence_sum(arr, index + 1, current_sum, target)
```

### 9. Combination Sum
```python
# Core algorithm: Unlimited use of elements
def combination_sum(candidates, index, target, current, result):
    if target == 0:
        result.append(current[:])
        return
    if index >= len(candidates) or target < 0:
        return

    # Include current element (can use unlimited times)
    current.append(candidates[index])
    combination_sum(candidates, index, target - candidates[index], current, result)
    current.pop()

    # Move to next element
    combination_sum(candidates, index + 1, target, current, result)
```

### 10. Combination Sum II
```python
# Core algorithm: Skip duplicates at same level
def combination_sum_ii(candidates, index, target, current, result):
    if target == 0:
        result.append(current[:])
        return

    for i in range(index, len(candidates)):
        # Skip duplicates at same recursion level
        if i > index and candidates[i] == candidates[i-1]:
            continue

        if candidates[i] > target:
            break

        current.append(candidates[i])
        combination_sum_ii(candidates, i + 1, target - candidates[i], current, result)
        current.pop()
```

### 11. Subset Sum
```python
# Core algorithm: Generate all possible subset sums
def subset_sums(arr, index, current_sum, result):
    if index == len(arr):
        result.append(current_sum)
        return

    # Include current element
    subset_sums(arr, index + 1, current_sum + arr[index], result)
    # Exclude current element
    subset_sums(arr, index + 1, current_sum, result)
```

### 12. Subsets II
```python
# Core algorithm: Skip duplicates to avoid duplicate subsets
def subsets_with_dup(nums, index, current, result):
    result.append(current[:])

    for i in range(index, len(nums)):
        # Skip duplicates at same level
        if i > index and nums[i] == nums[i-1]:
            continue

        current.append(nums[i])
        subsets_with_dup(nums, i + 1, current, result)
        current.pop()
```

### 13. Subsets III
```python
# Core algorithm: Standard backtracking for unique subsets
def subsets(nums, index, current, result):
    if index == len(nums):
        result.append(current[:])
        return

    # Include current element
    current.append(nums[index])
    subsets(nums, index + 1, current, result)
    current.pop()

    # Exclude current element
    subsets(nums, index + 1, current, result)
```

### 14. Letter Combinations
```python
# Core algorithm: Map digits to letters, try all combinations
phone_map = {
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}

def letter_combinations(digits, index, current, result):
    if index == len(digits):
        result.append(current)
        return

    for char in phone_map[digits[index]]:
        letter_combinations(digits, index + 1, current + char, result)
```

### 15. Palindrome Partitioning
```python
# Core algorithm: Try all partitions, check palindrome
def palindrome_partition(s, index, current, result):
    if index == len(s):
        result.append(current[:])
        return

    for i in range(index, len(s)):
        substring = s[index:i+1]
        if is_palindrome(substring):
            current.append(substring)
            palindrome_partition(s, i + 1, current, result)
            current.pop()

def is_palindrome(s):
    return s == s[::-1]
```

### 16. Word Search
```python
# Core algorithm: DFS with backtracking
def word_search(board, word, row, col, index, visited):
    if index == len(word):
        return True

    if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or
        visited[row][col] or board[row][col] != word[index]):
        return False

    visited[row][col] = True

    # Try 4 directions
    found = (word_search(board, word, row+1, col, index+1, visited) or
             word_search(board, word, row-1, col, index+1, visited) or
             word_search(board, word, row, col+1, index+1, visited) or
             word_search(board, word, row, col-1, index+1, visited))

    visited[row][col] = False  # Backtrack
    return found
```

### 17. Rat in a Maze
```python
# Core algorithm: Try 4 directions (DLRU), backtrack
def solve_maze(maze, row, col, dest_row, dest_col, path, visited):
    if row == dest_row and col == dest_col:
        return True

    # Try Down, Left, Right, Up
    directions = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]

    for dr, dc, direction in directions:
        new_row, new_col = row + dr, col + dc

        if (0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and
            maze[new_row][new_col] == 1 and not visited[new_row][new_col]):

            visited[new_row][new_col] = True
            path.append(direction)

            if solve_maze(maze, new_row, new_col, dest_row, dest_col, path, visited):
                return True

            # Backtrack
            path.pop()
            visited[new_row][new_col] = False

    return False
```

## Greedy Algorithms

### 1. Assign Cookies
```python
# Core algorithm: Sort both, assign smallest cookie to smallest appetite
g.sort()  # Children's appetites
s.sort()  # Cookie sizes

child = cookie = 0
while child < len(g) and cookie < len(s):
    if s[cookie] >= g[child]:
        child += 1
    cookie += 1

return child
```

### 2. Fractional Knapsack
```python
# Core algorithm: Sort by value/weight ratio
items = [(value[i]/weight[i], value[i], weight[i]) for i in range(len(value))]
items.sort(reverse=True)

total_value = 0
for ratio, val, wt in items:
    if capacity >= wt:
        total_value += val
        capacity -= wt
    else:
        total_value += val * (capacity / wt)
        break

return total_value
```

### 3. Find Min Number of Coins
```python
# Core algorithm: Use largest denominations first
denominations = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
count = 0

for coin in denominations:
    if amount >= coin:
        count += amount // coin
        amount %= coin

return count
```

### 4. Lemonade Change
```python
# Core algorithm: Greedily use larger bills for change
five_count = ten_count = 0

for bill in bills:
    if bill == 5:
        five_count += 1
    elif bill == 10:
        if five_count > 0:
            five_count -= 1
            ten_count += 1
        else:
            return False
    else:  # bill == 20
        if ten_count > 0 and five_count > 0:
            ten_count -= 1
            five_count -= 1
        elif five_count >= 3:
            five_count -= 3
        else:
            return False

return True
```

### 5. Valid Parenthesis Checker
```python
# Core algorithm: Counter balance, never go negative
balance = 0

for char in s:
    if char == '(':
        balance += 1
    else:  # char == ')'
        balance -= 1
        if balance < 0:
            return False

return balance == 0
```

### 6. N Meetings in One Room
```python
# Core algorithm: Sort by end time, greedily pick
meetings = [(start[i], end[i], i+1) for i in range(len(start))]
meetings.sort(key=lambda x: x[1])  # Sort by end time

selected = [meetings[0]]
last_end = meetings[0][1]

for i in range(1, len(meetings)):
    if meetings[i][0] > last_end:  # No overlap
        selected.append(meetings[i])
        last_end = meetings[i][1]

return len(selected)
```

### 7. Jump Game
```python
# Core algorithm: Track farthest reachable
farthest = 0
for i in range(len(nums)):
    if i > farthest:
        return False
    farthest = max(farthest, i + nums[i])
return True
```

### 8. Jump Game II
```python
# Core algorithm: BFS-like approach, count jumps
jumps = 0
current_end = 0
farthest = 0

for i in range(len(nums) - 1):
    farthest = max(farthest, i + nums[i])

    if i == current_end:
        jumps += 1
        current_end = farthest

return jumps
```

### 9. Min Platforms for Railway
```python
# Core algorithm: Sort arrivals and departures separately
arrivals.sort()
departures.sort()

platforms_needed = 1
max_platforms = 1
i = j = 1

while i < len(arrivals) and j < len(departures):
    if arrivals[i] <= departures[j]:
        platforms_needed += 1
        i += 1
    else:
        platforms_needed -= 1
        j += 1

    max_platforms = max(max_platforms, platforms_needed)

return max_platforms
```

### 10. Job Sequencing Problem
```python
# Core algorithm: Sort by profit, place at latest slot
jobs.sort(key=lambda x: x[1], reverse=True)  # Sort by profit
max_deadline = max(job[0] for job in jobs)
slots = [False] * (max_deadline + 1)

count = total_profit = 0
for deadline, profit in jobs:
    # Find latest available slot
    for j in range(min(max_deadline, deadline), 0, -1):
        if not slots[j]:
            slots[j] = True
            count += 1
            total_profit += profit
            break

return count, total_profit
```

### 11. Candy Distribution
```python
# Core algorithm: Two passes (left-to-right, right-to-left)
n = len(ratings)
candies = [1] * n

# Left to right pass
for i in range(1, n):
    if ratings[i] > ratings[i-1]:
        candies[i] = candies[i-1] + 1

# Right to left pass
for i in range(n-2, -1, -1):
    if ratings[i] > ratings[i+1]:
        candies[i] = max(candies[i], candies[i+1] + 1)

return sum(candies)
```

### 12. Insert Interval
```python
# Core algorithm: Three phases - before, merge, after
result = []
i = 0

# Add all intervals ending before new interval starts
while i < len(intervals) and intervals[i][1] < newInterval[0]:
    result.append(intervals[i])
    i += 1

# Merge all overlapping intervals
while i < len(intervals) and intervals[i][0] <= newInterval[1]:
    newInterval[0] = min(newInterval[0], intervals[i][0])
    newInterval[1] = max(newInterval[1], intervals[i][1])
    i += 1

result.append(newInterval)

# Add remaining intervals
while i < len(intervals):
    result.append(intervals[i])
    i += 1

return result
```

### 13. Merge Intervals
```python
# Core algorithm: Sort by start time, merge overlapping
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]

for current in intervals[1:]:
    if current[0] <= merged[-1][1]:  # Overlap
        merged[-1][1] = max(merged[-1][1], current[1])
    else:
        merged.append(current)

return merged
```

### 14. Non-overlapping Intervals
```python
# Core algorithm: Sort by end time, count overlaps
intervals.sort(key=lambda x: x[1])
count = 0
last_end = intervals[0][1]

for i in range(1, len(intervals)):
    if intervals[i][0] < last_end:  # Overlap
        count += 1
    else:
        last_end = intervals[i][1]

return count
```

## Binary Trees

### 1. Preorder Traversal
```python
# Core algorithm: Root -> Left -> Right
def preorder(root, result):
    if not root:
        return

    result.append(root.val)  # Process root
    preorder(root.left, result)      # Traverse left
    preorder(root.right, result)     # Traverse right
```

### 2. Inorder Traversal
```python
# Core algorithm: Left -> Root -> Right
def inorder(root, result):
    if not root:
        return

    inorder(root.left, result)       # Traverse left
    result.append(root.val)  # Process root
    inorder(root.right, result)      # Traverse right
```

### 3. Postorder Traversal
```python
# Core algorithm: Left -> Right -> Root
def postorder(root, result):
    if not root:
        return

    postorder(root.left, result)     # Traverse left
    postorder(root.right, result)    # Traverse right
    result.append(root.val)  # Process root
```

## Stack & Queue

### 1. Implement Stack using Arrays
```python
# Core algorithm: Array-based stack with capacity
class Stack:
    def __init__(self, capacity):
        self.arr = []
        self.max_length = capacity

    def push(self, num):
        if len(self.arr) < self.max_length:
            self.arr.append(num)

    def pop(self):
        return self.arr.pop() if self.arr else -1

    def top(self):
        return self.arr[-1] if self.arr else -1

    def isEmpty(self):
        return 1 if len(self.arr) == 0 else 0

    def isFull(self):
        return 1 if len(self.arr) == self.max_length else 0
```

### 2. Implement Queue using Array
```python
# Core algorithm: Circular array with front and rear pointers
class Queue:
    def __init__(self, capacity):
        self.arr = [0] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = capacity

    def enqueue(self, item):
        if self.size == self.capacity:
            return False
        self.arr[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self):
        if self.size == 0:
            return -1
        item = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
```

### 3. Implement Stack using Queue
```python
# Core algorithm: Use two queues to simulate LIFO
from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        # Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap queues
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft() if self.q1 else None

    def top(self):
        return self.q1[0] if self.q1 else None

    def empty(self):
        return len(self.q1) == 0
```

### 4. Implement Queue using Stacks
```python
# Core algorithm: Use two stacks for FIFO
class MyQueue:
    def __init__(self):
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        self._transfer()
        return self.stack2.pop() if self.stack2 else None

    def peek(self):
        self._transfer()
        return self.stack2[-1] if self.stack2 else None

    def empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def _transfer(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
```

### 5. Valid Parentheses
```python
# Core algorithm: Stack to match opening and closing brackets
def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)

    return len(stack) == 0
```

### 6. Next Greater Element
```python
# Core algorithm: Monotonic stack (decreasing order)
from collections import deque

def nextGreaterElements(nums):
    stack = deque()
    result = [-1] * len(nums)

    # Traverse from right to left
    for i in range(len(nums) - 1, -1, -1):
        # Remove smaller elements from stack
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        # If stack not empty, top is next greater
        if stack:
            result[i] = stack[-1]

        stack.append(nums[i])

    return result
```

### 7. Sort a Stack
```python
# Core algorithm: Recursion to sort and insert in position
def sortStack(stack):
    if not stack:
        return

    top = stack.pop()
    sortStack(stack)
    insertInSortedOrder(stack, top)

def insertInSortedOrder(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
        return

    top = stack.pop()
    insertInSortedOrder(stack, element)
    stack.append(top)
```

## Advanced Stack & Queue

### 1. Next Smaller Element
```python
# Core algorithm: Monotonic stack (increasing order)
def nextSmallerElement(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result
```

### 2. LRU Cache
```python
# Core algorithm: HashMap + Doubly Linked List
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        # Dummy head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            new_node = Node(key, value)
            if len(self.cache) >= self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
            self.cache[key] = new_node
            self._add_to_head(new_node)

    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)

    def _pop_tail(self):
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node
```

### 3. Largest Rectangle in Histogram
```python
# Core algorithm: Stack to find next/previous smaller elements
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel value

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area
```

### 4. Sliding Window Maximum
```python
# Core algorithm: Deque to maintain decreasing order
from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()  # Store indices
    result = []

    for i in range(len(nums)):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements from back
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        # Add to result if window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

### 5. Min Stack
```python
# Core algorithm: Auxiliary stack to track minimum
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if self.min_stack and val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None
```

### 6. Stock Span Problem
```python
# Core algorithm: Monotonic stack to find previous greater
def calculateSpan(prices):
    stack = []  # Store indices
    spans = []

    for i, price in enumerate(prices):
        # Remove smaller prices from stack
        while stack and prices[stack[-1]] <= price:
            stack.pop()

        # Calculate span
        span = i + 1 if not stack else i - stack[-1]
        spans.append(span)
        stack.append(i)

    return spans
```

## Binary Tree Advanced

### 1. All Tree Traversals in One
```python
# Core algorithm: Single function for all three traversals
def allTraversals(root):
    preorder, inorder, postorder = [], [], []

    def traverse(node):
        if not node:
            return

        preorder.append(node.val)  # Root first
        traverse(node.left)        # Left
        inorder.append(node.val)   # Root middle
        traverse(node.right)       # Right
        postorder.append(node.val) # Root last

    traverse(root)
    return preorder, inorder, postorder
```

### 2. Root to Node Path
```python
# Core algorithm: DFS with path tracking
def findPath(root, target):
    def dfs(node, path):
        if not node:
            return False

        path.append(node.val)

        if node.val == target:
            return True

        if dfs(node.left, path) or dfs(node.right, path):
            return True

        path.pop()  # Backtrack
        return False

    path = []
    dfs(root, path)
    return path
```

### 3. Left View Binary Tree
```python
# Core algorithm: Level-order traversal, first node of each level
def leftView(root):
    if not root:
        return []

    result = []

    def dfs(node, level):
        if not node:
            return

        # First node at this level
        if level == len(result):
            result.append(node.val)

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return result
```

### 4. Bottom View Binary Tree
```python
# Core algorithm: Level-order with horizontal distance tracking
from collections import deque, defaultdict

def bottomView(root):
    if not root:
        return []

    queue = deque([(root, 0)])  # (node, horizontal_distance)
    hd_map = defaultdict(int)

    while queue:
        node, hd = queue.popleft()
        hd_map[hd] = node.val  # Overwrite for bottom view

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    return [hd_map[hd] for hd in sorted(hd_map.keys())]
```

### 5. Top View Binary Tree
```python
# Core algorithm: Level-order, first occurrence at each horizontal distance
from collections import deque

def topView(root):
    if not root:
        return []

    queue = deque([(root, 0)])
    hd_map = {}

    while queue:
        node, hd = queue.popleft()

        # Only first occurrence for top view
        if hd not in hd_map:
            hd_map[hd] = node.val

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    return [hd_map[hd] for hd in sorted(hd_map.keys())]
```

### 6. Vertical Order Traversal
```python
# Core algorithm: Sort by (column, row, value)
from collections import defaultdict

def verticalTraversal(root):
    nodes = []

    def dfs(node, row, col):
        if not node:
            return
        nodes.append((col, row, node.val))
        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)
    nodes.sort()  # Sort by col, then row, then val

    result = []
    columns = defaultdict(list)
    for col, row, val in nodes:
        columns[col].append(val)

    for col in sorted(columns.keys()):
        result.append(columns[col])

    return result
```

### 7. Maximum Width Binary Tree
```python
# Core algorithm: Level-order with position indexing
from collections import deque

def widthOfBinaryTree(root):
    if not root:
        return 0

    queue = deque([(root, 0)])
    max_width = 0

    while queue:
        level_size = len(queue)
        start_pos = queue[0][1]

        for _ in range(level_size):
            node, pos = queue.popleft()

            if node.left:
                queue.append((node.left, 2 * pos))
            if node.right:
                queue.append((node.right, 2 * pos + 1))

        # Width is difference between first and last position + 1
        end_pos = pos
        max_width = max(max_width, end_pos - start_pos + 1)

    return max_width
```

## Heaps

### 1. Implement Min Heap
```python
# Core algorithm: Array representation with heapify operations
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._heapify_up(parent)

    def _heapify_down(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)
```

## Trie

### 1. Implement Trie
```python
# Core algorithm: Tree of characters with end-of-word flags
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def contains(self, ch):
        return self.children[ord(ch) - ord('a')] is not None

    def get(self, ch):
        return self.children[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.children[ord(ch) - ord('a')] = node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.contains(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if not node.contains(ch):
                return False
            node = node.get(ch)
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if not node.contains(ch):
                return False
            node = node.get(ch)
        return True
```

### 2. Implement Trie II
```python
# Core algorithm: Trie with count tracking
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.count_words = 0      # Words ending here
        self.count_prefixes = 0   # Words passing through here

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.children[ord(ch) - ord('a')]:
                node.children[ord(ch) - ord('a')] = TrieNode()
            node = node.children[ord(ch) - ord('a')]
            node.count_prefixes += 1
        node.count_words += 1

    def countWordsEqualTo(self, word):
        node = self.root
        for ch in word:
            if not node.children[ord(ch) - ord('a')]:
                return 0
            node = node.children[ord(ch) - ord('a')]
        return node.count_words

    def countWordsStartingWith(self, prefix):
        node = self.root
        for ch in prefix:
            if not node.children[ord(ch) - ord('a')]:
                return 0
            node = node.children[ord(ch) - ord('a')]
        return node.count_prefixes

    def erase(self, word):
        node = self.root
        for ch in word:
            node = node.children[ord(ch) - ord('a')]
            node.count_prefixes -= 1
        node.count_words -= 1
```

### 3. Longest String with All Prefixes
```python
# Core algorithm: Check if all prefixes exist in trie
def longestStringWithAllPrefixes(words):
    trie = Trie()

    # Insert all words
    for word in words:
        trie.insert(word)

    def hasAllPrefixes(word):
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            if not trie.search(prefix):
                return False
        return True

    longest = ""
    for word in words:
        if hasAllPrefixes(word):
            if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                longest = word

    return longest
```

### 4. Complete String
```python
# Core algorithm: String is complete if all prefixes exist as words
def completeString(words):
    trie = Trie()

    for word in words:
        trie.insert(word)

    def isComplete(word):
        for i in range(1, len(word) + 1):
            if not trie.search(word[:i]):
                return False
        return True

    result = ""
    for word in words:
        if isComplete(word):
            if len(word) > len(result) or (len(word) == len(result) and word < result):
                result = word

    return result if result else "None"
```

### 5. Number of Distinct Substrings
```python
# Core algorithm: Insert all suffixes into trie, count nodes
def countDistinctSubstrings(s):
    trie = Trie()

    # Insert all suffixes
    for i in range(len(s)):
        trie.insert(s[i:])

    def countNodes(node):
        if not node:
            return 0

        count = 1  # Count current node
        for child in node.children:
            if child:
                count += countNodes(child)

        return count

    # Subtract 1 for root node
    return countNodes(trie.root) - 1
```

### 6. Max XOR of Two Numbers
```python
# Core algorithm: Binary trie for bit manipulation
class TrieNode:
    def __init__(self):
        self.children = [None, None]  # 0 and 1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):  # 32-bit numbers
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def getMaxXor(self, num):
        node = self.root
        max_xor = 0

        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # Try to go opposite direction for max XOR
            opposite_bit = 1 - bit

            if node.children[opposite_bit]:
                max_xor |= (1 << i)
                node = node.children[opposite_bit]
            else:
                node = node.children[bit]

        return max_xor

def findMaximumXOR(nums):
    trie = Trie()

    for num in nums:
        trie.insert(num)

    max_xor = 0
    for num in nums:
        max_xor = max(max_xor, trie.getMaxXor(num))

    return max_xor
```

### 7. Max XOR with Element from Array
```python
# Core algorithm: Offline queries with sorting by limit
def maximizeXor(nums, queries):
    # Sort nums and add indices to queries
    nums.sort()
    indexed_queries = [(queries[i][0], queries[i][1], i) for i in range(len(queries))]
    indexed_queries.sort(key=lambda x: x[1])  # Sort by limit

    trie = Trie()
    result = [-1] * len(queries)
    num_idx = 0

    for x, limit, query_idx in indexed_queries:
        # Add all numbers <= limit to trie
        while num_idx < len(nums) and nums[num_idx] <= limit:
            trie.insert(nums[num_idx])
            num_idx += 1

        # Find max XOR with x
        if num_idx > 0:  # Trie is not empty
            result[query_idx] = trie.getMaxXor(x)

    return result
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

### 2. Min Value in BST
```python
# Core algorithm: Keep going left
def find_min(root):
    while root.left:
        root = root.left
    return root.val
```

### 3. Ceil in BST
```python
# Core algorithm: Track smallest value >= target
def ceil(root, key):
    ceil_val = -1

    while root:
        if root.val == key:
            return root.val
        elif root.val > key:
            ceil_val = root.val
            root = root.left
        else:
            root = root.right

    return ceil_val
```

### 4. Insert Node in BST
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

### 5. Delete Node in BST
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

### 6. Kth Smallest Element
```python
# Core algorithm: Inorder traversal gives sorted order
def kthSmallest(root, k):
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    sorted_vals = inorder(root)
    return sorted_vals[k-1]
```

### 7. Validate BST
```python
# Core algorithm: Each node must be within (min, max) range
def isValidBST(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True

    if root.val <= min_val or root.val >= max_val:
        return False

    return (isValidBST(root.left, min_val, root.val) and
            isValidBST(root.right, root.val, max_val))
```

### 8. LCA in BST
```python
# Core algorithm: First node where paths to p and q split
def lowestCommonAncestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root  # Found split point
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

### 3. Connected Components
```python
# Core algorithm: DFS/BFS from each unvisited node
def count_components(graph, n):
    visited = set()
    count = 0

    for i in range(n):
        if i not in visited:
            dfs(graph, i, visited, [])
            count += 1

    return count
```

### 4. Number of Provinces
```python
# Core algorithm: Count connected components in adjacency matrix
def findCircleNum(isConnected):
    visited = [False] * len(isConnected)
    provinces = 0

    for i in range(len(isConnected)):
        if not visited[i]:
            dfs_provinces(isConnected, i, visited)
            provinces += 1

    return provinces

def dfs_provinces(adj_matrix, node, visited):
    visited[node] = True
    for neighbor in range(len(adj_matrix)):
        if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
            dfs_provinces(adj_matrix, neighbor, visited)
```

### 5. Rotten Oranges
```python
# Core algorithm: Multi-source BFS with time tracking
from collections import deque

def orangesRotting(grid):
    queue = deque()
    fresh_count = 0

    # Add all rotten oranges to queue
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                queue.append((i, j, 0))  # (row, col, time)
            elif grid[i][j] == 1:
                fresh_count += 1

    max_time = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        row, col, time = queue.popleft()
        max_time = max(max_time, time)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and
                grid[new_row][new_col] == 1):

                grid[new_row][new_col] = 2
                fresh_count -= 1
                queue.append((new_row, new_col, time + 1))

    return max_time if fresh_count == 0 else -1
```

### 6. Flood Fill
```python
# Core algorithm: DFS/BFS to change connected pixels
def floodFill(image, sr, sc, color):
    original_color = image[sr][sc]
    if original_color == color:
        return image

    def dfs(row, col):
        if (row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or
            image[row][col] != original_color):
            return

        image[row][col] = color

        # Fill 4 directions
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    dfs(sr, sc)
    return image
```

### 7. Cycle Detection (Undirected BFS)
```python
# Core algorithm: If adjacent node is visited and not parent, cycle found
from collections import deque

def has_cycle_bfs(graph, n):
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            if bfs_cycle_check(graph, i, visited):
                return True
    return False

def bfs_cycle_check(graph, start, visited):
    queue = deque([(start, -1)])  # (node, parent)
    visited[start] = True

    while queue:
        node, parent = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, node))
            elif neighbor != parent:
                return True  # Cycle found

    return False
```

### 8. Cycle Detection (Undirected DFS)
```python
# Core algorithm: DFS with parent tracking
def has_cycle_dfs(graph, node, parent, visited):
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if has_cycle_dfs(graph, neighbor, node, visited):
                return True
        elif neighbor != parent:
            return True  # Back edge found (cycle)

    return False
```

### 9. 0-1 Matrix
```python
# Core algorithm: Multi-source BFS from all 0s
from collections import deque

def updateMatrix(mat):
    queue = deque()

    # Add all 0s to queue and mark 1s as unvisited
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                queue.append((i, j))
            else:
                mat[i][j] = float('inf')

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < len(mat) and 0 <= new_col < len(mat[0]) and
                mat[new_row][new_col] > mat[row][col] + 1):

                mat[new_row][new_col] = mat[row][col] + 1
                queue.append((new_row, new_col))

    return mat
```

### 10. Surrounded Regions
```python
# Core algorithm: Mark boundary-connected 'O's as safe
def solve(board):
    if not board:
        return

    def dfs(row, col):
        if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or
            board[row][col] != 'O'):
            return

        board[row][col] = 'S'  # Mark as safe

        # DFS in 4 directions
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    # Mark boundary-connected 'O's as safe
    for i in range(len(board)):
        dfs(i, 0)  # Left boundary
        dfs(i, len(board[0]) - 1)  # Right boundary

    for j in range(len(board[0])):
        dfs(0, j)  # Top boundary
        dfs(len(board) - 1, j)  # Bottom boundary

    # Convert: 'O' -> 'X', 'S' -> 'O'
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'S':
                board[i][j] = 'O'
```

### 11. Number of Enclaves
```python
# Core algorithm: Count land cells not reachable from boundary
def numEnclaves(grid):
    def dfs(row, col):
        if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or
            grid[row][col] == 0):
            return

        grid[row][col] = 0  # Mark as water

        # DFS in 4 directions
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    # Remove boundary-connected land
    for i in range(len(grid)):
        dfs(i, 0)  # Left boundary
        dfs(i, len(grid[0]) - 1)  # Right boundary

    for j in range(len(grid[0])):
        dfs(0, j)  # Top boundary
        dfs(len(grid) - 1, j)  # Bottom boundary

    # Count remaining land
    return sum(sum(row) for row in grid)
```

### 12. Word Ladder I
```python
# Core algorithm: BFS level-wise transformation
from collections import deque

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    word_set = set(wordList)
    queue = deque([(beginWord, 1)])  # (word, level)
    visited = {beginWord}

    while queue:
        word, level = queue.popleft()

        if word == endWord:
            return level

        # Try changing each character
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]

                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, level + 1))

    return 0
```

### 13. Bipartite Graph
```python
# Core algorithm: 2-coloring using DFS/BFS
def isBipartite(graph):
    color = {}

    def dfs(node, c):
        color[node] = c

        for neighbor in graph[node]:
            if neighbor in color:
                if color[neighbor] == c:
                    return False
            else:
                if not dfs(neighbor, 1 - c):
                    return False

        return True

    for i in range(len(graph)):
        if i not in color:
            if not dfs(i, 0):
                return False

    return True
```

### 14. Topological Sort (DFS)
```python
# Core algorithm: Add to result when DFS completes (finish time)
def topological_sort_dfs(graph, n):
    visited = [False] * n
    stack = []

    def dfs(node):
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

        stack.append(node)  # Add when finishing

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return stack[::-1]  # Reverse for correct order
```

### 15. Topological Sort (BFS - Kahn's)
```python
# Core algorithm: Start with 0 indegree nodes
from collections import deque

def topological_sort_bfs(graph, n):
    indegree = [0] * n

    # Calculate indegree
    for i in range(n):
        for neighbor in graph[i]:
            indegree[neighbor] += 1

    # Start with 0 indegree nodes
    queue = deque([i for i in range(n) if indegree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == n else []  # Check for cycle
```

### 16. Cycle Detection (Directed DFS)
```python
# Core algorithm: Use 3 colors (white, gray, black)
def has_cycle_directed(graph, n):
    # 0: white (unvisited), 1: gray (visiting), 2: black (visited)
    color = [0] * n

    def dfs(node):
        if color[node] == 1:  # Gray - back edge found
            return True
        if color[node] == 2:  # Black - already processed
            return False

        color[node] = 1  # Mark as gray

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        color[node] = 2  # Mark as black
        return False

    for i in range(n):
        if color[i] == 0 and dfs(i):
            return True

    return False
```

### 17. Course Schedule II
```python
# Core algorithm: Topological sort with cycle detection
def findOrder(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for dependent in graph[course]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                queue.append(dependent)

    return order if len(order) == numCourses else []
```

### 18. Find Eventual Safe States
```python
# Core algorithm: Safe nodes have no outgoing edges to cycles
def eventualSafeNodes(graph):
    n = len(graph)
    color = [0] * n  # 0: white, 1: gray, 2: black

    def dfs(node):
        if color[node] != 0:
            return color[node] == 2

        color[node] = 1  # Mark as gray

        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False

        color[node] = 2  # Mark as black (safe)
        return True

    return [i for i in range(n) if dfs(i)]
```

### 19. Shortest Path (Unweighted)
```python
# Core algorithm: BFS gives shortest path in unweighted graphs
from collections import deque

def shortest_path_unweighted(graph, start, end):
    queue = deque([(start, 0)])  # (node, distance)
    visited = {start}

    while queue:
        node, dist = queue.popleft()

        if node == end:
            return dist

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1  # No path found
```

### 20. Shortest Path in DAG
```python
# Core algorithm: Topological sort + relaxation
def shortest_path_dag(graph, start, n):
    # Topological sort
    topo_order = topological_sort_dfs(graph, n)

    dist = [float('inf')] * n
    dist[start] = 0

    # Relax edges in topological order
    for u in topo_order:
        if dist[u] != float('inf'):
            for v, weight in graph[u]:
                dist[v] = min(dist[v], dist[u] + weight)

    return dist
```

### 21. Dijkstra's Algorithm
```python
# Core algorithm: Greedy shortest path using priority queue
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)

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

### 22. Shortest Path in Binary Maze
```python
# Core algorithm: BFS for shortest path in 0/1 maze
from collections import deque

def shortest_path_binary_maze(grid, start, end):
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return -1

    queue = deque([(start[0], start[1], 0)])  # (row, col, dist)
    visited = set([start])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        row, col, dist = queue.popleft()

        if (row, col) == end:
            return dist

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and
                grid[new_row][new_col] == 0 and (new_row, new_col) not in visited):

                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))

    return -1
```

### 23. Path with Minimum Effort
```python
# Core algorithm: Binary search on answer + DFS feasibility check
def minimumEffortPath(heights):
    def can_reach(max_effort):
        visited = set()

        def dfs(row, col):
            if (row, col) == (len(heights)-1, len(heights[0])-1):
                return True

            visited.add((row, col))

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + dr, col + dc

                if (0 <= new_row < len(heights) and 0 <= new_col < len(heights[0]) and
                    (new_row, new_col) not in visited):

                    effort = abs(heights[new_row][new_col] - heights[row][col])
                    if effort <= max_effort and dfs(new_row, new_col):
                        return True

            return False

        return dfs(0, 0)

    left, right = 0, max(max(row) for row in heights)

    while left < right:
        mid = (left + right) // 2
        if can_reach(mid):
            right = mid
        else:
            left = mid + 1

    return left
```

### 24. Cheapest Flights K Stops
```python
# Core algorithm: Modified Dijkstra with state (cost, node, stops)
import heapq

def findCheapestPrice(n, flights, src, dst, k):
    graph = [[] for _ in range(n)]
    for u, v, price in flights:
        graph[u].append((v, price))

    pq = [(0, src, 0)]  # (cost, node, stops)
    visited = {}

    while pq:
        cost, node, stops = heapq.heappop(pq)

        if node == dst:
            return cost

        if stops > k:
            continue

        if node in visited and visited[node] <= stops:
            continue

        visited[node] = stops

        for neighbor, price in graph[node]:
            heapq.heappush(pq, (cost + price, neighbor, stops + 1))

    return -1
```

### 25. Network Delay Time
```python
# Core algorithm: Dijkstra to find max time to reach all nodes
import heapq

def networkDelayTime(times, n, k):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in times:
        graph[u].append((v, w))

    dist = [float('inf')] * (n + 1)
    dist[k] = 0
    pq = [(0, k)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    max_time = max(dist[1:])
    return max_time if max_time != float('inf') else -1
```

### 26. Bellman-Ford Algorithm
```python
# Core algorithm: Relax all edges V-1 times, detect negative cycles
def bellman_ford(edges, n, src):
    dist = [float('inf')] * n
    dist[src] = 0

    # Relax all edges V-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None  # Negative cycle detected

    return dist
```

### 27. Floyd-Warshall Algorithm
```python
# Core algorithm: Try all intermediate vertices k for paths i->j
def floyd_warshall(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]

    # Initialize distances
    for i in range(n):
        dist[i][i] = 0

    for u, v, w in graph:
        dist[u][v] = w

    # Try all intermediate vertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
```

### 28. Find City with Smallest Threshold
```python
# Core algorithm: Floyd-Warshall + count reachable cities
def findTheCity(n, edges, distanceThreshold):
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = dist[v][u] = w

    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Find city with minimum reachable cities
    min_reachable = float('inf')
    result_city = -1

    for i in range(n):
        reachable = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
        if reachable <= min_reachable:
            min_reachable = reachable
            result_city = i

    return result_city
```

### 29. Prim's Algorithm
```python
# Core algorithm: Grow MST by adding minimum weight edge
import heapq

def prim_mst(graph, n):
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, node)
    mst_weight = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        mst_weight += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    return mst_weight
```

### 30. Kruskal's Algorithm
```python
# Core algorithm: Sort edges, use Union-Find to avoid cycles
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def kruskal_mst(edges, n):
    edges.sort()  # Sort by weight
    uf = UnionFind(n)
    mst_weight = 0
    edges_used = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst_weight += weight
            edges_used += 1
            if edges_used == n - 1:
                break

    return mst_weight
```

### 31. Number of Operations to Connect
```python
# Core algorithm: Count components, need (components-1) operations
def makeConnected(n, connections):
    if len(connections) < n - 1:
        return -1  # Not enough cables

    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False

    components = n
    for u, v in connections:
        if union(u, v):
            components -= 1

    return components - 1
```

### 32. Most Stones Removed
```python
# Core algorithm: Stones in same row/col are connected
def removeStones(stones):
    parent = {}

    def find(x):
        if x not in parent:
            parent[x] = x
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py

    for x, y in stones:
        union(x, ~y)  # Use ~y to distinguish row and column indices

    return len(stones) - len({find(x) for x, y in stones})
```

### 33. Number of Islands II
```python
# Core algorithm: Dynamic connectivity with Union-Find
def numIslandsII(m, n, positions):
    parent = {}
    rank = {}
    count = 0
    result = []

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        nonlocal count
        px, py = find(x), find(y)
        if px != py:
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            count -= 1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for r, c in positions:
        if (r, c) in parent:
            result.append(count)
            continue

        parent[(r, c)] = (r, c)
        rank[(r, c)] = 0
        count += 1

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and (nr, nc) in parent:
                union((r, c), (nr, nc))

        result.append(count)

    return result
```

## Dynamic Programming

### 1. Climbing Stairs
```python
# Core algorithm: Fibonacci pattern
def climbStairs(n):
    if n <= 2:
        return n

    prev2, prev1 = 1, 2

    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1
```

### 2. Frog Jump
```python
# Core algorithm: Min cost to reach each stone
def frog_jump(heights):
    n = len(heights)
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        # Jump 1 step
        dp[i] = min(dp[i], dp[i-1] + abs(heights[i] - heights[i-1]))

        # Jump 2 steps
        if i >= 2:
            dp[i] = min(dp[i], dp[i-2] + abs(heights[i] - heights[i-2]))

    return dp[n-1]
```

### 3. Frog Jump with K Distance
```python
# Core algorithm: Try all possible jumps from 1 to k
def frog_jump_k(heights, k):
    n = len(heights)
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(1, min(i + 1, k + 1)):
            dp[i] = min(dp[i], dp[i-j] + abs(heights[i] - heights[i-j]))

    return dp[n-1]
```

### 4. Maximum Sum Non-Adjacent
```python
# Core algorithm: At each house - rob or not rob
def house_robber(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, curr

    return prev1
```

### 5. House Robber II
```python
# Core algorithm: Run house robber twice for circular array
def rob_circular(nums):
    if len(nums) == 1:
        return nums[0]

    def rob_linear(arr):
        prev2, prev1 = 0, 0
        for num in arr:
            curr = max(prev1, prev2 + num)
            prev2, prev1 = prev1, curr
        return prev1

    # Case 1: Rob houses 0 to n-2 (exclude last)
    # Case 2: Rob houses 1 to n-1 (exclude first)
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
```

### 6. Ninja Training
```python
# Core algorithm: DP with state tracking last activity
def ninja_training(points):
    n = len(points)
    prev = [0] * 4

    # Base case - day 0
    for activity in range(4):
        prev[activity] = max(points[0][j] for j in range(3) if j != activity)

    for day in range(1, n):
        curr = [0] * 4
        for last_activity in range(4):
            for activity in range(3):
                if activity != last_activity:
                    curr[last_activity] = max(curr[last_activity],
                                            prev[activity] + points[day][activity])
        prev = curr

    return prev[3]  # No restriction on last day
```

### 7. Grid Unique Paths
```python
# Core algorithm: Paths from top + paths from left
def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]
```

### 8. Grid Unique Paths II
```python
# Core algorithm: Same as unique paths but handle obstacles
def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    # Base cases
    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            elif i == 0 and j == 0:
                continue
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]

    return dp[m-1][n-1]
```

### 9. Min Path Sum
```python
# Core algorithm: Add current cell + min of top/left
def minPathSum(grid):
    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0:
                grid[i][j] += grid[i-1][j]
            else:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[m-1][n-1]
```

### 10. Subset Sum Equal to Target
```python
# Core algorithm: Include or exclude each element
def subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # Base case - sum 0 is always possible
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # Exclude current element
            dp[i][j] = dp[i-1][j]

            # Include current element if possible
            if nums[i-1] <= j:
                dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]

    return dp[n][target]
```

### 11. Partition Equal Subset Sum
```python
# Core algorithm: Check if subset with sum = total_sum/2 exists
def canPartition(nums):
    total_sum = sum(nums)

    if total_sum % 2 == 1:
        return False

    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]
```

### 12. Partition with Min Difference
```python
# Core algorithm: Find all possible sums, minimize difference
def minimumDifference(nums):
    total_sum = sum(nums)
    n = len(nums)

    # Find all possible subset sums
    dp = [False] * (total_sum + 1)
    dp[0] = True

    for num in nums:
        for j in range(total_sum, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    min_diff = float('inf')
    for i in range(total_sum // 2 + 1):
        if dp[i]:
            diff = abs(total_sum - 2 * i)
            min_diff = min(min_diff, diff)

    return min_diff
```

### 13. 0/1 Knapsack
```python
# Core algorithm: Max value with weight constraint
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't include current item
            dp[i][w] = dp[i-1][w]

            # Include current item if possible
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], values[i-1] + dp[i-1][w - weights[i-1]])

    return dp[n][capacity]
```

### 14. Minimum Coins
```python
# Core algorithm: Try all coins for each amount
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

### 15. Coin Change II
```python
# Core algorithm: Count ways to make amount (process coins in outer loop)
def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]
```

### 16. Longest Common Subsequence
```python
# Core algorithm: Match characters or take max from subproblems
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

### 17. Print All LCS
```python
# Core algorithm: Backtrack from dp table to build all LCS
def print_all_lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Backtrack to find all LCS
    def backtrack(i, j, lcs):
        if i == 0 or j == 0:
            result.add(lcs[::-1])
            return

        if text1[i-1] == text2[j-1]:
            backtrack(i-1, j-1, lcs + text1[i-1])
        else:
            if dp[i-1][j] == dp[i][j]:
                backtrack(i-1, j, lcs)
            if dp[i][j-1] == dp[i][j]:
                backtrack(i, j-1, lcs)

    result = set()
    backtrack(m, n, "")
    return list(result)
```

### 18. Longest Common Substring
```python
# Core algorithm: Track length of common substring ending at each position
def longestCommonSubstring(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0

    return max_length
```

### 19. Longest Palindromic Subsequence
```python
# Core algorithm: LPS(s) = LCS(s, reverse(s))
def longestPalindromeSubseq(s):
    return longestCommonSubsequence(s, s[::-1])
```

### 20. Min Insertions to Make Palindrome
```python
# Core algorithm: Insertions needed = n - LPS(s)
def minInsertions(s):
    n = len(s)
    lps_length = longestPalindromeSubseq(s)
    return n - lps_length
```

### 21. Min Insert/Delete to Convert String
```python
# Core algorithm: Operations = (m - LCS) + (n - LCS)
def minDistance(word1, word2):
    lcs_length = longestCommonSubsequence(word1, word2)
    deletions = len(word1) - lcs_length
    insertions = len(word2) - lcs_length
    return deletions + insertions
```

### 22. Shortest Common Supersequence
```python
# Core algorithm: Build shortest string containing both as subsequences
def shortestCommonSupersequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build LCS DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Build SCS by backtracking
    result = []
    i, j = m, n

    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            result.append(str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            result.append(str1[i-1])
            i -= 1
        else:
            result.append(str2[j-1])
            j -= 1

    # Add remaining characters
    while i > 0:
        result.append(str1[i-1])
        i -= 1

    while j > 0:
        result.append(str2[j-1])
        j -= 1

    return ''.join(reversed(result))
```

---

## SDE Sheet Additional Problems

### Maximum Product Subarray
```python
# Core algorithm: Track both max and min product
def maxProduct(nums):
    max_product = min_product = result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product

        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])

        result = max(result, max_product)

    return result
```

### Reverse Words in String (SDE Alternative)
```python
# Core algorithm: Parse words and reverse order
def reverseWords(s):
    # Split by spaces and filter empty strings
    words = [word for word in s.split(' ') if word]
    return ' '.join(reversed(words))
```

### Find Middle of Linked List (SDE Alternative)
```python
# Core algorithm: Tortoise and Hare
def findMiddle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

### Populate Next Right Pointers
```python
# Core algorithm: Level-order traversal to connect nodes
from collections import deque

def connect(root):
    if not root:
        return root

    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # Connect to next node in same level
            if i < level_size - 1:
                node.next = queue[0]

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return root
```

### Floor in BST
```python
# Core algorithm: Track largest value <= target
def floor(root, key):
    floor_val = -1

    while root:
        if root.val == key:
            return root.val
        elif root.val < key:
            floor_val = root.val
            root = root.right
        else:
            root = root.left

    return floor_val
```

### Alternative Graph Implementations

#### Cycle Detection (Undirected BFS Alternative)
```python
# Core algorithm: Alternative BFS implementation
from collections import deque

def hasCycleBFS(adj, V):
    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            queue = deque([(i, -1)])  # (node, parent)
            visited[i] = True

            while queue:
                node, parent = queue.popleft()

                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, node))
                    elif neighbor != parent:
                        return True

    return False
```

#### Cycle Detection Schedule Alternative
```python
# Core algorithm: Topological sort to detect cycle
from collections import deque

def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    completed = 0

    while queue:
        course = queue.popleft()
        completed += 1

        for dependent in graph[course]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                queue.append(dependent)

    return completed == numCourses
```

### LRU Cache
```python
# Core algorithm: HashMap + Doubly Linked List
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Create dummy head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def pop_tail(self):
        last_node = self.tail.prev
        self.remove_node(last_node)
        return last_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_head(node)
        else:
            new_node = Node(key, value)

            if len(self.cache) >= self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]

            self.cache[key] = new_node
            self.add_to_head(new_node)
```

---

*This revision file contains the core algorithmic implementations for quick reference during coding interviews and practice sessions.*