# Neetcode Blind 75 — Detailed Solutions

Detailed walkthrough of each solved problem: problem statement, the key trick, and the full solution.

---

## Arrays & Hashing

#### 1. Contains Duplicate

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Arrays & Hashing | Hash Set | Use set to track seen numbers, return True immediately if duplicate found | O(n) | O(n) |

**Problem Statement:**
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and `false` if every element is distinct.

Example:
```
Input:  nums = [1,2,3,1]   ->  Output: true
Input:  nums = [1,2,3,4]   ->  Output: false
```

**Solution:**
```python
"""
TC: O(n)
SC: O(n)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True

            num_set.add(num)

        return False
```

---

#### 2. Valid Anagram

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Arrays & Hashing | Frequency Map | If lengths differ, return False. Build a char->count map for each string, then compare the two maps for equality | O(m + n) | O(m + n) |

**Problem Statement:**
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

Example:
```
Input:  s = "anagram", t = "nagaram"   ->  Output: true
Input:  s = "rat", t = "car"           ->  Output: false
```

**Solution:**
```python
"""
Time Complexity: O(M+N), M is length of s and N is length of t
Space Complexity: O(M+N),
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        s_freq = {}
        t_freq = {}

        for ch in s:
            s_freq[ch] = s_freq[ch]+1 if s_freq.get(ch) else 1

        for ch in t:
            t_freq[ch] = t_freq[ch]+1 if t_freq.get(ch) else 1

        return s_freq == t_freq
```

---

#### 3. Two Sum

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Arrays & Hashing | Hash Map | Store target-cur_no in dict, and for each iteration check if current num exists in dict | O(n) | O(n) |

**Problem Statement:**
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. Exactly one solution exists, and you may not use the same element twice.

Example:
```
Input:  nums = [2,7,11,15], target = 9   ->  Output: [0,1]
```

**Solution:**
```python
import copy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_diff_dict = {}
        n = len(nums)

        for i in range(n):
            cur_no = nums[i]

            if num_diff_dict.get(cur_no) is not None:
                return [num_diff_dict[cur_no], i]

            num_diff_dict[target-cur_no] = i
```

---

#### 4. Top K Frequent Elements

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Arrays & Hashing | Frequency Map + Sort | Build a num->count map, sort items by count descending, take the first k keys | O(n log n) | O(n) |

**Problem Statement:**
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. The answer may be returned in any order.

Example:
```
Input:  nums = [1,1,1,2,2,3], k = 2   ->  Output: [1,2]
```

**Solution:**
```python
"""
TC: O(n log n)
SC: O(n)
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}

        for num in nums:
            data[num] = data[num] + 1 if data.get(num) else 1

        res = []

        for key, val in (sorted(data.items(), key= lambda item: -item[1])):
            if k > 0:
                res.append(key)
                k -= 1

        return res
```

---

#### 5. Product of Array Except Self

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Arrays & Hashing | Prefix/Suffix | First pass: store left products (prefix), Second pass: multiply with right products (suffix) in-place | O(n) | O(1) |

**Problem Statement:**
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. Must run in O(n) without using division.

Example:
```
Input:  nums = [1,2,3,4]   ->  Output: [24,12,8,6]
```

**Solution:**
```python
"""
TC: O(N)
SC: O(1) (+ O(N) auxilary space for output)
"""
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n

        left_prod = 1
        for i in range(0, n):
            output[i] = left_prod
            left_prod *= nums[i]

        right_prod = 1
        for i in range(n-1, -1, -1):
            output[i] *= right_prod
            right_prod *= nums[i]

        return output
```

---

#### 6. Longest Consecutive Sequence

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Arrays & Hashing | Hash Set (Sequence Start) | Put all nums in a set. Only start counting from a sequence START (num-1 not in set), then walk num+1, num+2... while present, tracking the longest run | O(n) | O(n) |

**Problem Statement:**
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. Must run in O(n).

Example:
```
Input:  nums = [100,4,200,1,3,2]   ->  Output: 4   ([1,2,3,4])
```

**Solution:**
```python
"""
TC: O(n)
SC: O(n)
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        res = 1
        nums_set = set()

        for item in nums:
            nums_set.add(item)

        for no in nums_set:
            if no-1 not in nums_set:
                count = 1
                while no+1 in nums_set:
                    count += 1
                    no += 1

                res = max(res, count)

        return res
```

---

## Two Pointers

#### 1. Valid Palindrome

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Two Pointers | Two Pointers | Keep only alphanumeric chars (lowercased), then two pointers from both ends moving inward | O(n) | O(n) |

**Problem Statement:**
Given a string `s`, return `true` if it is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.

Example:
```
Input:  s = "A man, a plan, a canal: Panama"   ->  Output: true
Input:  s = "race a car"                       ->  Output: false
```

**Solution:**
```python
"""
TC: O(n)
SC: O(n)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""

        for ch in s:
            if (ord(ch) >= ord("a") and ord(ch) <= ord("z")) or (ch in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ]):
                new_s += ch

        print(new_s)
        start_index, last_index = 0, len(new_s) -1

        while start_index <= last_index:
            if new_s[start_index] != new_s[last_index]:
                return False

            start_index += 1
            last_index -= 1

        return True
```

---

#### 2. 3Sum

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Two Pointers | Two Pointers | SORT array first! Fix first element, then solve 2Sum on remaining sorted array using two pointers from both ends. Skip duplicates for all three positions | O(n²) | O(1) |

**Problem Statement:**
Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j != k` and `nums[i] + nums[j] + nums[k] == 0`.

Example:
```
Input:  nums = [-1,0,1,2,-1,-4]   ->  Output: [[-1,-1,2],[-1,0,1]]
```

**Solution:**
```python
"""
TC: O(n^2)
SC: O(1) (excluding output)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(0, n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first_num = nums[i]

            start = i + 1
            end = n-1

            while start < end:
                second_num = nums[start]
                third_num = nums[end]

                if first_num + second_num + third_num == 0:
                    res.append([first_num, second_num, third_num])
                    start += 1
                    end -= 1
                    while nums[start] == nums[start-1] and start < end:
                        start += 1

                    while nums[end] == nums[end+1] and start < end:
                        end -= 1

                elif first_num + second_num + third_num < 0:
                    start += 1
                else:
                    end -= 1

        return res
```

---

#### 3. Container With Most Water

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Two Pointers | Two Pointers | Start with pointers at both ends of array. Move pointer with smaller height (wider base won't help with shorter height) | O(n) | O(1) |

**Problem Statement:**
Given `n` non-negative integers `height` representing vertical lines, find two lines that together with the x-axis form a container that holds the most water.

Example:
```
Input:  height = [1,8,6,2,5,4,8,3,7]   ->  Output: 49
```

**Solution:**
```python
"""
TC: O(n)
SC: O(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = -1

        start = 0
        end = n-1

        while start < end:
            area = min(height[start], height[end]) * (end-start)
            res = max(area, res)

            if height[start] <= height[end]:
                cur_height = height[start]
                while start < end and height[start] <= cur_height:
                    start += 1
            else:
                cur_height = height[end]
                while start < end and height[end] <= cur_height:
                    end -= 1

        return res
```

---

## Sliding Window

#### 1. Best Time to Buy and Sell Stock

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Sliding Window | Single Pass | Track min price seen so far, update max profit at each step | O(n) | O(1) |

**Problem Statement:**
Given an array `prices` where `prices[i]` is the price of a stock on day `i`, find the maximum profit from buying on one day and selling on a later day. Return 0 if no profit is possible.

Example:
```
Input:  prices = [7,1,5,3,6,4]   ->  Output: 5   (buy at 1, sell at 6)
```

**Solution:**
```python
"""
TC: O(n)
SC: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            cur_price = prices[i]
            max_profit = max(max_profit, cur_price - min_price)

            if cur_price < min_price:
                min_price = cur_price

        return max_profit
```

---

#### 2. Longest Substring Without Repeating Characters

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Sliding Window | Sliding Window | Expand right pointer adding chars to a count map. When the new char's count > 1, shrink from left until no duplicate | O(n) | O(min(n, charset)) |

**Problem Statement:**
Given a string `s`, find the length of the longest substring without repeating characters.

Example:
```
Input:  s = "abcabcbb"   ->  Output: 3   ("abc")
```

**Solution:**
```python
"""
TC: O(n)
SC: O(min(n, charset))
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result_len = 0
        l,r = 0, 0
        curr_char = {}
        size = len(s)

        while r < size :
            curr_char[s[r]] = curr_char.get(s[r], 0) + 1
            while curr_char[s[r]] > 1:
                curr_char[s[l]] -= 1
                l += 1


            if result_len < r-l+1 :
                result_len = r-l+1

            r += 1

        return result_len
```

---

#### 3. Longest Repeating Character Replacement

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Sliding Window | Sliding Window + Max Freq | Window is valid when (window_len - count of most frequent char) <= k. Expand right and update max_freq; when invalid, shrink left | O(n) | O(charset) |

**Problem Statement:**
Given a string `s` and an integer `k`, you can change up to `k` characters to any other uppercase letter. Return the length of the longest substring containing the same letter after such replacements.

Example:
```
Input:  s = "ABAB", k = 2   ->  Output: 4
```

**Solution:**
```python
"""
TC: O(n)
SC: O(charset)
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l ,r = 0, 0
        char_freq = {}
        max_freq = 1
        size = len(s)
        is_window_len_changed = True

        while r < size:
            window_len = r - l + 1
            if is_window_len_changed:
                char_freq[s[r]] =  char_freq.get(s[r]) + 1 if char_freq.get(s[r]) else 1
                max_freq = char_freq[s[r]] if max_freq < char_freq[s[r]] else max_freq
            else:
                char_freq[s[l-1]] =  char_freq.get(s[l-1]) - 1

            if window_len - max_freq <= k:
                r += 1
                is_window_len_changed = True
            else:
                l += 1
                is_window_len_changed = False

        return r-l
```

---

#### 4. Minimum Window Substring

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Sliding Window | Sliding Window + Need Count | Build required-char counts from t and track how many required chars are currently satisfied. Expand right; once all requirements met, shrink left while still valid | O(m + n) | O(charset) |

**Problem Statement:**
Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. Return `""` if no such substring exists.

Example:
```
Input:  s = "ADOBECODEBANC", t = "ABC"   ->  Output: "BANC"
```

**Solution:**
```python
"""
TC: O(m + n)
SC: O(charset)
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        size = len(s)
        result = ""
        result_len = float("inf")
        l, r = 0, 0
        required_chars = {}
        window = {}
        required_len = len(t)
        current_len = 0
        is_new_char_added_in_window = True
        for curr_char in t:
            required_chars[curr_char] = 1 + required_chars.get(curr_char, 0)
            window[curr_char] = 0

        while r < size and l <= r:
            if s[r] in t and is_new_char_added_in_window:
                window[s[r]] += 1
                if window[s[r]] <= required_chars[s[r]]:
                    current_len += 1

            #print(required_len, current_len, window)
            if required_len == current_len:
                curr_substring = s[l:r+1]
                if len(curr_substring) < result_len:
                    result = curr_substring
                    result_len = len(curr_substring)
                    #print(result)

                if not required_chars.get(s[l]):
                    l += 1
                    is_new_char_added_in_window = False
                    continue

                if window[s[l]] > required_chars[s[l]]:
                    window[s[l]] -= 1
                    l += 1
                    is_new_char_added_in_window = False
                    continue

                window[s[l]] -= 1
                current_len -= 1
                l += 1
                is_new_char_added_in_window = True

            r += 1

        return result
```

---

## Stack

#### 1. Valid Parentheses

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Stack | Matching Stack | Push opening brackets; on a closing bracket check it matches the top opening (pop if so). Valid only if every closer matched and the stack is empty at the end | O(n) | O(n) |

**Problem Statement:**
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid (every open bracket is closed by the same type in the correct order).

Example:
```
Input:  s = "()[]{}"   ->  Output: true
Input:  s = "(]"       ->  Output: false
```

**Solution:**
```python
"""
TC: O(n)
SC: O(n)
"""
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for element in s:
            if len(stack) == 0:
                stack.append(element)
            else:
                if element == "}" and stack[-1] == "{" \
                    or element == ")" and stack[-1] == "(" \
                    or element == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(element)

        return len(stack) == 0
```

---

## Binary Search

#### 1. Find Minimum in Rotated Sorted Array

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Binary Search | Modified Binary Search | If nums[mid] > nums[right]: rotation point (min) is in right half, else in left half. Keep searching until left == right | O(log n) | O(1) |

**Problem Statement:**
Given a rotated sorted array `nums` of unique elements, return the minimum element. Must run in O(log n).

Example:
```
Input:  nums = [3,4,5,1,2]   ->  Output: 1
```

**Solution:**
```python
"""
TC: O(log n)
SC: O(1)
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search solution
        n = len(nums)
        start, end = 0, n-1
        res = float("inf")

        while start <= end:
            mid = (start + end) // 2

            is_left_sorted = True if nums[start] <= nums[mid] else False

            if is_left_sorted:
                res = min(res, nums[start])
                start = mid + 1
            else:
                res = min(res, nums[mid])
                end = mid - 1

        return res
```

---

#### 2. Search in Rotated Sorted Array

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Binary Search | Modified Binary Search | Identify sorted half, check if target in sorted range, search appropriate half | O(log n) | O(1) |

**Problem Statement:**
Given a rotated sorted array `nums` of unique elements and a `target`, return the index of `target` if found, else `-1`. Must run in O(log n).

Example:
```
Input:  nums = [4,5,6,7,0,1,2], target = 0   ->  Output: 4
```

**Solution:**
```python
"""
TC: O(log n)
SC: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1

        while low <= high:
            mid = (low+high) // 2

            if nums[mid] == target:
                return mid

            is_left_half_sorted = nums[low] <= nums[mid]

            if is_left_half_sorted:
                if nums[low] <= target and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            # is right half sorted
            else:
                if nums[mid] < target and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1

        return -1
```

---

## Linked List

#### 1. Reverse Linked List

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Pointer Reversal | Walk the list keeping prev and cur; each step save next, point cur.next back to prev, then advance prev=cur, cur=next | O(n) | O(1) iterative / O(n) recursive |

**Problem Statement:**
Given the head of a singly linked list, reverse the list and return the new head.

Example:
```
Input:  head = [1,2,3,4,5]   ->  Output: [5,4,3,2,1]
```

**Solution:**
```python
"""
TC: O(n)
SC: O(n) recursion stack
"""
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(first, second):
            if not second:
                return first

            temp = second.next
            second.next = first
            return reverse_list(second, temp)

        head = reverse_list(None, head)

        return head
```

---

#### 2. Linked List Cycle

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Fast & Slow Pointers | Move slow by 1 and fast by 2. If there's a cycle they eventually meet; if fast (or fast.next) hits None, the list ends => no cycle | O(n) | O(1) |

**Problem Statement:**
Given the head of a linked list, determine if it has a cycle.

Example:
```
Input:  head = [3,2,0,-4], tail connects to node index 1   ->  Output: true
```

**Solution:**
```python
"""
TC: O(n)
SC: O(1)
"""
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = head
        second = head

        while first and second and second.next:
            first = first.next
            second = second.next.next

            if first == second:
                return True

        return False
```

---

#### 3. Remove Nth Node From End of List

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Two Pointers (Gap of n) | Advance fast n steps first. If fast is None, the head itself is the target. Else move slow and fast together until fast.next is None | O(n) | O(1) |

**Problem Statement:**
Given the head of a linked list, remove the `n`-th node from the end of the list and return its head.

Example:
```
Input:  head = [1,2,3,4,5], n = 2   ->  Output: [1,2,3,5]
```

**Solution:**
```python
"""
TC: O(n)
SC: O(1)
"""
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next
        # Case to delete the first node of the linked list
        if not fast:
            head = head.next
            return head

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
```

---

## Trees

#### 1. Maximum Depth of Binary Tree

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trees | DFS Recursion | Depth of a node = 1 + max(depth of left subtree, depth of right subtree). Base case: null node => 0 | O(n) | O(h) recursion stack |

**Problem Statement:**
Given the root of a binary tree, return its maximum depth (number of nodes along the longest path from root to farthest leaf).

Example:
```
Input:  root = [3,9,20,null,null,15,7]   ->  Output: 3
```

**Solution:**
```python
"""
TC: O(n)
SC: O(h) recursion stack
"""
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def get_height(cur_node):
            if not cur_node:
                return 0

            left_subtree_height = get_height(cur_node.left)
            right_subtree_height = get_height(cur_node.right)

            return 1 + max(left_subtree_height, right_subtree_height)

        return get_height(root)
```

---

#### 2. Same Tree

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trees | Parallel DFS | Recurse both trees in lockstep. Both null => True; one null or values differ => False; else recurse left-with-left AND right-with-right | O(n) | O(h) recursion stack |

**Problem Statement:**
Given the roots of two binary trees `p` and `q`, return `true` if they are the same (structurally identical and same node values).

Example:
```
Input:  p = [1,2,3], q = [1,2,3]   ->  Output: true
```

**Solution:**
```python
"""
TC: O(n)
SC: O(h) recursion stack
"""
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def is_same_tree(fst_cur_node, scd_cur_node):

            if not fst_cur_node and not scd_cur_node:
                return True

            # if two nodes are not same return false
            if (not fst_cur_node and scd_cur_node) or (fst_cur_node and not scd_cur_node) or \
             not (fst_cur_node.val == scd_cur_node.val) :
                return False

            # left subtree visit
            left = is_same_tree(fst_cur_node.left, scd_cur_node.left)
            # right subtree visit
            if left:
                right = is_same_tree(fst_cur_node.right, scd_cur_node.right)

            return left and right

        return is_same_tree(p, q)
```

---

#### 3. Lowest Common Ancestor of a Binary Search Tree

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trees | BST Property Walk | Use the ordering: if both p and q are less than node, go left; if both greater, go right; otherwise this node is the LCA | O(h) | O(h) recursion stack |

**Problem Statement:**
Given a binary search tree (BST) and two nodes `p` and `q`, find their lowest common ancestor.

Example:
```
Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8   ->  Output: 6
```

**Solution:**
```python
"""
TC: O(h)
SC: O(h) recursion stack
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            temp = p
            p = q
            q = temp

        def get_common_ancestor(node: "TreeNode"):
            if p.val < node.val and q.val < node.val:
                return get_common_ancestor(node.left)
            elif p.val > node.val and q.val > node.val:
                return get_common_ancestor(node.right)
            # The below 2 cases not checked both returns the node, thus we simply return the node
            # if p.val < node.val and node.val < q.val:
            # if p.val == node.val or q.val == node.val:
            return node

        return get_common_ancestor(root)
```

---

#### 4. Binary Tree Level Order Traversal

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trees | BFS (Level Tracking) | BFS with a queue, tagging each node with its level and appending to res[level]. Enqueue left then right children | O(n) | O(n) |

**Problem Statement:**
Given the root of a binary tree, return the level order traversal of its nodes' values (left to right, level by level).

Example:
```
Input:  root = [3,9,20,null,null,15,7]   ->  Output: [[3],[9,20],[15,7]]
```

**Solution:**
```python
"""
TC: O(n)
SC: O(n)
"""
from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque([(root, 0)])

        while queue:
            cur_node, cur_level = queue.popleft()

            if not cur_node:
                continue

            if len(res) <= cur_level:
                res.append([])

            res[cur_level].append(cur_node.val)

            # add left child to queue
            queue.append((cur_node.left, cur_level+1))
            # add right child to queue
            queue.append((cur_node.right, cur_level+1))

        return res
```

---

#### 5. Validate Binary Search Tree

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trees | Min/Max Bounds DFS | Recurse carrying an open (min, max) range each node must fall strictly inside. Going left tightens the max, going right tightens the min | O(n) | O(h) |

**Problem Statement:**
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

Example:
```
Input:  root = [2,1,3]   ->  Output: true
Input:  root = [5,1,4,null,null,3,6]   ->  Output: false
```

**Solution:**
```python
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Time Complexity: O(N),  actually O(2N) - O(n) for inorder traversal and o(n) for looping over the res
Space complexity: O(N), again O(2N) - O(n) for recursion stack and O(n) for storing in order result
Space Complexity:

We have used the logic that if we run a inorder traversal on BST it returns an sorted array, so we
simply have run the in order traversal on the given binary tree and checked if it's sorted or not
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def get_valid_bst(node, min_limit, max_limit):
            if not node:
               return True

            if min_limit < node.val and node.val < max_limit:
                left_tree_res = get_valid_bst(node.left, min_limit, node.val)
                right_tree_res = get_valid_bst(node.right, node.val, max_limit)
                return left_tree_res and right_tree_res
            else:
                return False

        return get_valid_bst(root, float("-inf"), float("inf"))
```

---

#### 6. Kth Smallest Element in a BST

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trees | Inorder Traversal | Inorder (left, node, right) of a BST visits values in sorted order, so the kth visited node is the answer | O(n) | O(n) |

**Problem Statement:**
Given the root of a binary search tree and an integer `k`, return the `k`-th smallest value (1-indexed) among all the values of the nodes.

Example:
```
Input:  root = [3,1,4,null,2], k = 1   ->  Output: 1
```

**Solution:**
```python
"""
TC: O(n)
SC: O(n)
"""
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def pre_order_traversal(node, res=[]):
            if not node:
                return

            pre_order_traversal(node.left, res)
            res.append(node.val)
            pre_order_traversal(node.right, res)

            return res

        res =  pre_order_traversal(root)
        return res[k-1]
```

---

#### 7. Construct Binary Tree from Preorder and Inorder Traversal

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trees | Recursive Split | preorder[0] is always the root. Find it in inorder: everything left of it is the left subtree, everything right is the right subtree. Split both arrays and recurse | O(n²) | O(n²) |

**Problem Statement:**
Given two integer arrays `preorder` and `inorder` representing the preorder and inorder traversal of a binary tree, construct and return the binary tree.

Example:
```
Input:  preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]   ->  Output: [3,9,20,null,null,15,7]
```

**Solution:**
```python
"""
TC: O(n^2)
SC: O(n^2)
"""
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Simple fn that returns index of element in an list
        def search_element_in_arr(arr, val):
            for i in range(len(arr)):
                if arr[i] == val:
                    return i

            return -1

        def build_binary_tree(pre_order_arr, in_order_arr):
            # Base cases
            if len(pre_order_arr) == 0:
                return None
            elif len(pre_order_arr) == 1:
                return TreeNode(pre_order_arr[0])

            root_val = pre_order_arr[0]
            root_in_order_index = search_element_in_arr(in_order_arr, root_val)
            # building left and right subtree in order traversal arr
            left_in_order_tree = in_order_arr[0:root_in_order_index]
            right_in_order_tree = in_order_arr[root_in_order_index+1:]
            # total count of left subtree nodes
            left_subtree_node_count = len(left_in_order_tree)
            # building left and right subtree in pre order traversal arr
            left_pre_order_tree = pre_order_arr[1 : 1+left_subtree_node_count]
            right_pre_order_tree = pre_order_arr[1+left_subtree_node_count : ]
            # Creating root node and setting up left and right node using recursive call of fn
            root_node = TreeNode(root_val)
            root_node.left = build_binary_tree(left_pre_order_tree, left_in_order_tree)
            root_node.right = build_binary_tree(right_pre_order_tree, right_in_order_tree)
            # returning the root node
            return root_node

        return build_binary_tree(preorder, inorder)
```

---

#### 8. Binary Tree Maximum Path Sum

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trees | DFS (Return vs Update) | Each DFS returns the best straight-line path going DOWN one side, clamping negatives to 0. Separately update a global max with the best path THROUGH the node | O(n) | O(h) |

**Problem Statement:**
Given the root of a binary tree, return the maximum path sum of any non-empty path (a path need not pass through the root).

Example:
```
Input:  root = [-10,9,20,null,null,15,7]   ->  Output: 42
```

**Solution:**
```python
"""
TC: O(n)
SC: O(h) recursion stack
"""
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float("-inf")]
        def path_sum_in_order(cur_node):
            if not cur_node:
                return 0

            cur_sum = cur_node.val
            left_sum = path_sum_in_order(cur_node.left)
            right_sum = path_sum_in_order(cur_node.right)

            if left_sum < 0:
                left_sum = 0

            if right_sum < 0:
                right_sum = 0

            max_sum[0] = max(max_sum[0], cur_sum+left_sum+right_sum)


            return max(cur_sum+left_sum, cur_sum+right_sum)

        path_sum_in_order(root)
        return max_sum[0]
```

---

## Backtracking

#### 1. Combination Sum

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Backtracking | Pick / Not-Pick Recursion | Same element can be reused, so on "pick" stay on the same index. On "not pick" move to the next index. When the sum equals the target, save the current array | O(k * 2^(n + k)) | O(n + k²) |

**Problem Statement:**
Given an array of distinct integers `candidates` and a `target`, return all unique combinations where the chosen numbers sum to `target`. The same number may be chosen an unlimited number of times.

Example:
```
Input:  candidates = [2,3,6,7], target = 7   ->  Output: [[2,2,3],[7]]
```

**Solution:**
```python
"""
TC: O(k * 2^(n + k))
SC: O(n + k^2)
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []

        def combination_sum(cur_index, cur_arr=[], cur_sum=0):
            if cur_index >= n:
                return

            if cur_sum > target:
                return

            if cur_sum == target:
                res.append(cur_arr)
                return

            cur_val = candidates[cur_index]

            combination_sum(cur_index, cur_arr + [cur_val], cur_sum+cur_val)
            combination_sum(cur_index+1, cur_arr, cur_sum)

        combination_sum(0)

        return res
```

---

#### 2. Word Search

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Backtracking | Grid DFS + Backtrack | From each cell matching word[0], DFS in 4 directions matching one char per step. Mark the cell visited before recursing and unmark after (backtrack) | O(m * n * 4^L) | O(L) recursion (+ O(m*n) visited) |

**Problem Statement:**
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid (formed by sequentially adjacent cells, not reusing a cell).

Example:
```
Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"   ->  Output: true
```

**Solution:**
```python
"""
TC: O(m * n * 4^L)
SC: O(L) recursion (+ O(m*n) visited)
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        col_max = len(board[0])   # row
        row_max = len(board)      # col
        word_len = len(word)
        visited = [[False for _ in range(col_max)] for _ in range(row_max)]

        def find_word(row, col, cur_word_ind):
            if cur_word_ind == word_len:
                return True

            if row < 0 or col < 0 or row >= row_max or col >= col_max or visited[row][col] or word[cur_word_ind] != board[row][col]:
                return False

            visited[row][col] = True
            #print(cur_seq, visited)

            # top
            top = find_word(row-1, col, cur_word_ind+1)
            # right
            right = find_word(row, col+1,  cur_word_ind+1)
            # bottom
            bottom = find_word(row+1, col,  cur_word_ind+1)
            # left
            left = find_word(row, col-1,  cur_word_ind+1)

            visited[row][col] = False

            return top or right or bottom or left

        for j in range(col_max):
            for i in range(row_max):
                if board[i][j] == word[0]:
                    if find_word(i, j, 0):
                        return True

        return False
```

---

## Tries

#### 1. Implement Trie (Prefix Tree)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Tries | Nodes with 26 Children | Each node holds 26 child links + an is_end flag. insert/search/startsWith walk one char at a time creating or checking links | insert/search O(L) | O(total chars) |

**Problem Statement:**
Implement a trie with `insert`, `search`, and `startsWith` methods.

Example:
```
Input:  insert("apple"); search("apple") -> true; search("app") -> false; startsWith("app") -> true
```

**Solution:**
```python
"""
insert/search: O(L)
SC: O(total chars)
"""
class Node:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False

    def contains_key(self, ch: str) -> 'Node':
        return self.links[ord(ch)-ord("a")]     # ord returns ascii code of character

    # fn that returns node reference for char ch
    def get(self, ch: str) -> 'Node':
        return self.links[ord(ch)-ord("a")]

    def put(self, ch: str, node: 'Node') -> None:
        self.links[ord(ch)-ord("a")] = node

    def set_end(self) -> 'Node':
        self.flag = True

    def is_end(self) -> bool:
        return self.flag




class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                node.put(cur_char, Node())
            node = node.get(cur_char)
        node.set_end()

    def search(self, word: str) -> bool:
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                return False

            node = node.get(cur_char)

        return node.is_end()

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for cur_char in prefix:
            if not node.contains_key(cur_char):
                return False

            node = node.get(cur_char)

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

---

## Graphs

#### 1. Number of Islands

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Graphs | Grid DFS (Flood Fill) | Scan every cell; when you hit an unvisited '1', increment the island count and DFS/flood-fill all connected land, marking cells visited | O(m * n) | O(m * n) |

**Problem Statement:**
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

Example:
```
Input:  grid = [["1","1","0","0"],["1","1","0","0"],["0","0","1","0"],["0","0","0","1"]]   ->  Output: 3
```

**Solution:**
```python
"""
TC: O(m * n)
SC: O(m * n)
"""
from typing import List


class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:
        total_rows = len(grid)
        total_columns = len(grid[0])
        visited_nodes = []
        for i in range(total_rows):
            temp_arr = []
            for j in range(total_columns):
                temp_arr.append(0)
            visited_nodes.append(temp_arr)


        total_dist_comp = 0

        def islandHop(i,j):

            if not (i < total_rows and j < total_columns and i >= 0 and j >= 0):
                return False
            if grid[i][j] == "0" or visited_nodes[i][j]:
                return False

            if not visited_nodes[i][j] and grid[i][j] == "1":
                visited_nodes[i][j] = 1
                islandHop(i+1,j)
                islandHop(i-1,j)
                islandHop(i,j+1)
                islandHop(i,j-1)

            return True

        for row_index in range(total_rows):
            for column_index in range(total_columns):
                if not visited_nodes[row_index][column_index]:
                    if islandHop(row_index, column_index):
                        print(row_index, column_index)
                        total_dist_comp += 1


        return total_dist_comp
```

---

#### 2. Pacific Atlantic Water Flow

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Graphs | Reverse-Flow DFS from Borders | Instead of testing every cell, invert it: seed one visited-set per ocean from its border cells and DFS inward to neighbours with height >= current. A cell in BOTH sets can drain to both oceans | O(m * n) | O(m * n) |

**Problem Statement:**
Given an `m x n` matrix of heights, return the list of grid coordinates where water can flow to both the Pacific and Atlantic oceans (Pacific touches the top/left edges, Atlantic touches the bottom/right edges). Water flows from a cell to an adjacent cell with height less than or equal to the current cell's height.

Example:
```
Input:  heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

**Solution:**
```python
"""
TC: O(m * n)
SC: O(m * n)

Reverse-flow DFS. Instead of asking "can this cell reach both oceans", start
from each ocean's border cells and DFS inward, moving to neighbours with height
>= current (water flows uphill in reverse). Cells reachable from both oceans are
the answer.
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        no_of_rows = len(heights)
        no_of_columns = len(heights[0])

        pacific_ocean_visit = set()
        atlantic_ocean_visit = set()
        result = []

        def dfs(cur_row, cur_col, reachable):
            # if we are getting to this node that means it is visitable/ reachable
            reachable.add((cur_row, cur_col))

            # top, right, bottom, left
            for (x, y) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row = cur_row+x
                new_col = cur_col+y

                if new_row < 0 or new_col < 0 or new_row >= no_of_rows or new_col >= no_of_columns:
                    continue

                if (new_row, new_col) in reachable:
                    continue

                if heights[new_row][new_col] < heights[cur_row][cur_col]:
                    continue

                dfs(new_row, new_col, reachable)


        for r in range(no_of_rows):
            dfs(r, 0, pacific_ocean_visit)
            dfs(r, no_of_columns-1, atlantic_ocean_visit)

        for c in range(no_of_columns):
            dfs(0, c, pacific_ocean_visit)
            dfs(no_of_rows-1, c, atlantic_ocean_visit)

        for r in range(no_of_rows):
            for c in range(no_of_columns):
                if (r, c) in pacific_ocean_visit and (r, c) in atlantic_ocean_visit:
                    result.append([r, c])

        return result
```

---

#### 3. Course Schedule

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Graphs | DFS Cycle Detection | Build adjacency list (course -> prereqs). DFS each node tracking the current path (visited). If a node is revisited while still on the path => cycle => can't finish | O(V + E) | O(V + E) |

**Problem Statement:**
There are `numCourses` courses labeled `0` to `numCourses - 1`. Given `prerequisites` where `prerequisites[i] = [a, b]` means you must take `b` before `a`, return `true` if you can finish all courses.

Example:
```
Input:  numCourses = 2, prerequisites = [[1,0]]   ->  Output: true
Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]   ->  Output: false
```

**Solution:**
```python
"""
TC: O(V + E)
SC: O(V + E)

Cycle detection in a directed graph (DFS). If a node is revisited while still on
the current DFS path (visited but not yet completed) => cycle => cannot finish.
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node_graph = [[] for i in range(numCourses)]

        for item in prerequisites:
            main_course = item[0]
            pre_req_course = item[1]
            node_graph[main_course].append(pre_req_course)

        course_completed = [0] * numCourses

        def courseFinish(node: int, visited_nodes: List[int]) -> bool:
            if course_completed[node]:
                return True

            if not course_completed[node] and visited_nodes[node]:
                return False

            visited_nodes[node] = 1

            if len(node_graph[node]) == 0:
                course_completed[node] = True
                return True

            for adj_node in node_graph[node]:
                if not courseFinish(adj_node, visited_nodes):
                    return False

            course_completed[node] = True
            return True


        for item in range(numCourses):
            if not course_completed[item]:
                if not courseFinish(item, [0]*numCourses):
                    return False

        return True
```

---

## Intervals

#### 1. Insert Interval

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Intervals | Sort + Merge Scan | Append the new interval, sort by start time, then walk pairwise merging current into next while they overlap | O(n log n) | O(n) |

**Problem Statement:**
Given a set of non-overlapping intervals sorted by start time and a new interval, insert the new interval and merge if necessary.

Example:
```
Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]   ->  Output: [[1,5],[6,9]]
```

**Solution:**
```python
"""
TC: O(n log n)
SC: O(n)
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            intervals.append(newInterval)
            intervals.sort(key=lambda x: x[0])
            size = len(intervals)
            result = []

            current, next = 0,1
            start, end = 0, 1

            while next < size:
                if intervals[current][start] <= intervals[next][start] <= intervals[current][end]:
                    intervals[current][start] = min(intervals[current][start], intervals[next][start])
                    intervals[current][end] = max(intervals[current][end], intervals[next][end])

                    next += 1
                    continue

                result.append(intervals[current])
                current = next
                next += 1

            result.append(intervals[current])

            return result
```

---

#### 2. Merge Intervals

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Intervals | Sort + Merge Scan | Sort by start time, then walk pairwise: merge current into next while they overlap, else push current to result and move on | O(n log n) | O(n) |

**Problem Statement:**
Given an array of intervals, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example:
```
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]   ->  Output: [[1,6],[8,10],[15,18]]
```

**Solution:**
```python
"""
TC: O(n log n)
SC: O(n)
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        size = len(intervals)
        result = []

        current, next = 0,1
        start, end = 0, 1

        while next < size:
            if intervals[current][start] <= intervals[next][start] <= intervals[current][end]:
                intervals[current][start] = min(intervals[current][start], intervals[next][start])
                intervals[current][end] = max(intervals[current][end], intervals[next][end])

                next += 1
                continue

            result.append(intervals[current])
            current = next
            next += 1

        result.append(intervals[current])

        return result
```

---

#### 3. Non Overlapping Intervals

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Intervals | Greedy (Sort by End Time) | Sort by end time. Whenever the next interval's start is before the current interval's end (overlap), drop it and count an erasure | O(n log n) | O(1) |

**Problem Statement:**
Given an array of intervals, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example:
```
Input:  intervals = [[1,2],[2,3],[3,4],[1,3]]   ->  Output: 1
```

**Solution:**
```python
"""
TC: O(n log n)
SC: O(1)
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals on the basis of end time of interval
        intervals.sort(key=lambda x: x[1])
        res,ind = 0, 0

        while ind < len(intervals)-1:
            cur_interval_end = intervals[ind][1]
            next_interval_start = intervals[ind+1][0]
            # pop next interval if the next interval overlaps with cur one
            if next_interval_start < cur_interval_end:
                intervals.pop(ind+1)
                res += 1
                continue

            ind += 1

        return res
```

---

## 1-D Dynamic Programming

#### 1. Climbing Stairs

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 1-D DP | Bottom-Up DP (Backwards) | Start with both n and n-1 base cases = 1. Loop from n-2 to 0: ways(i) = ways(i+1) + ways(i+2). Use 2 vars to optimize space | O(n) | O(1) |

**Problem Statement:**
You are climbing a staircase that takes `n` steps to reach the top. Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
```
Input:  n = 3   ->  Output: 3   (1+1+1, 1+2, 2+1)
```

**Solution:**
```python
"""
TC: O(n)
SC: O(1)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        res = [0, 1, 2]
        first = 1
        second = 2

        for i in range(n-2):
            temp = first + second
            first = second
            second = temp

        return second
```

---

#### 2. House Robber

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 1-D DP | Pick / Not-Pick with Memoization | rob(i): "pick" = nums[i] + rob(i-2) (skip adjacent), "not pick" = rob(i-1). Take max. Memoize by index | O(n) | O(n) |

**Problem Statement:**
Given an array of non-negative integers representing money in each house (adjacent houses have security systems linked), return the maximum amount you can rob without alerting the police (can't rob two adjacent houses).

Example:
```
Input:  nums = [1,2,3,1]   ->  Output: 4   (rob house 1 and 3)
```

**Solution:**
```python
"""
TC: O(n)
SC: O(n) memo + O(n) recursion stack

Check older solution not this one
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * (n)

        def robMax(n, min_index):
            if n < min_index:
                return 0

            if not memo[n] == -1:
                return memo[n]

            pick = nums[n] + robMax(n-2, min_index)
            not_picked = 0 + robMax(n-1, min_index)

            memo[n] = max(pick, not_picked)

            return memo[n]
        return robMax(n-1, 0)
```

---

#### 3. House Robber II

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 1-D DP | Two Linear Runs (Circular) | Houses are circular so first and last are adjacent. Run House Robber twice: on [0..n-2] and [1..n-1], take the max | O(n) | O(n) |

**Problem Statement:**
Same as House Robber, but the houses are arranged in a circle (the first and last house are adjacent).

Example:
```
Input:  nums = [2,3,2]   ->  Output: 3
```

**Solution:**
```python
"""
TC: O(n)
SC: O(n) memo + O(n) recursion stack

Circular street => either rob houses [0..n-2] (exclude last) or [1..n-1] (exclude first),
then take the max of the two linear House Robber runs.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if len(nums) == 1:
            return nums[0]

        def robMax(n, min_index, memo):
            if n < min_index:
                return 0

            if not memo[n] == -1:
                return memo[n]

            pick = nums[n] + robMax(n-2, min_index, memo)
            not_picked = 0 + robMax(n-1, min_index, memo)

            memo[n] = max(pick, not_picked)

            return memo[n]

        return max(
            robMax(n-1, 1, [-1] * (n)),
            robMax(n-2, 0, [-1] * (n))
        )
```

---

#### 4. Longest Palindromic Substring

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 1-D DP | Expand Around Center | For each index i, expand outward for odd and even palindromes. While s[left]==s[right] keep expanding. Slice s[left+1:right] gives the palindrome | O(n²) | O(1) |

**Problem Statement:**
Given a string `s`, return the longest palindromic substring in `s`.

Example:
```
Input:  s = "babad"   ->  Output: "bab"  (or "aba")
```

**Solution:**
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        n = len(s)

        def expand(left_index, right_index):
            while left_index >= 0 and right_index < n and s[left_index] == s[right_index]:
                left_index -= 1
                right_index += 1
            # this will return the most possible expanded string
            return s[left_index+1: right_index]

        for i in range(n):
            odd = expand(i, i)
            even = expand(i, i+1)

            if len(odd) > len(result):
                result = odd

            if len(even) > len(result):
                result = even

        return result
```

---

#### 5. Decode Ways

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 1-D DP | Bottom-Up DP | dp[i] = ways to decode s[0..i]. dp[i] += dp[i-1] if s[i] != '0'; dp[i] += dp[i-2] if 10 <= int(s[i-1:i+1]) <= 26 | O(n) | O(n) |

**Problem Statement:**
A message containing letters A-Z is encoded to numbers using `'A'->1, ..., 'Z'->26`. Given a string `s` of digits, return the number of ways to decode it.

Example:
```
Input:  s = "226"   ->  Output: 3   ("2 2 6", "22 6", "2 26")
```

**Solution:**
```python
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = number of ways to decode s[0..i] (i.e., s[0:i+1])
        # dp[i] = dp[i-1] + dp[i-2] where:
        #   dp[i-1]: valid if s[i] != '0' (current char decoded as single digit 1-9)
        #   dp[i-2]: valid if s[i-1:i+1] is a two-digit code between 10-26
        # One digit valid check: s[i] != '0'
        # Two digit valid check: 10 <= int(s[i-1:i+1]) <= 26
        n = len(s)
        dp = [0] * n

        dp[0] = 1 if s[0] != "0" else 0
        if n > 1:
            dp[1] = dp[0] if int(s[1]) != 0 else 0 # no of way to decode s[0..1] is no of ways to reach s[1] from s[0] + no of ways to take s[0] and s[1] combined
            dp[1] += 1 if int(s[0:2]) >= 10 and int(s[0:2]) <= 26 else 0

        for cur_index in range(2, n):
            prev_index = cur_index - 1
            prev_prev_index = cur_index - 2

            # 110 (11, 0 ) is not valid so we are checking cur index char should not be 0
            dp[cur_index] = dp[prev_index] if int(s[cur_index]) != 0 else 0
            # here combined prev char + cur char and if these 2 digits are valid then no of ways to reach to this (combined 2 digit code) is no of ways to reach 1 digit before the combined digit and same no
            # will be here as well if combined digit is valid as no of ways to reach combined digit from pre prev char will be same (as there is only one way from there to here)
            dp[cur_index] += dp[prev_prev_index] if int(s[prev_index: cur_index+1]) >= 10 and int(s[prev_index: cur_index+1]) <= 26 else 0


        return dp[n-1]
```

---

#### 6. Coin Change

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 1-D DP | Pick / Not-Pick with Memoization | solve(i, target): "pick" reuses same coin so stay on index i and subtract coin, "not pick" moves to i-1. Answer inf => -1 | O(n * amount) | O(n * amount) |

**Problem Statement:**
Given an array of coin denominations and a total `amount`, return the fewest number of coins needed to make up that amount, or `-1` if it can't be made.

Example:
```
Input:  coins = [1,2,5], amount = 11   ->  Output: 3   (5+5+1)
```

**Solution:**
```python
"""
TC: O(n * amount)
SC: O(n * amount) (memo) + O(amount) recursion stack
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = [[-1] * (amount+1) for _ in range(n)]

        def coin_change(index, target):
            if target < 0:
                return float("inf")

            if index == 0:
                return target // coins[index] if target % coins[index] == 0 else float("inf")

            if not memo[index][target] == -1:
                return memo[index][target]

            pick = 1 + coin_change(index, target-coins[index])

            unpick = coin_change(index-1, target)

            memo[index][target] = min(pick, unpick)

            return memo[index][target]

        res = coin_change(n-1, amount)

        return -1 if res == float("inf") else res
```

---

#### 7. Maximum Product Subarray

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 1-D DP | Prefix/Suffix | Track prefix product L→R and suffix product R→L. When hit 0, reset to 1. Max product is max of all prefix/suffix values | O(n) | O(1) |

**Problem Statement:**
Given an integer array `nums`, find a contiguous non-empty subarray that has the largest product, and return the product.

Example:
```
Input:  nums = [2,3,-2,4]   ->  Output: 6   ([2,3])
```

**Solution:**
```python
"""
TC: O(n)
SC: O(1)

Optimized approach (single pass, prefix & suffix together)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        prefix = 1
        suffix = 1
        n = len(nums)
        res = float("-inf")

        j = n-1
        for i in range(0, n):
            j = n-1-i

            prefix *= nums[i]
            suffix *= nums[j]

            res = max(res, prefix, suffix)

            if nums[i] == 0:
                prefix = 1

            if nums[j] == 0:
                suffix = 1


        return res
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        prefix = 1
        suffix = 1
        no_of_neg = 0
        n = len(nums)
        res = float("-inf")

        for i in range(0, n):
            prefix *= nums[i]
            res = max(res, prefix)

            if nums[i] == 0:
                prefix = 1


        for i in range(n-1, -1, -1):
            suffix *= nums[i]
            res = max(res, suffix)

            if nums[i] == 0:
                suffix = 1

        return res
```

---

#### 8. Word Break

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 1-D DP | Top-Down DP with Memoization | memo[i] = can s[0..i] be segmented using wordDict. For each index, try matching every word in dict starting at that position | O(n * m * k) | O(n) |

**Problem Statement:**
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Example:
```
Input:  s = "leetcode", wordDict = ["leet","code"]   ->  Output: true
```

**Solution:**
```python
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [-1]*n

        def word_break(index):
            if index == n:
                return True

            if memo[index] != -1:
                return memo[index]

            result = False
            for word in wordDict:
                word_len = len(word)
                if s[index: index+word_len] == word:
                    # pick
                    result = result or word_break(index+word_len)

            memo[index] = result
            return result

        return word_break(0)
```

---

#### 9. Longest Increasing Subsequence

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 1-D DP | Bottom-Up DP with Nested Pointers (+ Binary Search optimization) | Outer pointer j (0→n), inner pointer i (0→j). When nums[i] < nums[j], update dp[j] = max(dp[i]+1, dp[j]). Optimal: maintain a "tails" array and binary search the lower bound to overwrite | O(n²) (or O(n log n) optimized) | O(n) |

**Problem Statement:**
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

Example:
```
Input:  nums = [10,9,2,5,3,7,101,18]   ->  Output: 4   ([2,3,7,101])
```

**Solution:**
```python
"""
TC: O(n^2)
SC: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1] * n

        for j in range(1, n, 1):
            for i in range(j):
                if nums[i] < nums[j]:
                    arr[j] = max(arr[i]+1, arr[j])

        return max(arr)

"""

"""
Optimized Binary search solution (Trick)
TC: O(n log n)
SC: O(n)
"""
class Solution:

    def binary_search_lower_bound(self, arr, target):
        start, end = 0, len(arr) - 1

        while start <= end:
            mid = (start + end) // 2

            if arr[mid] < target:
                start = mid+1
            else:
                end = mid - 1

        return start


    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [nums[0]]


        for i in range(1, n, 1):
            num = nums[i]
            if arr[-1] < num:
                arr.append(num)
            else:
                index = self.binary_search_lower_bound(arr, num)
                arr[index] = num

        return len(arr)
```

---

## 2-D Dynamic Programming

#### 1. Unique Paths

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 2-D DP | Grid DP with Memoization | paths(i, j) = paths(i+1, j) + paths(i, j+1). Base: reaching bottom-right => 1, out of bounds => 0. Memoize each cell | O(m * n) | O(m * n) |

**Problem Statement:**
A robot is located at the top-left corner of an `m x n` grid and can only move down or right. Return the number of possible unique paths to the bottom-right corner.

Example:
```
Input:  m = 3, n = 7   ->  Output: 28
```

**Solution:**
```python
"""
TC: O(m * n)
SC: O(m * n) memo + O(m + n) recursion stack
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for j in range(n)] for i in range(m)]

        def get_unique_paths(i, j):
            if i >= m or j >= n:
                return 0

            if i == m-1 and j == n-1:
                return 1

            if not memo[i][j] == -1:
                return memo[i][j]

            memo[i][j] = get_unique_paths(i+1, j) + get_unique_paths(i, j+1)
            return memo[i][j]

        return get_unique_paths(0, 0)
```

---

#### 2. Longest Common Subsequence

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 2-D DP | Top-Down DP with Memoization | Start from both string ends. If chars match: 1 + solve remaining strings. If chars differ: skip char from either string, take maximum result | O(n*m) | O(n*m) |

**Problem Statement:**
Given two strings `text1` and `text2`, return the length of their longest common subsequence, or `0` if none exists.

Example:
```
Input:  text1 = "abcde", text2 = "ace"   ->  Output: 3   ("ace")
```

**Solution:**
```python
"""
TC: O(n * m)
SC: O(n * m) (memo) + O(n + m) recursion stack
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def lcs(index_1, index_2):
            if index_1 == -1 or index_2 == -1:
                return 0

            if dp[index_1][index_2] != -1:
                #print(dp[index_1][index_2])
                return dp[index_1][index_2]

            pick, not_pick = 0, 0
            # pick
            if text1[index_1] == text2[index_2]:
                pick = 1 + lcs(index_1 - 1, index_2 - 1)
            # not pick
            else:
                left_move_ahead = lcs(index_1 - 1, index_2)
                right_move_ahead = lcs(index_1, index_2 - 1)

                not_pick = max(left_move_ahead, right_move_ahead)

            dp[index_1][index_2] = max(pick, not_pick)
            return dp[index_1][index_2]

        lcs(n-1, m-1)

        return dp[n-1][m-1]
```

---

## Greedy

#### 1. Maximum Subarray

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Kadane's Algorithm | At each position decide: start new subarray OR extend current (nums[i] vs cur_sum + nums[i]) | O(n) | O(1) |

**Problem Statement:**
Given an integer array `nums`, find the contiguous subarray with the largest sum, and return its sum.

Example:
```
Input:  nums = [-2,1,-3,4,-1,2,1,-5,4]   ->  Output: 6   ([4,-1,2,1])
```

**Solution:**
```python
"""
TC: O(n)
SC: O(1)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        cur_sum = float("-inf")
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] > cur_sum + nums[i]:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]

            if cur_sum > max_sum:
                max_sum = cur_sum

            i += 1

        return max_sum
```

---

#### 2. Jump Game

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Furthest Reachable | Track furthest index reachable so far. If current index i > reachable, return False. Else reachable = max(reachable, i + nums[i]) | O(n) | O(1) |

**Problem Statement:**
Given an array of non-negative integers `nums`, where each element represents the max jump length from that position, determine if you can reach the last index starting from the first.

Example:
```
Input:  nums = [2,3,1,1,4]   ->  Output: true
Input:  nums = [3,2,1,0,4]   ->  Output: false
```

**Solution:**
```python
"""
TC: O(n)
SC: O(1)

Greedy: track the furthest index reachable so far. If the current index ever
exceeds reachable, we can't get there. Otherwise extend reachable = max(reachable, i + nums[i]).
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False

            reachable = max(reachable, nums[i] + i)

        return True
```

---

## Math & Geometry

#### 1. Rotate Image

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Math & Geometry | Transpose + Reverse Rows | Transpose the matrix (swap matrix[r][c] with matrix[c][r] for c<r), then reverse each row to get a 90° clockwise rotation | O(m * n) | O(1) |

**Problem Statement:**
Given an `n x n` 2D matrix representing an image, rotate the image by 90 degrees clockwise, in place.

Example:
```
Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]   ->  Output: [[7,4,1],[8,5,2],[9,6,3]]
```

**Solution:**
```python
"""
Time Complexity: O(m*n)
Space Complexity: O(1)

Intuition: If we observe that rotating a arrahy by 90 degree means transposing the matrix
and then reversing the rows
1 2
3 4

Transpose:
1 3
2 4
Reverse rows:
3 1
4 2
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        no_of_rows = len(matrix)
        no_of_cols = len(matrix[0])

        # Transpose the matrix
        for r in range(no_of_rows):
            for c in range(r):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # reverse each row of matrix to get the answer
        for r in range(no_of_rows):
            matrix[r].reverse()
```

---

#### 2. Spiral Matrix

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Math & Geometry | Directional Walk with Visited Grid | Walk in one of four directions (right -> bottom -> left -> top -> right), switching direction whenever the next cell is out of bounds or already visited | O(m * n) | O(m * n) |

**Problem Statement:**
Given an `m x n` matrix, return all elements of the matrix in spiral order.

Example:
```
Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]   ->  Output: [1,2,3,6,9,8,7,4,5]
```

**Solution:**
```python
"""
TC: O(m * n)
SC: O(m * n)
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        no_of_rows = len(matrix)
        no_of_cols = len(matrix[0])
        res = []
        next_dir = {
            "right": "bottom",
            "bottom": "left",
            "left": "top",
            "top": "right",
        }
        visited = [[False for _ in range(no_of_cols)] for _ in range(no_of_rows)]

        def move_spiral_path(r, c, path):
            if r < 0 or r >= no_of_rows or c < 0 or c >= no_of_cols or visited[r][c]:
                return

            visited[r][c] = True
            res.append(matrix[r][c])

            if path == "right":
                if c+1 >= no_of_cols or visited[r][c+1]:
                    next_row = r+1
                    next_col = c
                    next_path = next_dir[path]
                else:
                    next_row = r
                    next_col = c+1
                    next_path = path
            elif path == "bottom":
                if r+1 >= no_of_rows or visited[r+1][c]:
                    next_row = r
                    next_col = c-1
                    next_path = next_dir[path]
                else:
                    next_row = r+1
                    next_col = c
                    next_path = path
            elif path == "left":
                if c-1 < 0 or visited[r][c-1]:
                    next_row = r-1
                    next_col = c
                    next_path = next_dir[path]
                else:
                    next_row = r
                    next_col = c-1
                    next_path = path
            elif path == "top":
                if r-1 < 0 or visited[r-1][c]:
                    next_row = r
                    next_col = c+1
                    next_path = next_dir[path]
                else:
                    next_row = r-1
                    next_col = c
                    next_path = path

            move_spiral_path(next_row, next_col, next_path)

        move_spiral_path(0, 0, "right")
        return res
```

---

#### 3. Set Matrix Zeroes

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Math & Geometry | In-place Markers via First Row/Col | Use the matrix's own first row and first column as zero markers (with a separate flag for column 0), then zero out cells in a second pass | O(m * n) | O(1) |

**Problem Statement:**
Given an `m x n` matrix, if an element is 0, set its entire row and column to 0, in place.

Example:
```
Input:  matrix = [[1,1,1],[1,0,1],[1,1,1]]   ->  Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Solution:**
```python
from typing import List


"""
Time Complexity: O(m*n)
Space Complexity: O(m+n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Do not return anything, modify matrix in-place instead.
        rows  = set()
        cols = set()

        no_of_rows = len(matrix)
        no_of_cols = len(matrix[0])

        for r in range(no_of_rows):
            for c in range(no_of_cols):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in range(no_of_rows):
            for c in range(no_of_cols):
                if r in rows or c in cols:
                    matrix[r][c] = 0

        return matrix

"""
"""
Approach 2: We have just optmized above approach to use first row and col of the same matrix to
store the 0 reference instead of creating new two arrays row and col

Time Complexity: O(m*n)
Space Complexity: O(1)
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows  = set()
        cols = set()

        no_of_rows = len(matrix)
        no_of_cols = len(matrix[0])
        col_zero = 1

        for r in range(no_of_rows):
            for c in range(no_of_cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0

                    if c == 0:
                        col_zero = 0
                    else:
                        matrix[0][c] = 0

        for r in range(1, no_of_rows):
            for c in range(1, no_of_cols):
                if matrix[r][0] == 0:
                    matrix[r][c] = 0

                if matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for c in range(no_of_cols):
                matrix[0][c] = 0

        if col_zero == 0:
            for r in range(no_of_rows):
                matrix[r][0] = 0

        return matrix
```

---

## Bit Manipulation

#### 1. Number of 1 Bits

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Bit Manipulation | Bit Counting | Count set bits by checking n % 2, then right shift with n // 2 or n >> 1 | O(log n) | O(1) |

**Problem Statement:**
Given a positive integer `n`, write a function that returns the number of set bits in its binary representation (Hamming weight).

Example:
```
Input:  n = 11 (00000000000000000000000000001011)   ->  Output: 3
```

**Solution:**
```python
"""
TC: O(log n)
SC: O(1)
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n > 1:
            if n % 2:
                res += 1

            n = n // 2

        if n % 2:
            res += 1

        return res
```

---

#### 2. Counting Bits

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Bit Manipulation | Bit Counting | For each number 0 to n, count 1-bits using modulo and right shift operations | O(n log n) | O(1) |

**Problem Statement:**
Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (0 <= i <= n), `ans[i]` is the number of `1`'s in the binary representation of `i`.

Example:
```
Input:  n = 5   ->  Output: [0,1,1,2,1,2]
```

**Solution:**
```python
"""
TC: O(n log n)
SC: O(1) (excluding output)
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [-1] * (n+1)

        def get_one_count(n):
            res = 0
            while n:
                res += n % 2
                n = n >> 1

            return res

        for i in range(0, n+1):
            result[i] = get_one_count(i)

        return result
```

---

#### 3. Missing Number

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Bit Manipulation | XOR Trick | XOR all indices (0 to n) with all array values. Missing number will remain as XOR cancels out pairs | O(n) | O(1) |

**Problem Statement:**
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the one number in the range that is missing from the array.

Example:
```
Input:  nums = [3,0,1]   ->  Output: 2
```

**Solution:**
```python
"""
TC: O(n)
SC: O(1)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        """
        The idea is
        1. xor of same number cancels each other 5^5 =0 , 11^11=0
        2. xor of number x with 0 = x (as 1 ^ 0 =1 & 0^0 = 0)
        3. here all the numbers present in array will cancel out to 0 and finally that 0 ^ missing number will
           be left
        """
        xor_till_n = 0
        for num in range(n+1):
            xor_till_n = xor_till_n ^ num

        for num in nums:
            xor_till_n = xor_till_n ^ num

        return xor_till_n
```

---

#### 4. Reverse Bits

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Bit Manipulation | Bit-by-bit Reconstruction | Loop 32 times, shift result left then OR in last bit of n, right shift n each iteration | O(1) | O(1) |

**Problem Statement:**
Reverse the bits of a given 32-bit unsigned integer.

Example:
```
Input:  n = 00000010100101000001111010011100   ->  Output: 964176192 (00111001011110000010100101000000)
```

**Solution:**
```python
"""
TC: O(1) (fixed 32 iterations)
SC: O(1)
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            n_last_bit = n & 1
            res = res << 1
            res = (res | n_last_bit)

            n = n >> 1

        return res
```

---

#### 5. Sum of Two Integers

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Bit Manipulation | Bitwise Add (XOR + Carry) | XOR gives the sum without carry, AND+left-shift gives the carry; repeat until no carry remains, masking to 32 bits and converting back from two's complement if negative | O(1) | O(1) |

**Problem Statement:**
Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

Example:
```
Input:  a = 1, b = 2   ->  Output: 3
Input:  a = 2, b = 3   ->  Output: 5
```

**Solution:**
```python
"""
TC: O(1)
SC: O(1)
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 32) - 1

        while b:
            a, b = (a ^ b) & mask, ((a  & b) << 1) & mask

        return a if a < (1 << 31) else ~(a^mask)
```
