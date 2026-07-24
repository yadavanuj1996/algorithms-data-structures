# Striver Sheet — Detailed Solutions

Detailed walkthrough of each problem: problem statement, the key trick, and the full solution.

---

## A2Z DSA Course Problems

### Arrays

#### 1. Find Second Largest Element

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Array | Single Pass | Use two variables to track largest and second largest in one pass | O(n) | O(1) |

**Problem Statement:**
Given an array `Arr` of size `N`, print the second largest distinct element from the array. If the second largest element doesn't exist, return `-1`.

Constraints:
- `2 ≤ N ≤ 10^5`
- `1 ≤ Arr[i] ≤ 10^5`

Example:
```
Input:  N = 6, Arr[] = {12, 35, 1, 10, 34, 1}
Output: 34
Explanation: The largest element is 35 and the second largest distinct element is 34.
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

def secondLargest(arr, n):
    if (n < 2):
        return -1

    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    return second_large
```

---

#### 2. Check if Array is Sorted

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Array | Linear Scan | Compare each element with next element in single pass | O(n) | O(1) |

**Problem Statement:**
Given an array `nums`, return `true` if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return `false`. There may be duplicates in the original array. (LeetCode: *Check if Array Is Sorted and Rotated*)

Example:
```
Input:  nums = [3,4,5,1,2]   ->  Output: true   ([1,2,3,4,5] rotated by 3)
Input:  nums = [2,1,3,4]     ->  Output: false
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

class Solution:
    def check(self, nums: List[int]) -> bool:
        no_of_drops = 0

        if nums[-1] > nums[0]:
            no_of_drops += 1

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                no_of_drops += 1

                if no_of_drops > 1:
                    return False

        return True
```

---

#### 3. Remove Duplicates from Sorted Array

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Array | Two Pointers | Use slow pointer for unique position, fast pointer for scanning | O(n) | O(1) |

**Problem Statement:**
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place so each unique element appears only once, keeping relative order. Return `k`, the number of unique elements; the first `k` elements of `nums` must hold those unique values.

Example:
```
Input:  nums = [1,1,2]   ->  Output: 2, nums = [1,2,_]
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        for j in range(1, n):
            if not nums[i] == nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1
```

---

#### 4. Left Rotate Array by One

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Array | Temporary Variable | Store first element, shift all left, place first at end | O(n) | O(1) |

**Problem Statement:**
Given an integer array, rotate the array to the left by one position (the first element moves to the end).

Example:
```
Input:  [1,2,3,4,5]   ->  Output: [2,3,4,5,1]
```

**Solution:**
```python
# Time: O(N) | Space: O(1)
# (repo file solves the general rotate-by-k via slicing)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        while k > n:
            k = k - n

        nums[:] = nums[-k:n] + nums[0:-k]
```

---

#### 5. Left Rotate Array by D Places

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Array | Array Slicing | Use slice concatenation: arr = arr[d:] + arr[:d] | O(n) | O(n) |

**Problem Statement:**
Given an integer array `nums`, rotate the array by `k` steps, where `k` is non-negative.

Example:
```
Input:  nums = [1,2,3,4,5,6,7], k = 3   ->  Output: [5,6,7,1,2,3,4]
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        while k > n:
            k = k - n

        nums[:] = nums[-k:n] + nums[0:-k]
```

---

#### 6. Move Zeros to End

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Array | Two Pointers | First pointer tracks first zero, second finds next non-zero to swap | O(n) | O(1) |

**Problem Statement:**
Given an integer array `nums`, move all `0`s to the end while maintaining the relative order of the non-zero elements. Do it in-place without making a copy.

Example:
```
Input:  nums = [0,1,0,3,12]   ->  Output: [1,3,12,0,0]
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i, j = None, None

        # find the first zero: j sits on it, i scans from just after
        for ind in range(n):
            if nums[ind] == 0:
                j = ind
                i = j + 1
                break

        if i is None:
            return nums

        # j always points at the leftmost zero; swap in the next non-zero i finds
        while i < n:
            if not nums[i] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            i += 1
```

---

#### 7. Longest Subarray with Sum K

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Array | Sliding Window | Two pointers: expand right when sum < k, shrink left when sum > k | O(n) | O(1) |

**Problem Statement:**
Given an array `a` of non-negative integers and a value `k`, find the length of the longest contiguous subarray whose sum equals `k`.

Example:
```
Input:  a = [2,3,5,1,9], k = 10   ->  Output: 3   (subarray [2,3,5])
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

def longestSubarrayWithSumK(a: [int], k: int) -> int:
    i = 0
    j = 0
    curr_sum = a[0]
    result = 0
    size = len(a)
    while i < size and j < size and i <= j:
        if curr_sum == k:
            if j - i + 1 > result:
                result = j - i + 1
            j += 1
            if i < size and j < size:
                curr_sum = curr_sum + a[j]
        elif curr_sum < k:
            j += 1
            if j < size:
                curr_sum += a[j]
        elif curr_sum > k:
            i += 1
            if i < size:
                curr_sum -= a[i-1]

    return result
```

---

#### 8. Two Sum

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Array | Hash Map | For each number, calculate complement = target - current. Check if complement exists in hashmap. If yes, return indices. If no, store current number with its index | O(n) | O(n) |

**Problem Statement:**
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Exactly one solution exists and you may not use the same element twice.

Example:
```
Input:  nums = [2,7,11,15], target = 9   ->  Output: [0,1]
```

**Solution:**
```python
# Time: O(n) | Space: O(n)
# (repo file uses sort + two-pointer, then maps values back to original indices)
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

#### 9. Count Subarrays with Given Sum

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Array | Prefix Sum + Hash Map | Track running prefixSum. If (prefixSum - k) exists in hashmap, add its frequency to count. Store current prefixSum frequency in map | O(n) | O(n) |

**Problem Statement:**
Given an array of integers `nums` and an integer `k`, return the total number of contiguous subarrays whose sum equals `k`. (LeetCode: *Subarray Sum Equals K*)

Example:
```
Input:  nums = [1,2,3,1,1,1], k = 3   ->  Output: 3
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0                 # running prefix sum
        old_pre_sums = {0: 1}       # prefix-sum -> frequency
        count = 0
        for val in nums:
            pre_sum += val
            # a subarray ending here sums to k whenever (pre_sum - k) was seen before
            count += old_pre_sums[pre_sum - k] if pre_sum - k in old_pre_sums else 0
            old_pre_sums[pre_sum] = old_pre_sums.get(pre_sum, 0) + 1

        return count
```

---

#### 10. Pascal's Triangle

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Array | Mathematical Formula | For each row: start with 1, then calculate next element using formula: element = element * (row-col+1) / col. Build each row using previous calculations | O(n²) | O(n²) |

**Problem Statement:**
Given an integer `numRows`, return the first `numRows` of Pascal's triangle, where each number is the sum of the two numbers directly above it.

Example:
```
Input:  numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**Solution:**
```python
# Time: O(n^2) | Space: O(n^2)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for r in range(numRows):
            res.append([1])          # every row starts with 1
            ans = 1
            # build the rest of the row with the multiplicative formula
            for c in range(1, r+1):
                ans = ans * (r - c + 1)
                ans = ans // c
                res[r].append(ans)

        return res
```

---

### Binary Search

#### 1. Binary Search

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Binary Search | Divide & Conquer | Compare with mid, eliminate half search space each iteration | O(log n) | O(1) |

**Problem Statement:**
Given a sorted (ascending) array `nums` and an integer `target`, return the index of `target` if it exists, else `-1`. Must run in O(log n).

Example:
```
Input:  nums = [-1,0,3,5,9,12], target = 9   ->  Output: 4
```

**Solution:**
```python
# Time: O(log n) | Space: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.get_element_using_binary_serach(nums, target, 0, len(nums)-1)

    def get_element_using_binary_serach(self, nums, target, low, high):
        if not low <= high:
            return -1

        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.get_element_using_binary_serach(nums, target, mid+1, high)
        elif nums[mid] > target:
            return self.get_element_using_binary_serach(nums, target, low, mid-1)
```

---

#### 2. Lower Bound

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Binary Search | Modified Binary Search | Find smallest index where arr[i] >= x, update result when found | O(log n) | O(1) |

**Problem Statement:**
Given an array `arr` sorted in non-decreasing order and a number `x`, return the lower bound: the smallest index `idx` such that `arr[idx] >= x`. If all numbers are smaller than `x`, return `n` (array size). 0-based indexing.

Example:
```
Input:  arr = [1,2,2,3,3,5], x = 0   ->  Output: 0
```

**Solution:**
```python
# Time: O(log n) | Space: O(1)

def lowerBound(arr: [int], n: int, x: int) -> int:
    low = 0
    high = n - 1
    res = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        if arr[mid] >= x:
            res = mid            # candidate; keep searching left for a smaller index
            high = mid - 1
    return res
```

---

#### 3. Upper Bound

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Binary Search | Modified Binary Search | Find smallest index where arr[i] > x, similar to lower bound | O(log n) | O(1) |

**Problem Statement:**
Given a sorted array `arr` of `n` integers and an integer `x`, return the upper bound: the index of the first value strictly greater than `x`. If none exists, return `n`. 0-based indexing.

Example:
```
Input:  arr = [1,4,7,8,10], x = 7   ->  Output: 3
```

**Solution:**
```python
# Time: O(log n) | Space: O(1)

def upperBound(arr: [int], x: int, n: int) -> int:
    result = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            low = mid + 1
        else:
            result = mid          # first value > x so far; try to find an earlier one
            high = mid - 1
    return result
```

---

#### 4. Search Insert Position

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Binary Search | Lower Bound Variant | Use lower bound logic to find insertion position for target | O(log n) | O(1) |

**Problem Statement:**
Given a sorted array of distinct integers and a `target`, return the index if found; otherwise the index where it would be inserted to keep the array sorted. O(log n).

Example:
```
Input:  nums = [1,3,5,6], target = 5   ->  Output: 2
Input:  nums = [1,3,5,6], target = 2   ->  Output: 1
```

**Solution:**
```python
# Time: O(log n) | Space: O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        higher_bound = n

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                higher_bound = mid
                high = mid - 1
            else:
                return mid

        return higher_bound
```

---

#### 5. Find First/Last Occurrence

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Binary Search | Boundary Search | Use modified binary search to find leftmost and rightmost positions | O(log n) | O(1) |

**Problem Statement:**
Given an array `nums` sorted in non-decreasing order, find the starting and ending index of a given `target`. If not found, return `[-1, -1]`. (LeetCode: *Find First and Last Position of Element in Sorted Array*)

Example:
```
Input:  nums = [5,7,7,8,8,10], target = 8   ->  Output: [3,4]
Input:  nums = [5,7,7,8,8,10], target = 6   ->  Output: [-1,-1]
```

**Solution:**
```python
# Time: O(n) worst case (repo version expands linearly around a hit) | Space: O(1)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        low, high = 0, n-1
        res = [-1, -1]
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                temp_ind = mid
                while temp_ind < n and nums[temp_ind] == target:
                    res[1] = temp_ind
                    temp_ind += 1

                temp_ind = mid
                while temp_ind >= 0 and nums[temp_ind] == target:
                    res[0] = temp_ind
                    temp_ind -= 1

            if nums[mid] < target:
                low = mid + 1
            if nums[mid] >= target:
                high = mid - 1

        return res
```

---

#### 6. Single Element in Sorted Array

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Binary Search | Index Parity Check | Before single element: pairs start at even indices (0,2,4...). After single element: pairs start at odd indices. Check mid: if nums[mid] == nums[mid^1], single element is on right, else left | O(log n) | O(1) |

**Problem Statement:**
Given a sorted array where every element appears exactly twice except one that appears once, return the single element. Must run in O(log n) time, O(1) space.

Example:
```
Input:  nums = [1,1,2,3,3,4,4,8,8]   ->  Output: 2
Input:  nums = [3,3,7,7,10,11,11]    ->  Output: 10
```

**Solution:**
```python
# Time: O(log n) | Space: O(1)

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1 or not nums[0] == nums[1]:
            return nums[0]
        if not nums[n-1] == nums[n-2]:
            return nums[n-1]

        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2

            if not nums[mid] == nums[mid-1] and not nums[mid] == nums[mid+1]:
                return nums[mid]

            # even mid pairing with next, or odd mid pairing with prev => single is to the right
            if mid % 2 == 0 and nums[mid] == nums[mid+1]:
                low = mid + 1
            elif mid % 2 == 1 and nums[mid] == nums[mid-1]:
                low = mid + 1
            else:
                high = mid - 1
```

---

#### 7. Find Peak Element

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Binary Search | Slope Analysis | Compare nums[mid] with nums[mid+1]. If nums[mid] < nums[mid+1], peak is on right (upward slope), search right. Else peak is on left, search left | O(log n) | O(1) |

**Problem Statement:**
A peak element is strictly greater than its neighbors. Given `nums`, return the index of any peak. Imagine `nums[-1] = nums[n] = -∞`. Must run in O(log n).

Example:
```
Input:  nums = [1,2,3,1]         ->  Output: 2
Input:  nums = [1,2,1,3,5,6,4]   ->  Output: 5 (or 1)
```

**Solution:**
```python
# Time: O(log n) | Space: O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 1, n-2

        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid

            if nums[mid] > nums[mid+1]:
                high = mid - 1
            elif nums[mid] < nums[mid+1]:
                low = mid + 1
```

---

### Strings

#### 1. Remove Outermost Parentheses

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String | Counter Tracking | Skip first '(' and last ')' of each primitive group using counter | O(n) | O(n) |

**Problem Statement:**
Given a valid parentheses string `s`, split it into primitive parts and return `s` after removing the outermost parentheses of every primitive part.

Example:
```
Input:  s = "(()())(())(()(()))"   ->  Output: "()()()()(())"
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        result = ""

        for ch in s:
            if ch == "(" and count == 0:     # outer open -> skip
                count += 1
            elif ch == "(" and count > 0:
                result += ch
                count += 1
            elif ch == ")" and count == 1:   # outer close -> skip
                count -= 1
            elif ch == ")" and count > 1:
                result += ch
                count -= 1

        return result
```

---

#### 2. Reverse Words in String

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String | Two Pointers | Parse words from right to left, build result by reversing word order | O(n) | O(n) |

**Problem Statement:**
Given an input string `s`, reverse the order of the words. Collapse multiple spaces and trim leading/trailing spaces so the result has single spaces between words.

Example:
```
Input:  s = "the sky is blue"   ->  Output: "blue is sky the"
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        n = len(s)
        start, end = 0, 0
        while start < n:
            if s[start] == " ":
                start += 1
                end = start
                continue

            while not (end == n or s[end] == " "):
                end += 1

            res = s[start:end] + " " + res   # prepend each word
            start = end

        return res[:-1]
```

---

#### 3. Largest Odd Number in String

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String | Greedy | Find rightmost odd digit, return substring from start to that position | O(n) | O(1) |

**Problem Statement:**
Given a string `num` representing a large integer, return the largest-valued odd integer (as a string) that is a non-empty substring of `num`, or `""` if none exists.

Example:
```
Input:  num = "52"   ->  Output: "5"
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            # a number is odd iff its last digit is odd -> take prefix up to rightmost odd digit
            if int(num[i]) % 2 == 1:
                return num[0:i+1]

        return ""
```

---

#### 4. Longest Common Prefix

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String | Vertical Scanning | Compare characters column-wise across all strings until mismatch | O(m*n) | O(1) |

**Problem Statement:**
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return `""`.

Example:
```
Input:  strs = ["flower","flow","flight"]   ->  Output: "fl"
```

**Solution:**
```python
# Time: O(m*n) | Space: O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            fir_elem_char = strs[0][i]
            is_further_processing_req = True

            ind = 1
            while ind < len(strs):
                if i >= len(strs[ind]):
                    is_further_processing_req = False
                    break
                if not strs[ind][i] == fir_elem_char:
                    is_further_processing_req = False
                    break
                ind += 1

            if not is_further_processing_req:
                break
            else:
                result += fir_elem_char

        return result
```

---

#### 5. Rotate String

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String | String Concatenation | Check if goal exists in s+s (contains all possible rotations) | O(n) | O(n) |

**Problem Statement:**
Given two strings `s` and `goal`, return `true` if `s` can become `goal` after some number of left shifts (moving the leftmost char to the rightmost position).

Example:
```
Input:  s = "abcde", goal = "cdeab"   ->  Output: true
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) < len(s):
            return False

        s += s[:-1]          # s + s contains every rotation of s
        return goal in s
```

---

#### 6. Valid Anagram

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String | Frequency Count | Compare character frequency maps of both strings | O(n) | O(n) |

**Problem Statement:**
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s` (same characters, same counts), else `false`.

Example:
```
Input:  s = "anagram", t = "nagaram"   ->  Output: true
```

**Solution:**
```python
# Time: O(M+N) | Space: O(M+N)

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

#### 7. Reverse Every Word

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String | Split & Reverse | SPLIT string by spaces to get words array. For each word, reverse it character by character. JOIN all reversed words back with spaces | O(n) | O(n) |

**Problem Statement:**
Given an input string `s`, reverse the order of the words (same "Reverse Words in a String" problem; this repo variant scans from the right end and appends words in reversed order).

Example:
```
Input:  s = "the sky is blue"   ->  Output: "blue is sky the"
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        n = len(s)
        start, end = n-1, n-1
        for i in range(n-1, -1, -1):
            if start == end and s[i] == " ":
                start -= 1
                end = start
                continue

            if s[i] == " ":
                res += s[start+1:end+1] + " "
                end = start - 1

            start -= 1

        res += s[start+1:end+1]

        return res
```

---

### Linked Lists

#### 1. Reverse Linked List (Iterative)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Three Pointers | Use three pointers: prev=None, curr=head, next=curr.next. Set curr.next=prev, then move all three forward: prev=curr, curr=next, next=curr.next | O(n) | O(1) |

**Problem Statement:**
Given the head of a singly linked list, reverse the list and return the new head.

Example:
```
Input:  head = [1,2,3,4,5]   ->  Output: [5,4,3,2,1]
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = None
        second = head

        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp

        head = first
        return head
```

---

#### 2. Reverse Linked List (Recursive)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Recursion | Base case: if head.next is None, return head. Recursively reverse rest: newHead = reverse(head.next). Set head.next.next = head, head.next = None | O(n) | O(n) |

**Problem Statement:**
Given the head of a singly linked list, reverse the list recursively and return the new head.

Example:
```
Input:  head = [1,2,3,4,5]   ->  Output: [5,4,3,2,1]
```

**Solution:**
```python
# Time: O(N) | Space: O(N) recursion stack

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

#### 3. Detect Loop in Linked List

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Floyd's Cycle Detection | Use slow (moves 1 step) and fast (moves 2 steps) pointers. If they ever meet, there's a cycle. If fast reaches None, no cycle | O(n) | O(1) |

**Problem Statement:**
Given the head of a linked list, determine if it has a cycle. Return `true` if a cycle exists, otherwise `false`.

Example:
```
Input:  4 -> 3 -> 2 -> back to 3   ->  Output: true
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = head
        second = head

        while first and second.next and second.next.next:
            first = first.next
            second = second.next.next
            if first == second:
                return True

        return False
```

---

#### 4. Find Starting Point of Loop

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Floyd's Algorithm | First detect cycle using fast/slow. When they meet, reset slow to head. Move both slow and fast ONE step at a time until they meet again - that's the start! | O(n) | O(1) |

**Problem Statement:**
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return `null`. Do not modify the list.

Example:
```
Input:  4 -> 3 -> 2 -> 5 -> 8 -> back to 3   ->  Output: node with value 3
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while slow and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:                 # cycle detected
                slow = head
                while not slow == fast:      # both move 1 step to the cycle entry
                    slow = slow.next
                    fast = fast.next
                return slow

        return None
```

---

#### 5. Length of Loop

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Floyd's + Counting | First find where slow and fast meet in cycle. Keep one pointer fixed, move other until they meet again. Count steps = loop length | O(n) | O(1) |

**Problem Statement:**
Given a linked list whose last node may point to null or to some earlier node (forming a cycle), return the length of the cycle, or `0` if there is no cycle.

Example:
```
Input:  4 10 3 5, with tail linking to index 2   ->  Output: 3
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

def lengthOfLoop(head: Node) -> int:
    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:                 # meeting point inside cycle
            cycle_len = 1
            slow = slow.next
            while not slow == fast:      # walk one pointer around the cycle
                cycle_len += 1
                slow = slow.next
            return cycle_len

    return 0
```

---

#### 6. Check if Linked List is Palindrome

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Two Pointers + Reverse | Use slow/fast to find middle. Reverse second half. Compare first half with reversed second half node by node | O(n) | O(1) |

**Problem Statement:**
Given the head of a singly linked list, return `true` if it is a palindrome, otherwise `false`.

Example:
```
Input:  head = [1,2,2,1]   ->  Output: true
Input:  head = [1,2]       ->  Output: false
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

class Solution:
    def reverse_list(self, prev_node, cur_node):
        if not cur_node:
            return prev_node
        temp = cur_node.next
        cur_node.next = prev_node
        return reverse_list(cur_node, temp)

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # tortoise & hare to reach the middle
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half and compare with first half
        tail = self.reverse_list(None, slow)
        cur_node = head
        res = True
        while tail:
            if not cur_node.val == tail.val:
                res = False
                break
            tail = tail.next
            cur_node = cur_node.next
        # restore the list back
        self.reverse_list(None, tail)

        return res
```

---

#### 7. Segregate Odd Even Nodes

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Two Separate Lists | Keep odd and even pointers. Traverse: connect odd nodes together, even nodes together. Finally connect odd tail to even head | O(n) | O(1) |

**Problem Statement:**
Group all nodes at odd indices together followed by nodes at even indices (1st node is odd, 2nd is even, ...), keeping relative order within each group. O(1) space, O(n) time.

Example:
```
Input:  head = [1,2,3,4,5]   ->  Output: [1,3,5,2,4]
```

**Solution:**
```python
# Time: O(N) | Space: O(1)
# Note: repo names pointers with 0-index as "even"; result is identical.

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        even = head
        odd = head.next
        odd_head = head.next

        while odd and odd.next:
            even.next = even.next.next
            odd.next = odd.next.next
            even = even.next
            odd = odd.next

        even.next = odd_head
        return head
```

---

#### 8. Remove Nth Node from End

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Two Pointers with Gap | Move fast pointer n+1 steps ahead. Move both pointers until fast reaches end. slow.next is the node to remove. Set slow.next = slow.next.next | O(n) | O(1) |

**Problem Statement:**
Given the head of a linked list, remove the nth node from the end and return the head.

Example:
```
Input:  head = [1,2,3,4,5], n = 2   ->  Output: [1,2,3,5]
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next
        # removing the head itself
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

#### 9. Delete Middle Node

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Slow/Fast Pointers | Use slow (1 step) and fast (2 steps) pointers. Keep track of previous node of slow. When fast reaches end, delete slow node using prev.next = slow.next | O(n) | O(1) |

**Problem Statement:**
Delete the middle node (⌊n/2⌋th, 0-indexed) of a linked list and return the head.

Example:
```
Input:  head = [1,3,4,7,1,2,6]   ->  Output: [1,3,4,1,2,6]
Input:  head = [1,2,3,4]         ->  Output: [1,2,4]
```

**Solution:**
```python
# Time: O(N) | Space: O(1)
# Trick: start fast at head.next.next so slow lands just before the middle

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head
```

---

#### 10. Sort List with 0s, 1s, 2s

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Count & Reconstruct | First pass: count frequency of 0s, 1s, 2s. Second pass: overwrite node values with 0s first, then 1s, then 2s based on counts | O(n) | O(1) |

**Problem Statement:**
Given a linked list where each node's value is 0, 1, or 2, sort it in non-decreasing order and return the head.

Example:
```
Input:  1 -> 0 -> 2 -> 1 -> 0 -> 2 -> 1   ->  Output: 0 -> 0 -> 1 -> 1 -> 1 -> 2 -> 2
```

**Solution:**
```python
# Time: O(N) | Space: O(1)
# repo version builds three separate lists (0s, 1s, 2s) and links them

def sortList(head):
    cur_node = head
    zero_head = Node(-1); zero = zero_head
    one_head = Node(-1);  one = one_head
    two_head = Node(-1);  two = two_head

    while cur_node:
        if cur_node.data == 0:
            zero.next = Node(cur_node.data); zero = zero.next
        elif cur_node.data == 1:
            one.next = Node(cur_node.data);  one = one.next
        elif cur_node.data == 2:
            two.next = Node(cur_node.data);  two = two.next
        cur_node = cur_node.next

    zero_head = zero_head.next
    zero.next = one_head.next
    one.next = two_head.next

    return zero_head
```

---

#### 11. Intersection Point of Two Lists

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Length Difference | Calculate lengths of both lists. Move pointer of longer list by (length difference) steps. Then move both pointers together until they meet | O(n+m) | O(1) |

**Problem Statement:**
Given heads of two singly linked lists, return the node where they intersect, or `null` if they don't.

Example:
```
Input:  listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], intersect at 8   ->  Output: node 8
```

**Solution:**
```python
# Time: O(n+m) | Space: O(1)
# Trick: swap pointers to the other head on reaching end; they align at the intersection

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        cur_node_a = headA
        cur_node_b = headB

        while not cur_node_a == cur_node_b:
            cur_node_a = cur_node_a.next if cur_node_a else headB
            cur_node_b = cur_node_b.next if cur_node_b else headA

        return cur_node_a
```

---

#### 12. Add One to Number as Linked List

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Reverse + Add + Reverse | REVERSE the linked list first. Add 1 to head with carry propagation (9+1=10, carry=1). REVERSE back to get original order | O(n) | O(1) |

**Problem Statement:**
A positive integer is stored as a singly linked list of digits (most significant digit at head). Add 1 to the number and return the head.

Example:
```
Input:  1 -> 5 -> 2   ->  Output: 1 -> 5 -> 3
```

**Solution:**
```python
# Time: O(N) | Space: O(N) recursion stack
# repo version uses recursion to carry from the tail back up

def addOne(head: Node) -> Node:
    def add_one_ll(cur_node):
        if not cur_node:
            return 1
        carry = add_one_ll(cur_node.next)
        val = carry + cur_node.data
        cur_node.data = 0 if val > 9 else val
        carry = 1 if val > 9 else 0
        return carry

    carry = add_one_ll(head)
    if carry:
        head = Node(carry, head)      # extra leading digit (e.g. 999 -> 1000)

    return head
```

---

#### 13. Add Two Numbers as Linked Lists

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Simulation with Carry | Process both lists simultaneously. For each position: sum = l1.val + l2.val + carry. New digit = sum % 10, carry = sum // 10. Create new node for each digit | O(max(n,m)) | O(max(n,m)) |

**Problem Statement:**
Two non-empty linked lists represent two non-negative integers, digits stored in reverse order. Add the two numbers and return the sum as a linked list.

Example:
```
Input:  l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]   ->  Output: [8,9,9,9,0,0,0,1]
```

**Solution:**
```python
# Time: O(max(m,n)) | Space: O(max(m,n))

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        res_cur_node = None
        res_head = None

        while l1 or l2 or carry:
            sum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry = 1 if sum > 9 else 0
            sum = sum % 10 if sum > 9 else sum

            if not res_cur_node:
                res_cur_node = ListNode(sum)
                res_head = res_cur_node
            else:
                res_cur_node.next = ListNode(sum)
                res_cur_node = res_cur_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res_head
```

---

#### 14. Delete All Occurrences in DLL

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Doubly Linked List | Linear Traversal | For each node to delete: update prev.next = curr.next and curr.next.prev = prev. Handle head/tail edge cases separately | O(n) | O(1) |

**Problem Statement:**
Given a doubly linked list and a key `k`, delete all nodes whose data equals `k` and return the new head.

Example:
```
Input:  10 <-> 4 <-> 10 <-> 3 <-> 5 <-> 20 <-> 10, k = 10   ->  Output: 4 <-> 3 <-> 5 <-> 20
```

**Solution:**
```python
# Time: O(n) | Space: O(1)

def deleteAllOccurrences(head: Node, k: int) -> Node:
    cur_node = head

    while cur_node:
        if cur_node == head and cur_node.data == k:
            head = head.next
            cur_node = cur_node.next
            continue

        if cur_node.data == k:
            cur_node.prev.next = cur_node.next

        cur_node = cur_node.next

    return head
```

---

#### 15. Find Pairs with Given Sum in DLL

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Doubly Linked List | Two Pointers | Start with left=head, right=tail. If sum < target, move left forward. If sum > target, move right backward. If sum == target, found pair! | O(n) | O(1) |

**Problem Statement:**
Given a sorted doubly linked list of distinct positive integers and a number `k`, find all pairs with sum equal to `k`.

Example:
```
Input:  1 2 3 4 9, k = 5   ->  Output: [[1,4], [2,3]]
```

**Solution:**
```python
# Time: O(n) | Space: O(1) (excluding result)

def findPairs(head: Node, k: int) -> [[int]]:
    tail = head
    cur_node = head
    res = []
    while tail.next:
        tail = tail.next

    while cur_node != tail:
        val = cur_node.data + tail.data
        if val == k:
            res.append([cur_node.data, tail.data])
            tail = tail.prev
        elif val < k:
            cur_node = cur_node.next
        elif val > k:
            tail = tail.prev

    return res
```

---

### Recursion

#### 1. Pow(x, n)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Fast Exponentiation | If n is even: x^n = (x^(n/2))^2, if odd: x^n = x * x^(n-1) | O(log n) | O(log n) |

**Problem Statement:**
Implement `pow(x, n)` which calculates `x` raised to the power `n`.

Example:
```
Input:  x = 2.0, n = 10   ->  Output: 1024.0
Input:  x = 2.0, n = -2   ->  Output: 0.25
```

**Solution:**
```python
# Time: O(n) (repo version peels one power per call) | Space: O(n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            return x * pow(x, n-1)
        else:
            return pow(x, n+1) / x
```

---

#### 2. Count Good Numbers

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Modular Arithmetic | Use fast exponentiation with modulo, count even/odd positions separately | O(log n) | O(log n) |

**Problem Statement:**
A digit string is *good* if digits at even indices are even and digits at odd indices are prime (2,3,5,7). Return the number of good digit strings of length `n`, modulo 1e9+7.

Example:
```
Input:  n = 1   ->  Output: 5
Input:  n = 4   ->  Output: 400
```

**Solution:**
```python
# Time: O(log n) | Space: O(1)

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        no_of_even_digit = 5      # {0,2,4,6,8} at even positions
        no_of_prime_digit = 4     # {2,3,5,7}   at odd positions
        res = pow(no_of_even_digit, ((n+1)//2), MOD) * pow(no_of_prime_digit, (n//2), MOD)
        return res % MOD
```

---

#### 3. Sort Stack using Recursion

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Stack Operations | Remove top, sort remaining stack, insert top in sorted position | O(n²) | O(n) |

**Problem Statement:**
Given a stack `S`, sort it recursively (no looping allowed) into descending order.

Example:
```
Input:  [1,2,3,4]   ->  Output: [4,3,2,1]
```

**Solution:**
```python
# Time: O(N^2) | Space: O(N)

def sortStack(s):
    def fit_element(s, temp):
        if not s or s[-1] < temp:
            s.append(temp)
        else:
            s_temp = s.pop()
            fit_element(s, temp)
            s.append(s_temp)

    def sort_stack(s):
        if not s:
            return
        temp = s.pop()
        sort_stack(s)
        fit_element(s, temp)

    sort_stack(s)
    return s
```

---

#### 4. Reverse Stack using Recursion

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Stack Operations | Remove top, reverse remaining, insert at bottom of reversed stack | O(n²) | O(n) |

**Problem Statement:**
Reverse a given stack of `N` integers using recursion only, modifying the input stack in place (no extra data structure).

Example:
```
Input:  [1,2,3,4,5]   ->  Output: [5,4,3,2,1]
```

**Solution:**
```python
# Time: O(N^2) | Space: O(N)

def reverseStack(stack: List[int]) -> None:
    def fit_element(stack, element):
        if not stack:
            stack.append(element)
        else:
            temp = stack.pop()
            fit_element(stack, element)
            stack.append(temp)

    def reverse_stack(stack):
        if not stack:
            return
        temp = stack.pop()
        reverse_stack(stack)
        fit_element(stack, temp)     # push each popped element to the bottom

    reverse_stack(stack)
    return stack
```

---

#### 5. Generate All Binary Strings

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Pick / Not Pick | At each position: try both '0' and '1', backtrack after each choice | O(2^n) | O(n) |

**Problem Statement:**
Generate all binary strings of length `N` such that there are no consecutive `1`s.

Example:
```
Input:  N = 3   ->  Output: 000 001 010 100 101
```

**Solution:**
```python
# Time: O(2^n) | Space: O(n)

def generateString(N: int) -> List[str]:
    result = []
    def generate_string(index, sub_string, last=None):
        if index == N:
            result.append(sub_string)
            return
        # pick '1' only if previous char wasn't '1'
        if not last == 1:
            generate_string(index+1, sub_string+"1", 1)
        # pick '0'
        generate_string(index+1, sub_string+"0", 0)

    generate_string(0, "")
    return result
```

---

#### 6. Generate All Subsequences

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Pick / Not Pick | At each element: generate subsequences with and without current element | O(2^n) | O(n) |

**Problem Statement:**
Given an integer array `nums` of unique elements, return all possible subsets (the power set).

Example:
```
Input:  nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Solution:**
```python
# Time: O(2^n) | Space: O(n)

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def generateSubset(index, cur_set, nums):
            if index == len(nums):
                result.append(cur_set.copy())
                return
            # pick
            cur_set.append(nums[index])
            generateSubset(index+1, cur_set, nums)
            # unpick
            cur_set.remove(nums[index])
            generateSubset(index+1, cur_set, nums)

        generateSubset(0, [], nums)
        return result
```

---

#### 7. Count Subsequences with Sum K

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Pick / Not Pick + Count | Count valid combinations, return count instead of storing all | O(2^n) | O(n) |

**Problem Statement:**
Given an array `A` of size `N` and integer `K`, return all subarrays whose sum equals `K` (the repo file solves the return-all variant; an efficient prefix-sum method is used).

Example:
```
Input:  A = [1,2,3,1,1,1], K = 3   ->  subarrays [1,2], [3], [1,1,1]
```

**Solution:**
```python
# Time: O(N) | Space: O(N)  (prefix-sum approach)

def subarraysWithSumK(a: [int], k: int) -> [[int]]:
    pre_sum = 0
    old_pre_sums = {0: -1}
    result = []
    for i in range(len(a)):
        pre_sum += a[i]
        if pre_sum - k in old_pre_sums:
            result.append(a[old_pre_sums[pre_sum - k]+1:i+1])
        old_pre_sums[pre_sum] = i

    return result
```

---

#### 8. Check Subsequence with Sum K

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Pick / Not Pick + Early Stop | Return true on first valid subsequence found, early termination | O(2^n) | O(n) |

**Problem Statement:**
Given an array `A` of `N` integers, return `true` if there exists a subset summing to `K`, else `false`.

Example:
```
Input:  N=3, K=5, A=[1,2,3]   ->  Output: True   (subset [2,3])
```

**Solution:**
```python
# Time: O(n*k) | Space: O(n*k)  (memoized DP version in repo)

def isSubsetPresent(n: int, k: int, a: List[int]) -> bool:
    nums = a
    memo = [[-1]*(k+1)]*(n+1)

    def find(index, sum):
        if sum > k:
            return False
        if not memo[index][sum] == -1:
            return memo[index][sum]
        if index == n:
            memo[index][sum] = (sum == k)
            return memo[index][sum]
        # pick
        if find(index+1, sum+nums[index]):
            return True
        # unpick
        if find(index+1, sum):
            return True
        return False

    return find(0, 0)
```

---

#### 9. Combination Sum

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Unlimited Use | At each element: include unlimited times OR skip to next element | O(2^t) | O(target) |

**Problem Statement:**
Given distinct integers `candidates` and a `target`, return all unique combinations summing to `target`. The same number may be used unlimited times.

Example:
```
Input:  candidates = [2,3,6,7], target = 7   ->  Output: [[2,2,3],[7]]
```

**Solution:**
```python
# Time: O(2^t * k) | Space: O(k * x)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []

        def combination_sum(index, sum, arr):
            if index == n:
                if sum == 0:
                    result.append(arr.copy())
                return
            if sum < 0:
                return
            # pick (stay on same index -> unlimited use)
            combination_sum(index, sum - candidates[index], arr + [candidates[index]])
            # unpick (move to next index)
            combination_sum(index+1, sum, arr)

        combination_sum(0, target, [])
        return result
```

---

#### 10. Combination Sum II

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Skip Duplicates | Sort array, skip consecutive duplicates at same recursion level | O(2^n) | O(n) |

**Problem Statement:**
Given a collection `candidates` (may contain duplicates) and a `target`, return all unique combinations summing to `target`. Each number may be used at most once.

Example:
```
Input:  candidates = [2,5,2,1,2], target = 5   ->  Output: [[1,2,2],[5]]
```

**Solution:**
```python
# Time: O(2^n * k) | Space: O(k * x)

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        candidates.sort()
        def combination_sum_use_once(index, sum, arr):
            if index == n:
                if sum == 0:
                    result.append(arr.copy())
                return
            if sum < 0:
                return
            # pick
            combination_sum_use_once(index+1, sum - candidates[index], arr + [candidates[index]])
            # unpick, skipping duplicates so combos aren't repeated
            while index + 1 < n and candidates[index] == candidates[index+1]:
                index += 1
            combination_sum_use_once(index+1, sum, arr)

        combination_sum_use_once(0, target, [])
        return result
```

---

#### 11. Subset Sum

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Pick / Not Pick | Generate all possible subset sums using pick/not-pick pattern | O(2^n) | O(2^n) |

**Problem Statement:**
Given an array `nums` of `n` integers, return all subset sums in non-decreasing order.

Example:
```
Input:  nums = [1,2,3]   ->  Output: 0 1 2 3 3 4 5 6
```

**Solution:**
```python
# Time: O(2^n + 2^n log 2^n) | Space: O(2^n)

def subsetSum(num: List[int]) -> List[int]:
    n = len(num)
    result = []
    def sum_of_subset(index, num, sum):
        if index == n:
            result.append(sum)
            return
        # pick
        sum_of_subset(index+1, num, sum + num[index])
        # unpick
        sum_of_subset(index+1, num, sum)

    sum_of_subset(0, num, 0)
    result.sort()
    return result
```

---

#### 12. Subsets II

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Skip Duplicates | Sort array, skip duplicates at same level to avoid duplicate subsets | O(2^n) | O(2^n) |

**Problem Statement:**
Given an integer array `nums` that may contain duplicates, return all possible unique subsets (the power set).

Example:
```
Input:  nums = [1,2,2]   ->  Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**Solution:**
```python
# Time: O(2^n * k) | Space: O(2^n * k)

from copy import deepcopy

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        def get_subset_with_dup(index, arr):
            if index == n:
                result.append(deepcopy(arr))
                return
            # pick
            get_subset_with_dup(index+1, arr+[nums[index]])
            # unpick, skip duplicates so no duplicate subsets
            while index+1 < n and nums[index+1] == nums[index]:
                index += 1
            get_subset_with_dup(index+1, arr)

        get_subset_with_dup(0, [])
        return result
```

---

#### 13. Subsets III

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Pick / Not Pick | Generate all unique subsets using standard backtracking template | O(2^n) | O(2^n) |

**Problem Statement:**
(Repo file solves *Combination Sum III*) Find all combinations of `k` numbers from 1-9 (each used at most once) that sum to `n`.

Example:
```
Input:  k = 3, n = 9   ->  Output: [[1,2,6],[1,3,5],[2,3,4]]
```

**Solution:**
```python
# Time: O(2^9) | Space: O(k)

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        size = 10

        def combination_sum_3(index, sum, arr):
            if sum < 0 or len(arr) > k:
                return
            if index == size:
                if sum == 0 and len(arr) == k:
                    result.append(arr.copy())
                return
            # pick (index doubles as the digit value 1..9)
            combination_sum_3(index+1, sum - index, arr+[index])
            # unpick
            combination_sum_3(index+1, sum, arr)

        combination_sum_3(1, n, [])
        return result
```

---

#### 14. Letter Combinations

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Mapping + Backtracking | Map digits to letters, build combinations by trying all letter options | O(4^n) | O(n) |

**Problem Statement:**
Given a string of digits 2-9, return all possible letter combinations the number could represent (phone keypad mapping).

Example:
```
Input:  digits = "23"   ->  Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Solution:**
```python
# Time: O(4^n) | Space: O(n)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {
            2: ["a","b","c"], 3: ["d","e","f"], 4: ["g","h","i"],
            5: ["j","k","l"], 6: ["m","n","o"], 7: ["p","q","r","s"],
            8: ["t","u","v"], 9: ["w","x","y","z"]
        }
        n = len(digits)
        result = []

        def letter_combinations(index, cur_seq):
            if index == n:
                if cur_seq:                 # guard against empty input ""
                    result.append(cur_seq)
                return
            for item in phone_dict[int(digits[index])]:
                letter_combinations(index+1, cur_seq+item)

        letter_combinations(0, "")
        return result
```

---

#### 15. Palindrome Partitioning

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Backtracking | At each index i, try all substrings from i to end. If substring is palindrome, add to current partition and recurse on remaining string. Backtrack after each attempt | O(2^n * n) | O(n) |

**Problem Statement:**
Given a string `s`, partition it so that every substring is a palindrome, and return all possible partitionings.

Example:
```
Input:  s = "aab"   ->  Output: [["a","a","b"],["aa","b"]]
```

**Solution:**
```python
# Time: O(2^n * n) | Space: O(n)
# repo version inserts "|" cut markers and recurses on where to place them

class Solution:
    result = []

    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        if len(s) == 1:
            return [[s]]
        return self.valid_palindrome_partition(s[0:1]+"|"+s[1:])

    def is_valid_palindrome(self, arr: list) -> bool:
        for item in arr:
            if not item == item[::-1]:
                return False
        return True

    def valid_palindrome_partition(self, cur_seq: str):
        if cur_seq[-1] == "|":
            temp_arr = cur_seq[:len(cur_seq)-1].split("|")
            if self.is_valid_palindrome(temp_arr):
                self.result.append(temp_arr)
            return

        index = cur_seq.rfind("|")
        # place a cut / don't place a cut at the next position
        self.valid_palindrome_partition(cur_seq[0:index+2]+"|"+cur_seq[index+2:])
        self.valid_palindrome_partition(cur_seq[0:index]+cur_seq[index+1:index+2]+"|"+cur_seq[index+2:])
        return self.result
```

---

#### 16. Word Search

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | DFS + Backtracking | Start DFS from each cell. At each step: check bounds, if char matches, mark visited, explore 4 directions. BACKTRACK by unmarking visited before returning | O(m*n*4^L) | O(L) |

**Problem Statement:**
Given an `m x n` grid of characters and a word, return `true` if the word exists via sequentially adjacent (horizontal/vertical) cells, where a cell may not be reused.

Example:
```
Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

**Solution:**
```python
# Time: O(N*M*4^W) | Space: O(W + N*M)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        col_max = len(board[0])
        row_max = len(board)
        word_len = len(word)
        visited = [[False for _ in range(col_max)] for _ in range(row_max)]

        def find_word(row, col, cur_word_ind):
            if cur_word_ind == word_len:
                return True
            if (row < 0 or col < 0 or row >= row_max or col >= col_max
                    or visited[row][col] or word[cur_word_ind] != board[row][col]):
                return False

            visited[row][col] = True
            top = find_word(row-1, col, cur_word_ind+1)
            right = find_word(row, col+1, cur_word_ind+1)
            bottom = find_word(row+1, col, cur_word_ind+1)
            left = find_word(row, col-1, cur_word_ind+1)
            visited[row][col] = False       # backtrack

            return top or right or bottom or left

        for j in range(col_max):
            for i in range(row_max):
                if board[i][j] == word[0]:
                    if find_word(i, j, 0):
                        return True
        return False
```

---

#### 17. Rat in a Maze

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | DFS + Backtracking | From each cell, try 4 directions: Down, Left, Right, Up (DLRU order). Mark cell visited, recurse. If path found, add direction to result. BACKTRACK by unmarking | O(4^(m*n)) | O(m*n) |

**Problem Statement:**
Given an `N x N` maze (`1` = open, `0` = blocked) with a rat at `mat[0][0]`, find all paths to `mat[N-1][N-1]` using moves U/D/L/R.

Example:
```
Input:  3x3 maze [[1,1,1],[1,0,1],[1,1,1]]   ->  Output: ["DDRR","RRDD"]
```

**Solution:**
```python
# Time: O(4^(m*n)) | Space: O(m*n)

def ratMaze(matrix: List[List[int]]) -> List[str]:
    n = len(matrix)
    result = []
    visited = [[False for _ in range(n)] for _ in range(n)]

    def rat_maze(row, col, cur_seq):
        if row < 0 or col < 0 or row >= n or col >= n or not matrix[row][col] or visited[row][col]:
            return
        if row == n-1 and col == n-1:
            result.append(cur_seq)
            return

        visited[row][col] = True
        rat_maze(row-1, col, cur_seq+"U")
        rat_maze(row, col+1, cur_seq+"R")
        rat_maze(row+1, col, cur_seq+"D")
        rat_maze(row, col-1, cur_seq+"L")
        visited[row][col] = False           # backtrack

    rat_maze(0, 0, "")
    return result
```

---

### Greedy Algorithms

#### 1. Assign Cookies

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Two Pointers | Sort both arrays, assign smallest available cookie to smallest appetite | O(n log n) | O(1) |

**Problem Statement:**
Each child `i` has greed `g[i]`; each cookie `j` has size `s[j]`. A child is content if given a cookie with `s[j] >= g[i]`. Maximize the number of content children.

Example:
```
Input:  g = [1,2,3], s = [1,1]   ->  Output: 1
```

**Solution:**
```python
# Time: O(n log n) | Space: O(1)

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        cookie_size_len = len(s)
        i, j = 0, 0
        result = 0

        while i < len(g):
            greed = g[i]
            if j >= cookie_size_len:
                break
            if s[j] >= greed:
                j += 1
                result += 1
            else:
                j += 1
                continue
            i += 1

        return result
```

---

#### 2. Fractional Knapsack

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Value/Weight Ratio | Sort by value/weight ratio, pick highest ratio items first | O(n log n) | O(1) |

**Problem Statement:**
Given weights and values of `n` items and a knapsack capacity `W`, maximize total value. You may take fractions of items.

Example:
```
Input:  W = 50, items = [(60,10),(100,20),(120,30)]   ->  Output: 240.0
```

**Solution:**
```python
# Time: O(n log n) | Space: O(1)

class Solution:
    def sort_by_val_to_weight_ratio(self, element):
        return element[2]

    def fractionalknapsack(self, W, arr, n):
        w = W
        inp = []
        result = 0

        for item in arr:
            val_to_weight_ratio = item.value / item.weight
            inp.append((item.weight, item.value, val_to_weight_ratio))

        inp.sort(reverse=True, key=self.sort_by_val_to_weight_ratio)

        i = 0
        while w > 0 and i < len(inp):
            cur_weight, cur_value = inp[i][0], inp[i][1]
            if cur_weight <= w:
                result += cur_value
                w -= cur_weight
            else:
                result += (cur_value / cur_weight) * w      # take the fraction that fits
                w = 0
            i += 1

        return result
```

---

#### 3. Find Min Number of Coins

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Denomination Order | Start with largest denomination, use as many as possible, then smaller ones | O(d) | O(1) |

**Problem Statement:**
Given an infinite supply of coins `[1,2,5,10,20,50,100,500,1000]` and an amount `N`, return the coins (in decreasing order) making up `N` with the minimum count.

Example:
```
Input:  N = 13   ->  Output: [10, 2, 1]
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

def MinimumCoins(n: int) -> List[int]:
    currency = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    size = len(currency)
    result = []

    for i in range(size-1, -1, -1):          # largest denomination first
        while n > 0 and currency[i] <= n:
            n = n - currency[i]
            result.append(currency[i])

    return result
```

---

#### 4. Lemonade Change

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Change Management | Greedily use larger bills first (give change with $10 before $5) | O(n) | O(1) |

**Problem Statement:**
Customers pay for $5 lemonade with bills of 5/10/20 (in order). Starting with no change, return `true` if you can give correct change to every customer.

Example:
```
Input:  bills = [5,5,5,10,20]   ->  Output: true
Input:  bills = [5,5,10,10,20]  ->  Output: false
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        result = True
        bill_count_dict = {5: 0, 10: 0, 20: 0}

        for cur_bill in bills:
            bill_count_dict[cur_bill] = bill_count_dict[cur_bill] + 1

            if cur_bill == 10:
                if bill_count_dict[5] < 1:
                    result = False
                    break
                else:
                    bill_count_dict[5] -= 1
            elif cur_bill == 20:
                # prefer giving a 10+5 over three 5s
                if bill_count_dict[10] >= 1 and bill_count_dict[5] >= 1:
                    bill_count_dict[5] -= 1
                    bill_count_dict[10] -= 1
                elif bill_count_dict[5] >= 3:
                    bill_count_dict[5] -= 3
                else:
                    result = False
                    break

        return result
```

---

#### 5. Valid Parenthesis Checker

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Counter Balance | Use counter to track balance, never let it go negative | O(n) | O(n) |

**Problem Statement:**
Given a string of `'('`, `')'`, and `'*'` (where `*` can be `(`, `)`, or empty), return `true` if the string can be made valid.

Example:
```
Input:  s = "(*))"   ->  Output: true
Input:  s = "*((*"   ->  Output: false
```

**Solution:**
```python
# Time: O(N) | Space: O(N)  (stack of indices)

class Solution:
    def checkValidString(self, s: str) -> bool:
        left_par_index = []      # indices of '('
        start_par_index = []     # indices of '*'

        for i in range(len(s)):
            if s[i] == "*":
                start_par_index.append(i)
            elif s[i] == "(":
                left_par_index.append(i)
            elif s[i] == ")":
                if left_par_index:
                    left_par_index.pop()
                elif start_par_index:
                    start_par_index.pop()      # use a '*' as '('
                else:
                    return False

        # remaining '(' need a '*' to their right to act as ')'
        while left_par_index:
            if not start_par_index or start_par_index.pop() < left_par_index.pop():
                return False

        return True
```

---

#### 6. N Meetings in One Room

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Activity Selection | SORT by end time first! Create (start, end, index) tuples. Greedily pick meetings: select first meeting, then next meeting whose start >= current end | O(n log n) | O(n) |

**Problem Statement:**
Given `start[]` and `end[]` times of `N` meetings for a single room, return the maximum number of non-overlapping meetings that can be held.

Example:
```
Input:  start = [1,3,0,5,8,5], end = [2,4,6,7,9,9]   ->  Output: 4
```

**Solution:**
```python
# Time: O(n log n) | Space: O(n)

def maximumMeetings(start: List[int], end: List[int]) -> int:
    interval = []
    for i in range(len(start)):
        interval.append([start[i], end[i]])

    interval.sort(key=lambda x: x[0])
    if len(interval) == 1:
        return 1

    cur, next = 0, 1
    while next < len(interval):
        if interval[cur][0] <= interval[next][0] <= interval[cur][1]:
            # overlap: drop the one that ends later
            if interval[cur][1] <= interval[next][1]:
                interval.pop(next)
                continue
            else:
                interval.pop(cur)
                continue
        cur += 1
        next += 1

    return len(interval)
```

---

#### 7. Jump Game

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Reachability | Track farthest reachable index so far. At each position i, update farthest = max(farthest, i + nums[i]). If i > farthest, return False | O(n) | O(1) |

**Problem Statement:**
Each element `nums[i]` is your max jump length at index `i`, starting at index 0. Return `true` if you can reach the last index.

Example:
```
Input:  nums = [2,3,1,1,4]   ->  Output: true
Input:  nums = [3,2,1,0,4]   ->  Output: false
```

**Solution:**
```python
# Time: O(n) | Space: O(1)

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, nums[i] + i)
        return True
```

---

#### 8. Jump Game II

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Min Jumps | Track current jump range [l,r]. When reach end of range, increment jumps and extend range to farthest reachable. Count minimum jumps needed | O(n) | O(1) |

**Problem Statement:**
Each `nums[i]` is the max forward jump from index `i`. Return the minimum number of jumps to reach the last index (guaranteed reachable).

Example:
```
Input:  nums = [2,3,1,1,4]   ->  Output: 2
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        s_ind, e_ind = 0, 0
        steps = 0

        while e_ind < n-1:
            e_next_ind = -1
            # farthest we can reach from the current window [s_ind, e_ind]
            for i in range(s_ind, e_ind+1, 1):
                if nums[i] + i > e_next_ind:
                    e_next_ind = nums[i] + i
            s_ind = e_ind + 1
            e_ind = e_next_ind
            steps += 1

        return steps
```

---

#### 9. Min Platforms for Railway

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Event Sorting | SORT arrivals and departures separately! Use two pointers: when arrival < departure, need platform (increment), else release platform (decrement) | O(n log n) | O(1) |

**Problem Statement:**
Given arrival `AT[]` and departure `DT[]` times of trains, find the minimum number of platforms needed so that no train waits.

Example:
```
Input:  AT = [900,940,950,1100,1500,1800], DT = [910,1200,1120,1130,1900,2000]   ->  Output: 3
```

**Solution:**
```python
# Time: O(N log N) | Space: O(1)

def calculateMinPatforms(at, dt, n):
    at.sort()
    dt.sort()
    cur_plat, max_plat = 0, 0
    arr_index, dep_index = 0, 0

    while arr_index < n:
        # release platforms for every train that departed before this arrival
        while at[arr_index] > dt[dep_index]:
            cur_plat -= 1
            dep_index += 1
        cur_plat += 1
        max_plat = cur_plat if cur_plat > max_plat else max_plat
        arr_index += 1

    return max_plat
```

---

#### 10. Job Sequencing Problem

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Deadline Sorting | SORT by profit descending! For each job, place at latest possible slot before deadline. Use boolean array to track occupied slots | O(n²) | O(n) |

**Problem Statement:**
Each job has an id, deadline, and profit; each job takes 1 unit of time and only one job runs at a time. Maximize total profit and count jobs done, scheduling each job before its deadline.

Example:
```
Input:  jobs = [[1,2,30],[2,2,40],[3,1,10],[4,1,10]]   ->  Output: [2, 70]
```

**Solution:**
```python
# Time: O(N log N) + O(N*M) | Space: O(M)

def jobScheduling(jobs):
    jobs.sort(key=lambda arr: arr[2], reverse=True)      # highest profit first

    max_deadline = -1
    job_count = 0
    profit = 0
    for item in jobs:
        max_deadline = max(max_deadline, item[1])

    deadline_arr = [False] * (max_deadline + 1)

    for item in jobs:
        deadline_time = item[1]
        # place the job in the latest free slot before its deadline
        while deadline_time > 0:
            if not deadline_arr[deadline_time]:
                deadline_arr[deadline_time] = True
                job_count += 1
                profit += item[2]
                break
            deadline_time -= 1

    return [job_count, profit]
```

---

#### 11. Candy Distribution

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Two Pass | Two passes needed! Left→Right: if rating[i] > rating[i-1], candy[i] = candy[i-1] + 1. Right→Left: if rating[i] > rating[i+1], candy[i] = max(candy[i], candy[i+1] + 1) | O(n) | O(n) |

**Problem Statement:**
`n` children stand in a line with a rating each. Every child gets ≥1 candy, and a child with a higher rating than a neighbor must get more candies. Return the minimum total candies.

Example:
```
Input:  ratings = [1,2,2]   ->  Output: 4
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy_arr = [1] * n

        # left to right: satisfy the left neighbor
        for i in range(1, n):
            if ratings[i-1] < ratings[i] and candy_arr[i] < candy_arr[i-1] + 1:
                candy_arr[i] = candy_arr[i-1] + 1

        # right to left: satisfy the right neighbor
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and candy_arr[i] < candy_arr[i+1] + 1:
                candy_arr[i] = candy_arr[i+1] + 1

        return sum(candy_arr)
```

---

#### 12. Insert Interval

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Merge Logic | Three phases: 1) Add all intervals ending before new interval starts 2) Merge all overlapping intervals with new interval 3) Add remaining intervals | O(n) | O(n) |

**Problem Statement:**
Given sorted non-overlapping `intervals` and a `newInterval`, insert it and merge if necessary so the result stays sorted and non-overlapping.

Example:
```
Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

**Solution:**
```python
# Time: O(N log N) | Space: O(N)
# repo version appends the new interval, re-sorts, then merges

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        size = len(intervals)
        result = []

        current, next = 0, 1
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

#### 13. Merge Intervals

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Sort + Merge | SORT by start time first! Iterate through sorted intervals: if current start <= previous end, merge (update end to max). Else add previous, start new interval | O(n log n) | O(n) |

**Problem Statement:**
Given an array of `intervals`, merge all overlapping intervals and return the non-overlapping set covering all input intervals.

Example:
```
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]   ->  Output: [[1,6],[8,10],[15,18]]
```

**Solution:**
```python
# Time: O(N log N) | Space: O(N)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        size = len(intervals)
        result = []

        current, next = 0, 1
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

#### 14. Non-overlapping Intervals

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Activity Selection | SORT by end time! Count overlaps: if current start < previous end, increment removal count (keep earlier ending). Else update previous end | O(n log n) | O(1) |

**Problem Statement:**
Given an array of `intervals`, return the minimum number of intervals you must remove so the rest are non-overlapping.

Example:
```
Input:  intervals = [[1,2],[2,3],[3,4],[1,3]]   ->  Output: 1
```

**Solution:**
```python
# Time: O(N log N) | Space: O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])         # sort by end time
        res, ind = 0, 0

        while ind < len(intervals)-1:
            cur_interval_end = intervals[ind][1]
            next_interval_start = intervals[ind+1][0]
            if next_interval_start < cur_interval_end:
                intervals.pop(ind+1)               # remove the later-ending overlap
                res += 1
                continue
            ind += 1

        return res
```

---

### Binary Trees

#### 1. Preorder Traversal

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Tree Traversal | Root-Left-Right | Process root first, then recursively traverse left and right | O(n) | O(h) |

**Problem Statement:**
Given the root of a binary tree, return the preorder (root → left → right) traversal of its nodes' values.

**Solution:**
```python
# Time: O(n) | Space: O(h)

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.preOrder(root, [])

    def preOrder(self, root, result):
        if not root:
            return
        result.append(root.val)
        self.preOrder(root.left, result)
        self.preOrder(root.right, result)
        return result
```

---

#### 2. Inorder Traversal

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Tree Traversal | Left-Root-Right | Traverse left, process root, traverse right (gives sorted order for BST) | O(n) | O(h) |

**Problem Statement:**
Given the root of a binary tree, return the inorder (left → root → right) traversal of its nodes' values.

**Solution:**
```python
# Time: O(n) | Space: O(h)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inOrder(root, [])

    def inOrder(self, root, result):
        if not root:
            return
        self.inOrder(root.left, result)
        result.append(root.val)
        self.inOrder(root.right, result)
        return result
```

---

#### 3. Postorder Traversal

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Tree Traversal | Left-Right-Root | Process children before parent, useful for deletion/cleanup operations | O(n) | O(h) |

**Problem Statement:**
Given the root of a binary tree, return the postorder (left → right → root) traversal of its nodes' values.

**Solution:**
```python
# Time: O(n) | Space: O(h)

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postOrder(root, [])

    def postOrder(self, root, result):
        if not root:
            return
        self.postOrder(root.left, result)
        self.postOrder(root.right, result)
        result.append(root.val)
        return result
```

---

### Binary Search Trees

#### 1. Search in BST

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| BST Operations | Binary Search Property | Go left if target < node.val, right if target > node.val | O(log n) | O(1) |

**Problem Statement:**
Given the root of a BST and a value `val`, return the subtree rooted at the node whose value equals `val`, or `null` if not present.

Example:
```
Input:  root = [4,2,7,1,3], val = 2   ->  Output: [2,1,3]
```

**Solution:**
```python
# Time: O(log n) | Space: O(1)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if node.val < val:
                node = node.right
            elif node.val > val:
                node = node.left
            else:
                break
        return node
```

---

#### 2. Min Value in BST

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| BST Properties | Leftmost Node | Keep going left until you reach the leftmost node (smallest value) | O(log n) | O(1) |

**Problem Statement:**
Given a BST, find the minimum value in it (all values are unique).

Example:
```
Input:  6 4 7 2 5   ->  Output: 2
```

**Solution:**
```python
# Time: O(n) worst (skewed) | Space: O(1)

def minVal(root):
    if not root:
        return -1
    node = root
    while node.left:          # smallest value is the leftmost node
        node = node.left
    return node.data
```

---

#### 3. Ceil in BST

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| BST Operations | Lower Bound | Track smallest value >= target while traversing using BST property | O(log n) | O(1) |

**Problem Statement:**
Given a BST and an integer `x`, return the ceil of `x`: the smallest value in the tree ≥ `x` (or `-1` if none).

Example:
```
Input:  tree with values {2,5,6,7,8,10}, x = 4   ->  Output: 5
```

**Solution:**
```python
# Time: O(log n) | Space: O(1)

def findCeil(root, x):
    ceil = -1
    node = root
    while node:
        if node.data == x:
            return node.data
        if node.data > x:
            ceil = node.data      # candidate ceil, look left for a smaller valid one
            node = node.left
        else:
            node = node.right
    return ceil
```

---

#### 4. Insert Node in BST

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| BST Operations | Recursive Insertion | Find correct position using BST property, create new leaf node | O(log n) | O(log n) |

**Problem Statement:**
Given the root of a BST and a value `val` (not already present), insert it and return the root.

Example:
```
Input:  root = [40,20,60,10,30,50,70], val = 25   ->  Output: 25 inserted under 30's left
```

**Solution:**
```python
# Time: O(log n) | Space: O(1)

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        if not node:
            root = TreeNode(val)

        while node:
            if node.val < val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
            else:
                if node.val > val:
                    if node.left:
                        node = node.left
                    else:
                        node.left = TreeNode(val)
                        break

        return root
```

---

#### 5. Delete Node in BST

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| BST Operations | Case Analysis | 3 cases: no child (remove), 1 child (replace), 2 children (inorder successor) | O(log n) | O(log n) |

**Problem Statement:**
Given the root of a BST and a `key`, delete the node with that key and return the (possibly updated) root.

Example:
```
Input:  root = [5,3,6,2,4,null,7], key = 3   ->  Output: [5,4,6,2,null,null,7]
```

**Solution:**
```python
# Time: O(log n) balanced / O(n) skewed | Space: O(log n)

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min_val_bst(node):
            while node.left:
                node = node.left
            return node

        def delete_node_bst(cur_node, key):
            if not cur_node:
                return None
            if key < cur_node.val:
                cur_node.left = delete_node_bst(cur_node.left, key)
            elif key > cur_node.val:
                cur_node.right = delete_node_bst(cur_node.right, key)
            else:
                # 0 or 1 child
                if not cur_node.left:
                    return cur_node.right
                elif not cur_node.right:
                    return cur_node.left
                # 2 children: replace with inorder successor
                temp = find_min_val_bst(cur_node.right)
                cur_node.val = temp.val
                cur_node.right = delete_node_bst(cur_node.right, temp.val)
            return cur_node

        return delete_node_bst(root, key)
```

---

#### 6. Kth Smallest Element

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| BST Properties | Inorder Traversal | Inorder gives sorted order, return kth element during traversal | O(k) | O(log n) |

**Problem Statement:**
Given the root of a BST and integer `k`, return the kth smallest value (1-indexed).

Example:
```
Input:  root = [5,3,6,2,4,null,null,1], k = 3   ->  Output: 3
```

**Solution:**
```python
# Time: O(n) | Space: O(n)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def pre_order_traversal(node, res=[]):
            if not node:
                return
            pre_order_traversal(node.left, res)   # inorder -> sorted values
            res.append(node.val)
            pre_order_traversal(node.right, res)
            return res

        res = pre_order_traversal(root)
        return res[k-1]
```

---

#### 7. Validate BST

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| BST Properties | Range Validation | Each node must be within (min, max) range, update range recursively | O(n) | O(log n) |

**Problem Statement:**
Given the root of a binary tree, determine if it is a valid BST (left subtree < node < right subtree, recursively).

Example:
```
Input:  root = [5,1,4,null,null,3,6]   ->  Output: false
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

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

#### 8. LCA in BST

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| BST Properties | Path Splitting | First node where paths to p and q split (one goes left, other right) | O(log n) | O(1) |

**Problem Statement:**
Given a BST and two nodes `p` and `q`, return their lowest common ancestor (a node can be a descendant of itself).

Example:
```
Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4   ->  Output: 2
```

**Solution:**
```python
# Time: O(H) | Space: O(H)

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if p.val > q.val:
            p, q = q, p

        def get_common_ancestor(node):
            if p.val < node.val and q.val < node.val:
                return get_common_ancestor(node.left)
            elif p.val > node.val and q.val > node.val:
                return get_common_ancestor(node.right)
            # paths split here (or a node equals p/q) -> this is the LCA
            return node

        return get_common_ancestor(root)
```

---

### Graphs

**Basic Traversals**

#### 1. BFS Traversal

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Graph Traversal | Level-order | Use queue, mark visited before adding to avoid re-processing | O(V+E) | O(V) |

**Problem Statement:**
Given an adjacency list of a graph with `n` vertices, return the Breadth-First traversal starting from vertex 0.

Example:
```
Input:  adj = [[1,2,3],[2],[],[]]   ->  Output: [0,1,2,3]
```

**Solution:**
```python
# Time: O(N + 2E) | Space: O(N)

from collections import deque

def bfsTraversal(n: int, adj: List[List[int]]) -> List[int]:
    dq = deque()
    visited_nodes = [0] * n
    res = []
    dq.append(0)

    while dq:
        node = dq.popleft()
        if not visited_nodes[node]:
            visited_nodes[node] = 1
            res.append(node)
            for adjacent_node in adj[node]:
                dq.append(adjacent_node)

    return res
```

---

#### 2. DFS Traversal

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Graph Traversal | Depth-first | Use recursion or stack, mark visited during processing | O(V+E) | O(V) |

**Problem Statement:**
Given a connected undirected graph, perform a Depth First Traversal starting from vertex 0.

Example:
```
Input:  V = 5, adj = [[2,3,1],[0],[0,4],[0],[2]]   ->  Output: [0,2,4,3,1]
```

**Solution:**
```python
# Time: O(V + 2E) | Space: O(V)

class Solution:
    def dfsOfGraph(self, V, adj):
        visited_nodes = [0] * V
        result = []

        def dfs(cur_node):
            if not visited_nodes[cur_node]:
                visited_nodes[cur_node] = 1
                result.append(cur_node)
                for adj_node in adj[cur_node]:
                    dfs(adj_node)

        for node in range(V):
            if not visited_nodes[node]:
                dfs(node)

        return result
```

---

#### 3. Connected Components

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Graph Traversal | DFS/BFS | Run DFS/BFS from each unvisited node, count number of calls | O(V+E) | O(V) |

**Problem Statement:**
Given a graph, count and traverse its connected components by running DFS from each unvisited node (each fresh DFS call marks one new component).

**Solution:**
```python
# Time: O(V + E) | Space: O(V)

class Solution:
    def dfsOfGraph(self, V, adj):
        visited_nodes = [0] * V
        total_dis_comp = 0
        result = []

        def dfs(cur_node):
            if not visited_nodes[cur_node]:
                visited_nodes[cur_node] = 1
                result.append(cur_node)
                for adj_node in adj[cur_node]:
                    dfs(adj_node)

        for node in range(V):
            if not visited_nodes[node]:
                total_dis_comp += 1      # each new DFS root = one component
                dfs(node)

        return result
```

---

#### 4. Number of Provinces

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Connected Components | Union-Find/DFS | Each province is a connected component in adjacency matrix | O(V²) | O(V) |

**Problem Statement:**
Given an `n x n` matrix `isConnected` (1 = directly connected), return the number of provinces (groups of directly/indirectly connected cities).

Example:
```
Input:  isConnected = [[1,1,0],[1,1,0],[0,0,1]]   ->  Output: 2
```

**Solution:**
```python
# Time: O(N^2) | Space: O(N)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        no_of_nodes = len(isConnected)
        is_visited = [False] * no_of_nodes

        def dfs(cur_node):
            if is_visited[cur_node]:
                return
            is_visited[cur_node] = True
            for adj_node in range(no_of_nodes):
                if isConnected[cur_node][adj_node] == 1:
                    dfs(adj_node)

        no_of_provinces = 0
        for cur_city_node in range(no_of_nodes):
            if not is_visited[cur_city_node]:
                no_of_provinces += 1
                dfs(cur_city_node)

        return no_of_provinces
```

---

#### 4.1 Connected Components (Alt)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Connected Components | DFS/BFS | Alternative implementation for counting connected components | O(V+E) | O(V) |

**Problem Statement:**
Given `n` cities and an `n x n` roads matrix, count the number of provinces (connected components). Alternative implementation using an adjacency-matrix DFS.

Example:
```
Input:  roads = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]   ->  Output: 2
```

**Solution:**
```python
# Time: O(V + E) | Space: O(V)

def findNumOfProvinces(roads: List[List[int]], n: int) -> int:
    res = 0
    visited_nodes = [0]*n

    def dfs(node):
        if visited_nodes[node] == 1:
            return
        visited_nodes[node] = 1
        for connecting_node in range(len(roads[node])):
            if roads[node][connecting_node] == 1:
                dfs(connecting_node)

    for cur_node in range(n):
        if visited_nodes[cur_node] == 0:
            res += 1
            dfs(cur_node)

    return res
```

---

**BFS/DFS Problems**

#### 5. Rotten Oranges

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Multi-source BFS | BFS with Time | Add ALL rotten oranges to queue initially with time=0. BFS level by level: for each level, rot adjacent fresh oranges and add to next level with time+1 | O(m*n) | O(m*n) |

**Problem Statement:**
In an `m x n` grid (0 = empty, 1 = fresh, 2 = rotten), every minute a fresh orange adjacent to a rotten one rots. Return the minutes until no fresh orange remains, or `-1` if impossible.

Example:
```
Input:  grid = [[2,1,1],[1,1,0],[0,1,1]]   ->  Output: 4
```

**Solution:**
```python
# Time: O(m*n) | Space: O(m*n)

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        m = len(grid)
        n = len(grid[0])
        visited = [[False if grid[i][j] == 1 else True for j in range(n)] for i in range(m)]
        total_oranges = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    total_oranges += 1
                    dq.append((i, j, 0))
                if grid[i][j] == 1:
                    total_oranges += 1

        cur_time = 0
        total_queue_items = 0

        while dq:
            i, j, time = dq.popleft()
            cur_time = time
            total_queue_items += 1
            self.add_fresh_tomatoes_queue(dq, i-1, j, visited, m, n, cur_time)
            self.add_fresh_tomatoes_queue(dq, i, j+1, visited, m, n, cur_time)
            self.add_fresh_tomatoes_queue(dq, i+1, j, visited, m, n, cur_time)
            self.add_fresh_tomatoes_queue(dq, i, j-1, visited, m, n, cur_time)

        return cur_time if total_oranges == total_queue_items else -1

    def add_fresh_tomatoes_queue(self, dq, row_index, col_index, visited, m, n, cur_time):
        if 0 <= row_index < m and 0 <= col_index < n and not visited[row_index][col_index]:
            visited[row_index][col_index] = True
            dq.append((row_index, col_index, cur_time+1))
```

---

#### 6. Flood Fill

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| DFS/BFS | Color Change | DFS/BFS to change connected pixels of same color to new color | O(m*n) | O(m*n) |

**Problem Statement:**
Given an image grid, a start pixel `(sr, sc)`, and a `color`, flood fill all 4-directionally connected pixels of the same starting color with the new color.

Example:
```
Input:  image = [[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2   ->  Output: [[2,2,2],[2,2,0],[2,0,1]]
```

**Solution:**
```python
# Time: O(4 * N * M) | Space: O(N*M)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        total_rows = len(image)
        total_cols = len(image[0])

        def fill_color(row_no, col_no, prev_color=None):
            if row_no < 0 or row_no >= total_rows or col_no < 0 or col_no >= total_cols:
                return
            if (prev_color is not None and not prev_color == image[row_no][col_no]) or \
                    image[row_no][col_no] == color:
                return

            old_color = image[row_no][col_no]
            image[row_no][col_no] = color
            fill_color(row_no-1, col_no, old_color)
            fill_color(row_no, col_no+1, old_color)
            fill_color(row_no+1, col_no, old_color)
            fill_color(row_no, col_no-1, old_color)

        fill_color(sr, sc, None)
        return image
```

---

#### 7. Cycle Detection (Undirected BFS)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Cycle Detection | BFS with Parent | If adjacent node is visited AND not parent, cycle found | O(V+E) | O(V) |

**Problem Statement:**
Given an undirected graph with `V` vertices and `E` edges (no self-loops), return `true` if it contains a cycle. BFS variant carries each node's parent in the queue.

Example:
```
Input:  4 vertices, edges 0-1,1-2,2-3,3-0   ->  Output: True
```

**Solution:**
```python
# Time: O(N + 2E) | Space: O(N)

from collections import deque

def bfs(node, parent_node, node_graph, visited_nodes):
    dq = deque()
    dq.append((node, parent_node))
    while dq:
        cur_node, parent_node = dq[0][0], dq[0][1]
        if not visited_nodes[cur_node]:
            visited_nodes[cur_node] = 1
            dq.popleft()
            for adj_node in node_graph[cur_node]:
                if not adj_node == parent_node and not adj_node == cur_node:
                    dq.append((adj_node, cur_node))
        else:
            return True          # revisiting a non-parent node -> cycle
    return False
```

---

#### 8. Cycle Detection (Undirected DFS)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Cycle Detection | DFS with Parent | If adjacent node is visited AND not parent, cycle found | O(V+E) | O(V) |

**Problem Statement:**
Given an undirected graph with `V` vertices and `E` edges (no self-loops), return `true` if it contains a cycle. DFS variant passes the parent down the recursion.

Example:
```
Input:  4 vertices, edges 0-1,1-2,2-3,3-0   ->  Output: True
```

**Solution:**
```python
# Time: O(N + 2E) | Space: O(N)

def dfs(node, parent_node, node_graph, visited_nodes):
    res = False
    if not visited_nodes[node]:
        visited_nodes[node] = 1
        for adj_node in node_graph[node]:
            if not adj_node == parent_node and not adj_node == node:
                if dfs(adj_node, node, node_graph, visited_nodes):
                    res = True
                    break
    else:
        res = True               # already visited & not parent -> cycle
    return res
```

---

#### 9. 0-1 Matrix

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Multi-source BFS | Distance Calculation | BFS from all 0s simultaneously to find distance to nearest 0 | O(m*n) | O(m*n) |

**Problem Statement:**
Given a binary matrix `mat`, return a matrix where each cell holds its distance to the nearest `0` (adjacent-cell distance = 1).

Example:
```
Input:  mat = [[0,0,0],[0,1,0],[1,1,1]]   ->  Output: [[0,0,0],[0,1,0],[1,2,1]]
```

**Solution:**
```python
# Time: O(M*N) | Space: O(M*N)

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        total_rows = len(mat)
        total_cols = len(mat[0])
        queue = []
        is_visited = [[False]*total_cols for _ in range(total_rows)]
        result = [[None]*total_cols for _ in range(total_rows)]

        for r in range(total_rows):
            for c in range(total_cols):
                if mat[r][c] == 0:              # all zeros are BFS sources
                    queue.append((r, c, 0))
                    is_visited[r][c] = True

        def add_adj_element(row, col, steps):
            if row < 0 or row >= total_rows or col < 0 or col >= total_cols or is_visited[row][col]:
                return
            is_visited[row][col] = True
            queue.append((row, col, steps))

        while queue:
            row, col, steps = queue.pop(0)
            result[row][col] = steps
            add_adj_element(row-1, col, steps+1)
            add_adj_element(row, col+1, steps+1)
            add_adj_element(row+1, col, steps+1)
            add_adj_element(row, col-1, steps+1)

        return result
```

---

#### 10. Surrounded Regions

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| DFS/BFS | Border Traversal | Mark boundary-connected 'O's as safe, convert rest to 'X' | O(m*n) | O(m*n) |

**Problem Statement:**
Given an `m x n` board of `'X'` and `'O'`, capture all regions 4-directionally surrounded by `'X'` (flip enclosed `'O'`s to `'X'`). Border-connected `'O'`s survive.

Example:
```
Input:  [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
```

**Solution:**
```python
# Time: O(N*M) | Space: O(N*M)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        total_rows = len(board)
        total_cols = len(board[0])

        def mark_boundary_o(row, col):
            if (row < 0 or row >= total_rows or col < 0 or col >= total_cols
                    or board[row][col] is None or board[row][col] == "X"):
                return
            board[row][col] = None          # temporarily mark border-safe O
            mark_boundary_o(row-1, col)
            mark_boundary_o(row, col+1)
            mark_boundary_o(row+1, col)
            mark_boundary_o(row, col-1)

        for c in range(total_cols):
            if board[0][c] == "O": mark_boundary_o(0, c)
            if board[total_rows-1][c] == "O": mark_boundary_o(total_rows-1, c)
        for r in range(total_rows):
            if board[r][0] == "O": mark_boundary_o(r, 0)
            if board[r][total_cols-1] == "O": mark_boundary_o(r, total_cols-1)

        for r in range(total_rows):
            for c in range(total_cols):
                if board[r][c] == "O":
                    board[r][c] = "X"       # enclosed -> capture
                elif not board[r][c]:
                    board[r][c] = "O"       # restore border-safe
```

---

#### 11. Number of Enclaves

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| DFS/BFS | Boundary Analysis | Count land cells not reachable from boundary | O(m*n) | O(m*n) |

**Problem Statement:**
Given a binary grid (0 = sea, 1 = land), return the number of land cells from which you cannot walk off the boundary (i.e. land not connected to the border).

Example:
```
Input:  grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]   ->  Output: 3
```

**Solution:**
```python
# Time: O(N*M) | Space: O(N*M)

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        total_rows = len(grid)
        total_cols = len(grid[0])
        is_visited = [[False]*total_cols for _ in range(total_rows)]

        def mark_border_con_land_cell(row, col):
            if (row < 0 or row >= total_rows or col < 0 or col >= total_cols
                    or grid[row][col] == 0 or is_visited[row][col]):
                return
            is_visited[row][col] = True
            mark_border_con_land_cell(row-1, col)
            mark_border_con_land_cell(row, col+1)
            mark_border_con_land_cell(row+1, col)
            mark_border_con_land_cell(row, col-1)

        for c in range(total_cols):
            if grid[0][c] == 1: mark_border_con_land_cell(0, c)
            if grid[total_rows-1][c] == 1: mark_border_con_land_cell(total_rows-1, c)
        for r in range(total_rows):
            if grid[r][0] == 1: mark_border_con_land_cell(r, 0)
            if grid[r][total_cols-1] == 1: mark_border_con_land_cell(r, total_cols-1)

        result = 0
        for r in range(total_rows):
            for c in range(total_cols):
                if grid[r][c] == 1 and not is_visited[r][c]:
                    result += 1
        return result
```

---

#### 12. Word Ladder I

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| BFS | Level-wise Search | BFS from start word. For each word, try changing every character (a-z). If new word in wordList and not visited, add to queue. Level = transformation steps | O(M²*N) | O(M*N) |

**Problem Statement:**
Given `beginWord`, `endWord`, and a `wordList`, return the number of words in the shortest transformation sequence (each step changes one letter, each intermediate word must be in the list), or 0 if none.

Example:
```
Input:  beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
```

**Solution:**
```python
# Time: O(W * M * 26) | Space: O(W)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        queue = []
        if not endWord in word_set:
            return 0

        queue.append((beginWord, 1))
        while queue:
            cur_word, word_count = queue.pop(0)
            if cur_word == endWord:
                return word_count
            for i in range(len(cur_word)):
                for alphabet_no in range(26):
                    replaced_character = chr(ord("a") + alphabet_no)
                    replaced_word = cur_word[0:i] + replaced_character + cur_word[i+1:]
                    if replaced_word in word_set:
                        queue.append((replaced_word, word_count + 1))
                        word_set.remove(replaced_word)      # mark visited

        return 0
```

---

#### 13. Bipartite Graph

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| DFS/BFS | 2-Coloring | Start with color 0 for unvisited nodes. DFS/BFS: color current node, color neighbors with opposite color. If neighbor already has same color, NOT bipartite | O(V+E) | O(V) |

**Problem Statement:**
Given an undirected graph as an adjacency list, return `true` if it is bipartite (nodes 2-colorable so every edge joins different colors).

Example:
```
Input:  graph = [[1,2,3],[0,2],[0,1,3],[0,2]]   ->  Output: false
```

**Solution:**
```python
# Time: O(V) | Space: O(V)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [False] * n
        is_colored = [None] * n

        def color_node(cur_node, color=True):
            if visited[cur_node]:
                return is_colored[cur_node] == color
            visited[cur_node] = True
            is_colored[cur_node] = color
            is_bipartite = True
            for adj_node in graph[cur_node]:
                is_bipartite = is_bipartite and color_node(adj_node, not color)
            return is_bipartite

        for node in range(n):
            if visited[node]:
                continue
            if not color_node(node):
                return False
        return True
```

---

**Topological Sort**

#### 13.1 Cycle Detection (Alt Method)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Cycle Detection | Schedule Detection | Alternative cycle detection for directed graphs | O(V+E) | O(V) |

**Problem Statement:**
Detect a cycle in a directed graph via the course-schedule framing: return `true` if all courses can be finished (no cyclic prerequisite dependency).

Example:
```
Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]   ->  Output: False (cycle)
```

**Solution:**
```python
# Time: O(V+E) | Space: O(V+E)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        node_graph = [[] for i in range(numCourses)]
        for main_course, pre_req_course in prerequisites:
            node_graph[main_course].append(pre_req_course)

        course_completed = [0] * numCourses

        def courseFinish(node, visited_nodes):
            if course_completed[node]:
                return True
            if not course_completed[node] and visited_nodes[node]:
                return False              # back-edge -> cycle
            visited_nodes[node] = 1
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

#### 14. Topological Sort (DFS)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Topological Sort | Finish Time | DFS on each unvisited node. When DFS completes for a node (all children processed), add to result. REVERSE final result for correct topological order | O(V+E) | O(V) |

**Problem Statement:**
Given a DAG with `V` vertices and `E` edges, return any topological ordering of the vertices.

Example:
```
Input:  edges 0->1, 0->2   ->  Output: [0,2,1] (one valid order)
```

**Solution:**
```python
# Time: O(V + E) | Space: O(V)

from collections import deque

def topologicalSort(adj, v, e):
    node_graph = [[] for i in range(v)]
    for item in adj:
        if item[0] is not None:
            node_graph[item[0]].append(item[1])

    visited_nodes = [0] * v
    dq = deque()

    def topoSort(node):
        if visited_nodes[node]:
            return
        visited_nodes[node] = 1
        for adj_node in node_graph[node]:
            topoSort(adj_node)
        dq.append(node)              # push after all children done

    for cur_node in range(v):
        topoSort(cur_node)

    res = []
    while dq:
        res.append(dq.pop())         # reverse of finish order
    return res
```

---

#### 14.1 Cycle Detection (Undirected Alt)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Cycle Detection | BFS Alternative | Alternative BFS method for cycle detection in undirected graphs | O(V+E) | O(V) |

**Problem Statement:**
Given an undirected graph with `V` vertices and `E` edges (no self-loops), return `true` if it contains a cycle. BFS carrying the parent of each node.

Example:
```
Input:  4 vertices, edges 0-1,1-2,2-3,3-0   ->  Output: True
```

**Solution:**
```python
# Time: O(N + 2E) | Space: O(N)

from collections import deque

def bfs(node, parent_node, node_graph, visited_nodes):
    dq = deque()
    dq.append((node, parent_node))
    while dq:
        cur_node, parent_node = dq[0][0], dq[0][1]
        if not visited_nodes[cur_node]:
            visited_nodes[cur_node] = 1
            dq.popleft()
            for adj_node in node_graph[cur_node]:
                if not adj_node == parent_node and not adj_node == cur_node:
                    dq.append((adj_node, cur_node))
        else:
            return True
    return False
```

---

#### 15. Topological Sort (BFS - Kahn's)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Topological Sort | Indegree | Calculate indegree for all nodes. Add 0-indegree nodes to queue. Process queue: add current to result, reduce indegree of neighbors, add 0-indegree neighbors to queue | O(V+E) | O(V) |

**Problem Statement:**
Given a DAG with `V` vertices and `E` edges, return a topological ordering using Kahn's (BFS on in-degrees) algorithm.

Example:
```
Input:  adj = [[],[0],[0],[0]]   ->  Output: [1,2,3,0]
```

**Solution:**
```python
# Time: O(V + E) | Space: O(E)

from collections import deque

class Solution:
    def topoSort(self, V, adj):
        in_degree = [0] * V
        dq = deque()
        result = []

        for i in range(len(adj)):
            for item in adj[i]:
                in_degree[item] += 1

        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                dq.append(i)

        while dq:
            node = dq.popleft()
            for adj_node in adj[node]:
                in_degree[adj_node] -= 1
                if in_degree[adj_node] == 0:
                    dq.append(adj_node)
            result.append(node)

        return result
```

---

#### 16. Cycle Detection (Directed DFS)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Cycle Detection | DFS with Colors | Use 3 states: UNVISITED, VISITING, VISITED. If during DFS we reach a VISITING node, cycle found! Mark VISITED when DFS completes for a node | O(V+E) | O(V) |

**Problem Statement:**
Detect a cycle in a directed graph (Course Schedule): return `true` if all courses can be finished given prerequisite pairs.

Example:
```
Input:  numCourses = 2, prerequisites = [[1,0]]   ->  Output: True
```

**Solution:**
```python
# Time: O(V+E) | Space: O(V+E)
# course_completed = VISITED, per-DFS visited_nodes = VISITING

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        node_graph = [[] for i in range(numCourses)]
        for main_course, pre_req_course in prerequisites:
            node_graph[main_course].append(pre_req_course)

        course_completed = [0] * numCourses

        def courseFinish(node, visited_nodes):
            if course_completed[node]:
                return True
            if not course_completed[node] and visited_nodes[node]:
                return False                  # reached a VISITING node -> cycle
            visited_nodes[node] = 1
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

#### 17. Course Schedule II

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Topological Sort | Dependency Resolution | Use Kahn's algorithm to detect cycle and find valid ordering | O(V+E) | O(V) |

**Problem Statement:**
Given `numCourses` and prerequisite pairs, return an ordering of courses to finish all of them, or an empty array if impossible.

Example:
```
Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]   ->  Output: [0,2,1,3]
```

**Solution:**
```python
# Time: O(V+E) | Space: O(V+E)
# repo file reuses the DFS canFinish; the emitted finish order gives the schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        node_graph = [[] for i in range(numCourses)]
        for main_course, pre_req_course in prerequisites:
            node_graph[main_course].append(pre_req_course)

        course_completed = [0] * numCourses

        def courseFinish(node, visited_nodes):
            if course_completed[node]:
                return True
            if not course_completed[node] and visited_nodes[node]:
                return False
            visited_nodes[node] = 1
            for adj_node in node_graph[node]:
                if not courseFinish(adj_node, visited_nodes):
                    return False
            course_completed[node] = True     # order in which nodes complete = schedule
            return True

        for item in range(numCourses):
            if not course_completed[item]:
                if not courseFinish(item, [0]*numCourses):
                    return False
        return True
```

---

#### 18. Find Eventual Safe States

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Topological Sort | Reverse Graph | Safe nodes have no outgoing edges in terminal-oriented graph | O(V+E) | O(V) |

**Problem Statement:**
Given a directed graph, a node is safe if every path from it leads to a terminal node. Return all safe nodes in ascending order.

Example:
```
Input:  graph = [[1,2],[2,3],[5],[0],[5],[],[]]   ->  Output: [2,4,5,6]
```

**Solution:**
```python
# Time: O(V + E) | Space: O(V + E)
# reverse the edges, then Kahn's topo sort; nodes that drain out are safe

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        result = []
        reverse_graph = [[] for _ in range(V)]
        in_degree = [0] * V
        queue = []

        for cur_node in range(V):
            in_degree[cur_node] = len(graph[cur_node])      # out-degree of original
            for adj_node in graph[cur_node]:
                reverse_graph[adj_node].append(cur_node)

        for cur_node in range(V):
            if in_degree[cur_node] == 0:                     # terminal nodes
                queue.append(cur_node)

        while queue:
            cur_node = queue.pop(0)
            result.append(cur_node)
            for adj_node in reverse_graph[cur_node]:
                in_degree[adj_node] -= 1
                if in_degree[adj_node] == 0:
                    queue.append(adj_node)

        result.sort()
        return result
```

---

**Shortest Path**

#### 19. Shortest Path (Unweighted)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| BFS | Level Traversal | BFS naturally gives shortest path in unweighted graphs | O(V+E) | O(V) |

**Problem Statement:**
Given an undirected graph with unit-weight edges and a source `src`, return the shortest path length from `src` to every vertex (`-1` if unreachable).

Example:
```
Input:  n=4, edges = [[0,1],[0,3],[2,3]], src=0   ->  Output: [0,1,2,1]
```

**Solution:**
```python
# Time: O(V+E) | Space: O(V+E)

def shortestPath(n: int, edges: List[List[int]], src: int) -> List[int]:
    adj_list_input = [[] for _ in range(n)]
    for item in edges:
        adj_list_input[item[0]].append(item[1])
        adj_list_input[item[1]].append(item[0])

    queue = []
    visited = [False] * n
    queue.append((src, 0))
    result = [-1] * n

    while queue:
        cur_node, dis = queue.pop(0)
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        result[cur_node] = dis
        for adj_node in adj_list_input[cur_node]:
            queue.append((adj_node, dis+1))

    return result
```

---

#### 20. Shortest Path in DAG

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Topological Sort + DP | Relaxation | Topologically sort, then relax edges in order | O(V+E) | O(V) |

**Problem Statement:**
Given a weighted DAG with `N` vertices, return the shortest-path distance from vertex 0 to every vertex (`-1` if unreachable).

Example:
```
Input:  N=3, edges = [[2,0,4],[0,1,3],[2,1,2]]   ->  Output: [0,3,-1]
```

**Solution:**
```python
# Time: O(V+E) | Space: O(V+E)

def get_topo_sort_order(n, adj_list):
    stack = []
    visited = [False]*n
    def topo_sort(node):
        if visited[node]:
            return
        visited[node] = True
        for adj_node in adj_list[node]:
            topo_sort(adj_node[0])
        stack.append(node)
    topo_sort(0)
    return stack

def shortestPathInDAG(n: int, m: int, edges: List[List[int]]) -> List[int]:
    adj_list = [[] for _ in range(n)]
    dist = [-1]*n
    for src_node, dest_node, weight in edges:
        adj_list[src_node].append((dest_node, weight))

    stack = get_topo_sort_order(n, adj_list)
    dist[stack[-1]] = 0            # source (0) sits on top of the topo stack

    while stack:
        cur_node = stack.pop()
        for adj_node, w in adj_list[cur_node]:
            if dist[adj_node] == -1 or dist[cur_node] + w < dist[adj_node]:
                dist[adj_node] = dist[cur_node] + w

    return dist
```

---

#### 21. Dijkstra's Algorithm

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Priority Queue | Greedy Relaxation | Use min-heap with (distance, node). Always process node with minimum distance. Update distances of neighbors: if dist[u] + weight < dist[v], update dist[v] | O(E log V) | O(V) |

**Problem Statement:**
Given a weighted undirected connected graph and a source `S`, return the shortest distance from `S` to every vertex.

Example:
```
Input:  5 vertices, source 0, edges with weights   ->  Output: [0,4,1,2,5]
```

**Solution:**
```python
# Time: O(E log V) | Space: O(V + E)

from heapq import *

def dijkstra(edge, vertices, edges, source):
    adj_list = [[] for _ in range(vertices)]
    for src_node, dest_node, weight in edge:
        adj_list[src_node].append((dest_node, weight))
        adj_list[dest_node].append((src_node, weight))

    dist = [float("inf")] * vertices
    priority_queue = []
    dist[source] = 0
    heappush(priority_queue, (dist[source], source))

    while priority_queue:
        cur_path_dis, cur_node = heappop(priority_queue)     # min-distance node
        for adj_node, adj_node_dist in adj_list[cur_node]:
            if cur_path_dis + adj_node_dist < dist[adj_node]:
                dist[adj_node] = cur_path_dis + adj_node_dist
                heappush(priority_queue, (dist[adj_node], adj_node))

    return dist
```

---

#### 22. Shortest Path in Binary Maze

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| BFS/Dijkstra | Path Finding | BFS for unweighted, Dijkstra for weighted maze traversal | O(m*n) | O(m*n) |

**Problem Statement:**
Given an `n x n` binary matrix, return the length of the shortest clear path (all cells `0`, 8-directional moves) from top-left to bottom-right, or `-1` if none.

Example:
```
Input:  grid = [[0,0,0],[1,1,0],[1,1,0]]   ->  Output: 4
```

**Solution:**
```python
# Time: O(8*N*M) | Space: O(N*M)

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        no_of_rows = len(grid)
        no_of_cols = len(grid[0])
        queue = []
        visited = [[False]*no_of_cols for _ in range(no_of_rows)]
        if grid[0][0] == 1 or grid[no_of_rows-1][no_of_cols-1] == 1:
            return -1

        queue.append((0, 0, 0))
        while queue:
            row, col, dist = queue.pop(0)
            if (row < 0 or row >= no_of_rows or col < 0 or col >= no_of_cols
                    or grid[row][col] == 1 or visited[row][col]):
                continue
            visited[row][col] = True
            if row == no_of_rows-1 and col == no_of_cols-1:
                return dist + 1
            for dr, dc in [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]:
                queue.append((row+dr, col+dc, dist+1))

        return -1
```

---

#### 23. Path with Minimum Effort

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Binary Search + DFS | Binary Search Answer | Binary search on max effort, check feasibility with DFS | O(m*n*log(max)) | O(m*n) |

**Problem Statement:**
Given a grid of heights, travel from top-left to bottom-right minimizing effort, where a route's effort is the maximum absolute height difference between consecutive cells. Return the minimum effort.

Example:
```
Input:  heights = [[1,2,2],[3,8,2],[5,3,5]]   ->  Output: 2
```

**Solution:**
```python
# Time: O(4*N*M log(N*M)) | Space: O(N*M)  (repo uses Dijkstra on effort)

from heapq import *

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        no_of_rows = len(heights)
        no_of_cols = len(heights[0])
        dist = [[float("inf")]*no_of_cols for _ in range(no_of_rows)]
        priority_queue = []
        heappush(priority_queue, (0, (0, 0)))

        while priority_queue:
            abs_diff, (row, col) = heappop(priority_queue)
            for r, c in [(row-1,col),(row,col+1),(row+1,col),(row,col-1)]:
                if 0 <= r < no_of_rows and 0 <= c < no_of_cols:
                    next_abs_diff = max(abs_diff, abs(heights[row][col]-heights[r][c]))
                    if next_abs_diff < dist[r][c]:
                        dist[r][c] = next_abs_diff
                        heappush(priority_queue, (next_abs_diff, (r, c)))

        val = dist[no_of_rows-1][no_of_cols-1]
        return val if not val == float("inf") else 0
```

---

#### 24. Cheapest Flights K Stops

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Modified Dijkstra | State Space | Use (cost, node, stops) in priority queue. Only explore if stops <= K. State = (node, remaining_stops) to avoid revisiting same state | O(E*K) | O(V*K) |

**Problem Statement:**
Given `n` cities and directed weighted `flights`, return the cheapest price from `src` to `dst` with at most `k` stops, or `-1` if unreachable.

Example:
```
Input:  n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src=0, dst=3, k=1
Output: 700
```

**Solution:**
```python
# Time: O(E) (stops increase monotonically so a plain queue works) | Space: O(E+V)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        dist = [float("inf")] * n
        for s, d, weight in flights:
            adj_list[s].append((d, weight))

        queue = []
        queue.append((0, src, 0))    # (no_of_stops, node, dist)

        while queue:
            no_of_stops, cur_node, dist_to_node = queue.pop(0)
            if no_of_stops > k:
                break
            for adj_node, edge_weight in adj_list[cur_node]:
                if dist_to_node + edge_weight < dist[adj_node]:
                    dist[adj_node] = dist_to_node + edge_weight
                    queue.append((no_of_stops+1, adj_node, dist[adj_node]))

        return dist[dst] if not dist[dst] == float("inf") else -1
```

---

#### 25. Network Delay Time

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Dijkstra | Single Source | Find max time to reach all nodes from source using Dijkstra | O(E log V) | O(V) |

**Problem Statement:**
Given a directed weighted network of `n` nodes and travel times, a signal is sent from node `k`. Return the minimum time for all nodes to receive it, or `-1` if impossible.

Example:
```
Input:  times = [[2,1,1],[2,3,1],[3,4,1]], n=4, k=2   ->  Output: 2
```

**Solution:**
```python
# Time: O(E log n) | Space: O(n + E)

from heapq import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for _ in range(n+1)]
        dist = [float("inf") for _ in range(n+1)]
        for s, d, w in times:
            adj_list[s].append((d, w))

        priority_queue = []
        heappush(priority_queue, (0, k))
        dist[k] = 0

        while priority_queue:
            dist_to_cur_node, cur_node = heappop(priority_queue)
            for adj_node, adj_node_edge_weight in adj_list[cur_node]:
                if dist_to_cur_node + adj_node_edge_weight < dist[adj_node]:
                    dist[adj_node] = dist_to_cur_node + adj_node_edge_weight
                    heappush(priority_queue, (dist[adj_node], adj_node))

        max_dist = -1
        for i in range(1, n+1):
            if dist[i] > max_dist:
                max_dist = dist[i]

        return max_dist if not max_dist == float("inf") else -1
```

---

#### 26. Bellman-Ford Algorithm

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Edge Relaxation | Negative Weights | Relax all edges V-1 times, detect negative cycles | O(V*E) | O(V) |

**Problem Statement:**
Given a directed weighted graph (possibly negative weights, no negative cycles) with `N` vertices and a source `src`, return the shortest distance from `src` to every vertex (`10^8` if unreachable).

Example:
```
Input:  4 vertices, src=1, edges = [[1,2,4],[1,3,3],[2,4,7],[3,4,-2]]   ->  Output: [0,4,3,1]
```

**Solution:**
```python
# Time: O(N*M) | Space: O(N)

def bellmonFord(n, m, src, edges):
    dist = [10**8] * (n+1)
    dist[src] = 0
    # relax all edges N-1 times
    for i in range(n-1):
        for s_node, d_node, weight in edges:
            if dist[s_node] + weight < dist[d_node]:
                dist[d_node] = dist[s_node] + weight
    return dist
```

---

#### 27. Floyd-Warshall Algorithm

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| All Pairs DP | Via Vertex | Try all intermediate vertices k for paths i->j | O(V³) | O(V²) |

**Problem Statement:**
Given a directed weighted graph (may have negative edges, no negative cycles) with `N` vertices, find the shortest path length between `src` and `dest` using Floyd-Warshall.

Example:
```
Input:  4 vertices, src=1, dest=4, edges = [[1,2,4],[1,3,3],[2,4,7],[3,4,-2]]   ->  Output: 1
```

**Solution:**
```python
# Time: O(n^3) | Space: O(n^2)

def floydWarshall(n, m, src, dest, edges):
    dist_matrix = [[float("inf")]*(n+1) for _ in range(n+1)]

    for s_node in range(1, n+1):
        dist_matrix[s_node][s_node] = 0          # distance to self is 0

    for s_node, d_node, weight in edges:
        dist_matrix[s_node][d_node] = weight

    # try every intermediate node
    for via_node in range(1, n+1):
        for s_node in range(1, n+1):
            for d_node in range(1, n+1):
                dist_matrix[s_node][d_node] = min(
                    dist_matrix[s_node][d_node],
                    dist_matrix[s_node][via_node] + dist_matrix[via_node][d_node])

    return dist_matrix[src][dest] if not dist_matrix[src][dest] == float("inf") else 10**9
```

---

#### 28. Find City with Smallest Threshold

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Floyd-Warshall | Distance Analysis | Count reachable cities within threshold for each city | O(V³) | O(V²) |

**Problem Statement:**
Given `n` cities and weighted bidirectional `edges`, find the city with the fewest cities reachable within `distanceThreshold` (ties broken by the greatest city index).

Example:
```
Input:  n=4, edges=[[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold=4   ->  Output: 3
```

**Solution:**
```python
# Time: O(V^3) | Space: O(V^2)

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist_matrix = [[float("inf")]*n for _ in range(n)]
        for s_node in range(n):
            dist_matrix[s_node][s_node] = 0
        for s_node, d_node, weight in edges:
            dist_matrix[s_node][d_node] = weight
            dist_matrix[d_node][s_node] = weight

        for via_node in range(n):
            for s_node in range(n):
                for d_node in range(n):
                    dist_matrix[s_node][d_node] = min(
                        dist_matrix[s_node][d_node],
                        dist_matrix[s_node][via_node] + dist_matrix[via_node][d_node])

        city_node, adj_city_count = -1, float("inf")
        for s_node in range(n):
            count_of_ajd_cities = 0
            for d_node in range(n):
                count_of_ajd_cities += 1 if dist_matrix[s_node][d_node] <= distanceThreshold else 0
            if count_of_ajd_cities <= adj_city_count:      # <= keeps the greatest index on ties
                city_node, adj_city_count = s_node, count_of_ajd_cities

        return city_node
```

---

**MST & Union-Find**

#### 29. Prim's Algorithm

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy MST | Cut Property | Start with any node in MST. Use min-heap to track edges from MST to non-MST nodes. Always pick minimum weight edge that connects MST to new node | O(E log V) | O(V) |

**Problem Statement:**
Given an undirected connected weighted graph, find the total weight of its Minimum Spanning Tree (MST) using Prim's algorithm.

Example:
```
Input:  4 vertices, edges = [[0,1,3],[0,3,5],[1,2,1],[2,3,8]]   ->  Output: 9
```

**Solution:**
```python
# Time: O(E log E) | Space: O(E + V)

from heapq import *

def minimumSpanningTree(edges, V, E):
    visited = [False] * V
    priority_queue = []
    mst_weight = 0
    adj_list = [[] for _ in range(V)]
    for edge in edges:
        adj_list[edge.start].append((edge.end, edge.weigth))
        adj_list[edge.end].append((edge.start, edge.weigth))

    heappush(priority_queue, (0, 0, -1))   # (weight, node, parent)

    while priority_queue:
        edge_weight, cur_node, parent_node = heappop(priority_queue)
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        if not parent_node == -1:
            mst_weight += edge_weight
        for adj_node, adj_node_weight in adj_list[cur_node]:
            if not visited[adj_node]:
                heappush(priority_queue, (adj_node_weight, adj_node, cur_node))

    return mst_weight
```

---

#### 30. Kruskal's Algorithm

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Union-Find MST | Cycle Avoidance | SORT all edges by weight. For each edge (u,v): if find(u) != find(v), add edge to MST and union(u,v). Skip if same parent (creates cycle) | O(E log E) | O(V) |

**Problem Statement:**
Given a connected undirected weighted graph with `n` vertices and `m` edges, find the weight of its MST using Kruskal's algorithm (Union-Find).

Example:
```
Input:  5 vertices, edges = [[1,2,6],[2,3,5],[3,4,4],[1,4,1],[1,3,2],[3,5,3]]   ->  Output: 11
```

**Solution:**
```python
# Time: O(E log E) | Space: O(N)

def kruskalMST(n: int, edges: List[List[int]]) -> int:
    rank = [0] * (n+1)
    parent = [i for i in range(n+1)]

    def get_ulti_par(node):
        if parent[node] == node:
            return node
        parent[node] = get_ulti_par(parent[node])     # path compression
        return parent[node]

    def union_by_rank(u, v):
        u_ult_par = get_ulti_par(u)
        v_ult_par = get_ulti_par(v)
        if u_ult_par == v_ult_par:
            return
        if rank[u_ult_par] < rank[v_ult_par]:
            parent[u_ult_par] = v_ult_par
        elif rank[u_ult_par] > rank[v_ult_par]:
            parent[v_ult_par] = u_ult_par
        else:
            parent[v_ult_par] = u_ult_par
            rank[u_ult_par] += 1

    mst_weight = 0
    edges.sort(key=lambda element: element[2])         # smallest weight first
    for u, v, weight in edges:
        if not get_ulti_par(u) == get_ulti_par(v):     # skip if it forms a cycle
            mst_weight += weight
            union_by_rank(u, v)

    return mst_weight
```

---

#### 31. Number of Operations to Connect

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Union-Find | Component Counting | Count components, need (components-1) operations to connect | O(E*α(V)) | O(V) |

**Problem Statement:**
Given `n` computers and `connections` (cables), you may move a redundant cable to join disconnected computers. Return the minimum number of moves to connect all computers, or `-1` if impossible.

Example:
```
Input:  n=4, connections=[[0,1],[0,2],[1,2]]   ->  Output: 1
Input:  n=6, connections=[[0,1],[0,2],[0,3],[1,2],[1,3]]   ->  Output: 2
```

**Solution:**
```python
# Time: O(N + E) | Space: O(N)

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n

        def get_ultimate_parent(node):
            if parent[node] == node:
                return node
            parent[node] = get_ultimate_parent(parent[node])
            return parent[node]

        def union_by_rank(u, v):
            ulp_u = get_ultimate_parent(u)
            ulp_v = get_ultimate_parent(v)
            if ulp_u == ulp_v:
                return
            if rank[ulp_u] > rank[ulp_v]:
                parent[ulp_v] = ulp_u
            elif rank[ulp_u] < rank[ulp_v]:
                parent[ulp_u] = ulp_v
            else:
                parent[ulp_v] = ulp_u
                rank[ulp_u] += 1

        no_of_extra_edges = 0
        for u, v in connections:
            if get_ultimate_parent(u) == get_ultimate_parent(v):
                no_of_extra_edges += 1        # redundant edge -> reusable cable
            else:
                union_by_rank(u, v)

        no_of_components = 0
        for node in range(n):
            if node == parent[node]:
                no_of_components += 1

        require_edges = no_of_components - 1
        return require_edges if no_of_extra_edges >= require_edges else -1
```

---

#### 32. Most Stones Removed

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Union-Find | Connected Components | Stones in same row/col are connected, remove all but one per component | O(N*α(N)) | O(N) |

**Problem Statement:**
Given `n` stones at coordinates, a stone can be removed if it shares a row or column with another remaining stone. Return the maximum number of stones that can be removed.

Example:
```
Input:  stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]   ->  Output: 5
```

**Solution:**
```python
# Time: O(N) | Space: O(max_row + max_col)
# Trick: model rows and columns as nodes; answer = n - number_of_components

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        max_r, max_c = 0, 0
        n = len(stones)
        for r, c in stones:
            max_r = max(max_r, r)
            max_c = max(max_c, c)

        total_nodes = (max_r+1) + (max_c+1)
        rank = [0] * total_nodes
        parent = [i for i in range(total_nodes)]

        def get_ultimate_parent(node):
            if node == parent[node]:
                return node
            parent[node] = get_ultimate_parent(parent[node])
            return parent[node]

        def union_by_rank(u, v):
            ulp_u = get_ultimate_parent(u)
            ulp_v = get_ultimate_parent(v)
            if ulp_u == ulp_v:
                return
            if rank[ulp_u] < rank[ulp_v]:
                parent[ulp_u] = ulp_v
            elif rank[ulp_u] > rank[ulp_v]:
                parent[ulp_v] = ulp_u
            else:
                parent[ulp_v] = ulp_u
                rank[ulp_u] += 1

        node_set = set()
        for u, v in stones:
            v = (max_r+1) + v            # offset column ids so they don't clash with rows
            union_by_rank(u, v)
            node_set.add(u)
            node_set.add(v)

        no_of_comp = 0
        for node in node_set:
            if node == parent[node]:
                no_of_comp += 1

        return n - no_of_comp
```

---

#### 33. Number of Islands II

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Union-Find | Dynamic Connectivity | Add lands dynamically, merge adjacent components using Union-Find | O(K*α(M*N)) | O(M*N) |

**Problem Statement:**
Given an `n x m` grid of water, process `queries` that each turn a cell into land. After each query, return the current number of islands.

Example:
```
Input:  n=3, m=4, queries = [[1,1],[1,2],[2,3]]   ->  Output: [1,1,2]
```

**Solution:**
```python
# Time: O(Q*α + N*M) | Space: O(Q + N*M)

def numberOfIslandII(n: int, m: int, queries: List[List[int]], q: int) -> int:
    rank = [0] * (n*m)
    parent = [i for i in range(n*m)]
    result = []

    def get_ultimate_parent(node):
        if parent[node] == node:
            return parent[node]
        parent[node] = get_ultimate_parent(parent[node])
        return parent[node]

    def union_by_rank(u, v):
        ulp_u = get_ultimate_parent(u)
        ulp_v = get_ultimate_parent(v)
        if ulp_u == ulp_v:
            return
        if rank[ulp_u] > rank[ulp_v]:
            parent[ulp_v] = ulp_u
        elif rank[ulp_u] < rank[ulp_v]:
            parent[ulp_u] = ulp_v
        else:
            parent[ulp_v] = ulp_u
            rank[ulp_u] += 1

    def union_with_neighbour_node(cur_node, r, c, no_of_islands):
        for row, col in [(r-1,c),(r,c+1),(r+1,c),(r,c-1)]:
            if 0 <= row < n and 0 <= col < m and adj_matrix[row][col] == 1:
                adj_node = m*row + col
                if not get_ultimate_parent(cur_node) == get_ultimate_parent(adj_node):
                    no_of_islands -= 1          # merging two islands into one
                    union_by_rank(cur_node, adj_node)
        return no_of_islands

    no_of_islands = 0
    adj_matrix = [[0]*m for _ in range(n)]

    for u, v in queries:
        adj_matrix[u][v] = 1
        no_of_islands += 1                       # each new land starts as its own island
        cur_node = m*u + v
        no_of_islands = union_with_neighbour_node(cur_node, u, v, no_of_islands)
        result.append(no_of_islands)

    return result
```

---

### Dynamic Programming

**1D DP**

#### 1. Climbing Stairs

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 1D DP | Fibonacci | Each step can be reached from previous 1 or 2 steps: dp[i] = dp[i-1] + dp[i-2] | O(n) | O(n) |

**Problem Statement:**
You are climbing a staircase of `n` steps. Each move climbs 1 or 2 steps. Return the number of distinct ways to reach the top.

Example:
```
Input:  n = 3   ->  Output: 3
```

**Solution:**
```python
# Time: O(n) | Space: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)
        memo[0] = memo[1] = 1
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
```

---

#### 2. Frog Jump

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 1D DP | Min Cost Path | Min cost to reach stone: dp[i] = min(dp[i-1] + cost1, dp[i-2] + cost2) | O(n) | O(n) |

**Problem Statement:**
A frog on stair 1 wants to reach stair `N`. From stair `i` it can jump to `i+1` or `i+2`, costing `|HEIGHT[i]-HEIGHT[j]|`. Return the minimum total energy to reach stair `N`.

Example:
```
Input:  heights = [10,20,30,10]   ->  Output: 20
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

def frogJump(n: int, heights: List[int]) -> int:
    if n == 1:
        return 0
    memo = [-1]*n
    memo[0] = 0
    memo[1] = abs(heights[1] - heights[0])
    for i in range(2, n):
        memo[i] = min(
            abs(heights[i] - heights[i-1]) + memo[i-1],
            abs(heights[i] - heights[i-2]) + memo[i-2]
        )
    return memo[n-1]
```

---

#### 3. Frog Jump with K Distance

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 1D DP | Variable Jumps | Try all possible jumps from 1 to k, take minimum cost path | O(n*k) | O(n) |

**Problem Statement:**
Same as Frog Jump, but from stair `i` the frog can jump to any of `i+1 ... i+k`. Return the minimum total cost to reach stair `N`.

Example:
```
Input:  n=4, k=2, heights = [10,40,30,10]   ->  Output: 40
```

**Solution:**
```python
# Time: O(N*K) | Space: O(N)

def minimizeCost(n: int, k: int, heights: List[int]) -> int:
    memo = [-1]*n

    def min_energy_req(n):
        if n == 0:
            return 0
        if not memo[n] == -1:
            return memo[n]
        if n == 1:
            memo[1] = abs(heights[1]-heights[0])
            return memo[1]
        minimum = float("inf")
        for i in range(1, k+1):
            if n-i >= 0:
                val = abs(heights[n]-heights[n-i]) + min_energy_req(n-i)
                minimum = min(minimum, val)
        memo[n] = minimum
        return memo[n]

    return min_energy_req(n-1)
```

---

#### 4. Maximum Sum Non-Adjacent

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 1D DP | Pick/Not Pick | At each house: max(rob current + dp[i-2], skip current + dp[i-1]) | O(n) | O(n) |

**Problem Statement:**
Given money in each house (House Robber), maximize the amount robbed without robbing two adjacent houses.

Example:
```
Input:  nums = [2,7,9,3,1]   ->  Output: 12
```

**Solution:**
```python
# Time: O(n) | Space: O(n)

class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def robMax(n):
            if n < 0:
                return 0
            if not memo[n] == -1:
                return memo[n]
            pick = nums[n] + robMax(n-2)
            not_picked = 0 + robMax(n-1)
            memo[n] = max(pick, not_picked)
            return memo[n]

        return robMax(n-1)
```

---

#### 5. House Robber II

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 1D DP | Circular Array | Run house robber twice: [0...n-2] and [1...n-1], take maximum | O(n) | O(1) |

**Problem Statement:**
Same as House Robber but houses are arranged in a circle (first and last are adjacent). Maximize the robbed amount.

Example:
```
Input:  nums = [1,2,3,1]   ->  Output: 4
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

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

        # exclude last house OR exclude first house
        return max(
            robMax(n-1, 1, [-1] * n),
            robMax(n-2, 0, [-1] * n)
        )
```

---

**2D/Grid DP**

#### 6. Ninja Training

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 2D DP | State Tracking | dp[day][last_activity] = max points until day with last_activity done. For each day, try all activities except last one: dp[day][act] = points[day][act] + max(dp[day-1][other_activities]) | O(n*4) | O(n*4) |

**Problem Statement:**
Over `N` days, each day the ninja performs one of 3 activities (each with points), but not the same activity on two consecutive days. Maximize total merit points.

Example:
```
Input:  points = [[1,2,5],[3,1,1],[3,3,3]]   ->  Output: 11
```

**Solution:**
```python
# Time: O(N*4) | Space: O(N*4)

def ninjaTraining(n: int, points: List[List[int]]) -> int:
    def get_max_point(i, j):
        if i == n:
            return 0
        if not memo[i][j] == -1:
            return memo[i][j]
        child_indexes = [0, 1, 2]
        child_indexes.remove(j)          # skip last activity
        temp_max = float("-inf")
        for child_index in child_indexes:
            temp = points[i][j] + get_max_point(i+1, child_index)
            temp_max = max(temp_max, temp)
        memo[i][j] = temp_max
        return memo[i][j]

    memo = [[-1, -1, -1] for _ in range(n)]
    result = float("-inf")
    for activity_no in range(3):
        result = max(result, get_max_point(0, activity_no))
    return result
```

---

#### 7. Grid Unique Paths

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 2D DP | Path Counting | Base case: dp[0][j] = dp[i][0] = 1 (first row/col). For each cell: dp[i][j] = dp[i-1][j] + dp[i][j-1] (paths from top + paths from left) | O(m*n) | O(m*n) |

**Problem Statement:**
A robot at the top-left of an `m x n` grid moves only right or down. Return the number of unique paths to the bottom-right.

Example:
```
Input:  m = 3, n = 2   ->  Output: 3
```

**Solution:**
```python
# Time: O(N*M) | Space: O(M*N)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1]*n for _ in range(m)]

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

#### 8. Grid Unique Paths II

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 2D DP | Path Counting with Obstacles | Same as unique paths but set dp[i][j] = 0 for obstacles | O(m*n) | O(m*n) |

**Problem Statement:**
Same as Unique Paths but the grid has obstacles (`1`). Paths cannot pass through obstacle cells. Return the number of unique paths.

Example:
```
Input:  obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]   ->  Output: 2
```

**Solution:**
```python
# Time: O(N*M) | Space: O(M*N)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[-1]*n for _ in range(m)]

        def get_unique_paths(i, j):
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
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

#### 9. Min Path Sum

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 2D DP | Path Optimization | dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]) | O(m*n) | O(m*n) |

**Problem Statement:**
Given an `m x n` grid of non-negative numbers, find a top-left to bottom-right path (moving only right/down) minimizing the sum along the path.

Example:
```
Input:  grid = [[1,3,1],[1,5,1],[4,2,1]]   ->  Output: 7
```

**Solution:**
```python
# Time: O(N*M) | Space: O(M*N)

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[-1]*n for _ in range(m)]

        def get_min_path_sum(i, j):
            if i >= m or j >= n:
                return float("inf")
            if i == m-1 and j == n-1:
                return grid[i][j]
            if not memo[i][j] == -1:
                return memo[i][j]
            memo[i][j] = grid[i][j] + min(get_min_path_sum(i, j+1), get_min_path_sum(i+1, j))
            return memo[i][j]

        return get_min_path_sum(0, 0)
```

---

**Subsequence DP**

#### 10. Subset Sum Equal to Target

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Subsequence DP | 0/1 Knapsack | dp[i][sum] = can we make sum using first i elements. For each element: dp[i][sum] = dp[i-1][sum] OR dp[i-1][sum-arr[i]] (exclude OR include) | O(n*target) | O(n*target) |

**Problem Statement:**
Given an array of `N` positive integers and an integer `K`, return `true` if some subset sums to `K`.

Example:
```
Input:  arr = [4,3,2,1], K = 5   ->  Output: true
```

**Solution:**
```python
# Time: O(N*K) | Space: O(N*K)

def subsetSumToK(n, k, arr):
    memo = [[-1]*(k+1) for _ in range(n)]

    def get_subset_sum_to_k(index, target):
        if target == 0:
            return True
        if target < 0:
            return False
        if index == 0:
            return arr[index] == target
        if not memo[index][target] == -1:
            return memo[index][target]
        pick = get_subset_sum_to_k(index-1, target-arr[index])
        unpick = get_subset_sum_to_k(index-1, target)
        memo[index][target] = pick or unpick
        return memo[index][target]

    return get_subset_sum_to_k(n-1, k)
```

---

#### 11. Partition Equal Subset Sum

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Subsequence DP | Subset Sum | If total_sum is odd, return False. Otherwise, use subset sum DP to check if subset with sum = total_sum/2 exists. If yes, remaining elements also sum to total_sum/2 | O(n*sum) | O(n*sum) |

**Problem Statement:**
Given an integer array `nums`, return `true` if it can be partitioned into two subsets with equal sum.

Example:
```
Input:  nums = [1,5,11,5]   ->  Output: true
```

**Solution:**
```python
# Time: O(N*S) | Space: O(N*S)

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if not total % 2 == 0:               # odd total can't split evenly
            return False

        n = len(nums)
        target = total // 2
        memo = [[-1]*(target+1) for _ in range(n)]

        def get_partition_sum_to_target(index, target):
            if target == 0:
                return True
            if index == 0:
                return nums[0] == target
            if target < 0:
                return False
            if not memo[index][target] == -1:
                return memo[index][target]
            pick = get_partition_sum_to_target(index-1, target-nums[index])
            unpick = get_partition_sum_to_target(index-1, target)
            memo[index][target] = pick or unpick
            return memo[index][target]

        return get_partition_sum_to_target(n-1, target)
```

---

#### 12. Partition with Min Difference

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Subsequence DP | Subset Sum Variant | Find all possible sums, then minimize \|sum1 - sum2\| = \|total - 2*sum1\| | O(n*sum) | O(n*sum) |

**Problem Statement:**
Given an array `arr` of `n` non-negative integers, partition it into two subsets minimizing the absolute difference of their sums. Return that minimum difference.

Example:
```
Input:  arr = [8,6,5]   ->  Output: 3
```

**Solution:**
```python
# Time: O(n*sum) | Space: O(n*sum)

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    n = len(arr)
    total_sum = sum(arr)
    dp = [[-1]*(total_sum + 1) for _ in range(n)]

    def get_min_sum_difference(index, s1, s2):
        if index == n:
            return abs(s1 - s2)
        if not dp[index][s1] == -1:
            return dp[index][s1]
        pick = get_min_sum_difference(index+1, s1 + arr[index], s2)
        unpick = get_min_sum_difference(index+1, s1, s2 + arr[index])
        dp[index][s1] = min(pick, unpick)
        return dp[index][s1]

    return get_min_sum_difference(0, 0, 0)
```

---

#### 13. 0/1 Knapsack

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Subsequence DP | Classic Knapsack | dp[i][w] = max value using first i items with weight limit w. For each item: dp[i][w] = max(dp[i-1][w], value[i] + dp[i-1][w-weight[i]]) if weight[i] <= w | O(n*W) | O(n*W) |

**Problem Statement:**
A thief's knapsack carries at most weight `W`. Given `N` items with weights and values, maximize the total value that fits.

Example:
```
Input:  weights = [1,2,4,5], values = [5,4,8,6], W = 5   ->  Output: 13
```

**Solution:**
```python
# Time: O(N*W) | Space: O(N*W)  (tabulation)

dp = [[-1]*(max_weight+1) for _ in range(len(weights))]
# base case: only the first item available
for available_weight in range(max_weight+1):
    dp[0][available_weight] = values[0] if weights[0] <= available_weight else 0

for index in range(1, len(weights)):
    for w in range(max_weight+1):
        pick = 0
        if w - weights[index] >= 0:
            pick = values[index] + dp[index-1][w-weights[index]]
        unpick = dp[index-1][w]
        dp[index][w] = max(pick, unpick)

# answer: dp[n-1][max_weight]
```

---

#### 14. Minimum Coins

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Subsequence DP | Unbounded Knapsack | dp[amount] = min coins to make amount. For each amount, try all coins: if coin <= amount, dp[amount] = min(dp[amount], 1 + dp[amount-coin]) | O(coins*amount) | O(amount) |

**Problem Statement:**
Given coin denominations and an `amount`, return the fewest coins needed to make `amount` (infinite supply of each coin), or `-1` if impossible.

Example:
```
Input:  coins = [1,2,5], amount = 11   ->  Output: 3
Input:  coins = [2], amount = 3        ->  Output: -1
```

**Solution:**
```python
# Time: O(N*T) | Space: O(N*T)  (tabulation)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1]*(amount+1) for _ in range(len(coins))]
        # base: using only the first coin
        for target in range(amount+1):
            dp[0][target] = target // coins[0] if target % coins[0] == 0 else float("inf")

        for index in range(1, len(coins)):
            for target in range(amount+1):
                pick_coins = float("inf")
                if coins[index] <= target:
                    pick_coins = 1 + dp[index][target-coins[index]]   # stay on index (unbounded)
                unpick_coins = dp[index-1][target]
                dp[index][target] = min(pick_coins, unpick_coins)

        res = dp[len(coins)-1][amount]
        return -1 if res == float("inf") else int(res)
```

---

#### 15. Coin Change II

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Subsequence DP | Counting Ways | dp[amount] = number of ways to make amount. For each coin, update all amounts: if coin <= amount, dp[amount] += dp[amount-coin]. Process coins in outer loop to avoid counting duplicates! | O(coins*amount) | O(amount) |

**Problem Statement:**
Given coins and an `amount`, return the number of combinations that make up `amount` (infinite supply of each coin).

Example:
```
Input:  amount = 5, coins = [1,2,5]   ->  Output: 4
```

**Solution:**
```python
# Time: O(N*T) | Space: O(N*T)  (tabulation)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1]*(amount+1) for _ in range(len(coins))]
        n = len(coins)
        for i in range(n):
            dp[i][0] = 1                             # one way to make amount 0
        for target in range(1, amount+1):
            dp[0][target] = 1 if target % coins[0] == 0 else 0

        for index in range(1, n):
            for target in range(1, amount+1):
                pick = 0
                if target - coins[index] >= 0:
                    pick = dp[index][target-coins[index]]
                unpick = dp[index-1][target]
                dp[index][target] = pick + unpick

        return dp[n-1][amount]
```

---

**String DP**

#### 16. Longest Common Subsequence

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String DP | 2D Matching | dp[i][j] = LCS length for s1[0...i-1] and s2[0...j-1]. If s1[i-1] == s2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]. Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1]) | O(n*m) | O(n*m) |

**Problem Statement:**
Given two strings `text1` and `text2`, return the length of their longest common subsequence.

Example:
```
Input:  text1 = "abcde", text2 = "ace"   ->  Output: 3
```

**Solution:**
```python
# Time: O(N*M) | Space: O(N*M)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]      # row/col 0 = empty prefix

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]
```

---

#### 17. Print All LCS

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String DP | Backtracking | Build LCS by backtracking from dp table using optimal choices | O(n*m) | O(n*m) |

**Problem Statement:**
Given two strings `s` and `t`, print all longest common subsequences in lexicographical order.

Example:
```
Input:  s = "abaaa", t = "baabaca"   ->  Output: aaaa abaa baaa
```

**Solution:**
```python
# Time: O(N*M) + backtracking | Space: O(N*M)

class Solution:
    def all_longest_common_subsequences(self, s, t):
        text1, text2 = s, t
        n, m = len(text1), len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        res_len = dp[n][m]
        res = set()

        def add_answer(row, col, temp_str=""):
            while row > 0 and col > 0:
                if text1[row-1] == text2[col-1]:
                    temp_str = text1[row-1] + temp_str
                    row -= 1
                    col -= 1
                else:
                    if dp[row-1][col] > dp[row][col-1]:
                        row -= 1
                    elif dp[row-1][col] < dp[row][col-1]:
                        col -= 1
                    else:                       # both branches lead to an LCS -> explore both
                        add_answer(row-1, col, temp_str)
                        add_answer(row, col-1, temp_str)
                        return
            res.add(temp_str)

        for i in range(1, n+1):
            for j in range(1, m+1):
                if dp[i][j] == res_len and text1[i-1] == text2[j-1]:
                    add_answer(i, j)

        return sorted(res)
```

---

#### 18. Longest Common Substring

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String DP | Continuous Matching | dp[i][j] = length of common substring ending at s1[i-1] and s2[j-1]. If s1[i-1] == s2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]. Else: dp[i][j] = 0. Track max across all dp[i][j] | O(n*m) | O(n*m) |

**Problem Statement:**
Given two strings, find the length of their longest common substring (contiguous).

Example:
```
Input:  S1 = "ABCDGH", S2 = "ACDGHR"   ->  Output: 4  ("CDGH")
```

**Solution:**
```python
# Time: O(N*M) | Space: O(N*M)

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        res = 0
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if S1[i-1] == S2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0            # substring must be contiguous -> reset on mismatch
                res = max(res, dp[i][j])

        return res
```

---

#### 19. Longest Palindromic Subsequence

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String DP | LCS Variant | SMART TRICK: LPS(s) = LCS(s, reverse(s)). Create reversed string and find LCS between original and reversed string using standard LCS algorithm | O(n²) | O(n²) |

**Problem Statement:**
Given a string `s`, find the length of its longest palindromic subsequence.

Example:
```
Input:  s = "bbbab"   ->  Output: 4  ("bbbb")
```

**Solution:**
```python
# Time: O(n^2) | Space: O(n^2)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_rev = s[::-1]
        n, m = len(s), len(s_rev)
        dp = [[0]*(m+1) for _ in range(n+1)]

        # LPS(s) == LCS(s, reverse(s))
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == s_rev[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]
```

---

#### 20. Min Insertions to Make Palindrome

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String DP | LPS Application | Insertions needed = n - LPS(s), where LPS is longest palindromic subsequence | O(n²) | O(n²) |

**Problem Statement:**
Given a string `s`, return the minimum number of character insertions to make it a palindrome.

Example:
```
Input:  s = "mbadm"   ->  Output: 2
```

**Solution:**
```python
# Time: O(n^2) | Space: O(n^2)

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        s_rev = s[::-1]
        dp = [[0]*(n+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s_rev[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        long_palind_subseq_len = dp[n][n]
        # keep the LPS, insert a mirror for every remaining character
        return n - long_palind_subseq_len
```

---

#### 21. Min Insert/Delete to Convert String

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String DP | LCS Application | Operations = (n - LCS) + (m - LCS) where LCS is longest common subsequence | O(n*m) | O(n*m) |

**Problem Statement:**
Given two strings `word1` and `word2`, return the minimum number of single-character deletions (from either string) to make them equal.

Example:
```
Input:  word1 = "sea", word2 = "eat"   ->  Output: 2
```

**Solution:**
```python
# Time: O(n^2) | Space: O(n^2)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        lcs_len = dp[n][m]
        return (n - lcs_len) + (m - lcs_len)
```

---

#### 22. Shortest Common Supersequence

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String DP | LCS + Construction | Build shortest string containing both as subsequences using LCS | O(n*m) | O(n*m) |

**Problem Statement:**
Given two strings `str1` and `str2`, return the shortest string that has both as subsequences.

Example:
```
Input:  str1 = "abac", str2 = "cab"   ->  Output: "cabac"
```

**Solution:**
```python
# Time: O(n^2) | Space: O(n^2)

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # walk the LCS table backwards, emitting characters from both strings
        res = ""
        i, j = n, m
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                res = str1[i-1] + res
                i -= 1
                j -= 1
            elif dp[i-1][j] >= dp[i][j-1]:
                res = str1[i-1] + res
                i -= 1
            else:
                res = str2[j-1] + res
                j -= 1

        while i > 0:
            res = str1[i-1] + res
            i -= 1
        while j > 0:
            res = str2[j-1] + res
            j -= 1

        return res
```

---

## SDE Sheet Problems

### Arrays

#### 1. Pow(x, n)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Math | Fast Exponentiation | If n is even: x^n = (x^(n/2))^2, if odd: x^n = x * x^(n-1) | O(log n) | O(log n) |

**Problem Statement:**
Implement `pow(x, n)` which calculates `x` raised to the power `n`.

Example:
```
Input:  x = 2.0, n = 10   ->  Output: 1024.0
Input:  x = 2.0, n = -2   ->  Output: 0.25
```

**Solution:**
```python
# Time: O(n) | Space: O(n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            return x * pow(x, n-1)
        else:
            return pow(x, n+1) / x
```

---

#### 2. Two Sum

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Array | Hash Map | Store target-current in dict, check if current exists | O(n) | O(n) |

**Problem Statement:**
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`.

Example:
```
Input:  nums = [2,7,11,15], target = 9   ->  Output: [0,1]
```

**Solution:**
```python
# Time: O(n log n) | Space: O(n)  (repo uses sort + two-pointer)
import copy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original_input = copy.deepcopy(nums)
        nums.sort()
        i, j = 0, len(nums) - 1
        fir_ind, sec_ind = -1, -1
        while i < j:
            if nums[i] + nums[j] == target:
                break
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1

        for ind in range(len(original_input)):
            if original_input[ind] == nums[i] and fir_ind == -1:
                fir_ind = ind
            elif original_input[ind] == nums[j]:
                sec_ind = ind

        return [fir_ind, sec_ind]
```

---

### Linked Lists

#### 1. Reverse Linked List

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Three Pointers | Track prev, current, next. Reverse links one by one | O(n) | O(1) |

**Problem Statement:**
Given the head of a singly linked list, reverse the list and return the reversed list.

Example:
```
Input:  head = [1,2,3,4,5]   ->  Output: [5,4,3,2,1]
```

**Solution:**
```python
# Time: O(n) | Space: O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev_node = None
        current_node = head
        next_node = current_node.next

        while current_node:
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            next_node = current_node.next if current_node else None

        return prev_node
```

---

#### 2. Find Middle of Linked List

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Linked List | Two Pointers (Tortoise & Hare) | Slow pointer moves 1 step, fast moves 2 steps. When fast reaches end, slow is at middle | O(n) | O(1) |

**Problem Statement:**
Given the head of a singly linked list, return the middle node. If there are two middle nodes, return the second one.

Example:
```
Input:  head = [1,2,3,4,5]   ->  Output: node 3
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        second = head

        while not (second == None or second.next == None):
            first = first.next
            second = second.next.next

        return first
```

---

### Greedy Algorithms

#### 1. N Meetings in One Room

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Activity Selection | Sort by end time, greedily pick meetings that end earliest | O(n log n) | O(n) |

**Problem Statement:**
Given `N` meetings with start and end times and one room, return the maximum number of non-overlapping meetings that can be organized.

Example:
```
Input:  start = [1,3,0,5,8,5], end = [2,4,6,7,9,9]   ->  Output: 4
```

**Solution:**
```python
# Time: O(n log n) | Space: O(n)

def maximumMeetings(start: List[int], end: List[int]) -> int:
    interval = []
    for i in range(len(start)):
        interval.append([start[i], end[i]])

    interval.sort(key=lambda x: x[0])
    if len(interval) == 1:
        return 1

    cur, next = 0, 1
    while next < len(interval):
        if interval[cur][0] <= interval[next][0] <= interval[cur][1]:
            if interval[cur][1] <= interval[next][1]:
                interval.pop(next)
                continue
            else:
                interval.pop(cur)
                continue
        cur += 1
        next += 1

    return len(interval)
```

---

#### 2. Fractional Knapsack

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Value/Weight Ratio | Sort by value/weight ratio, pick highest ratio items first | O(n log n) | O(1) |

**Problem Statement:**
Given weights and values of `N` items and a knapsack capacity `W`, maximize the total value; items may be broken (fractions allowed).

Example:
```
Input:  N=3, W=50, value=[60,100,120], weight=[10,20,30]   ->  Output: 240.00
```

**Solution:**
```python
# Time: O(n log n) | Space: O(1)

class Solution:
    def sort_by_val_to_weight_ratio(self, element):
        return element[2]

    def fractionalknapsack(self, W, arr, n):
        w = W
        inp = []
        result = 0
        for item in arr:
            inp.append((item.weight, item.value, item.value / item.weight))
        inp.sort(reverse=True, key=self.sort_by_val_to_weight_ratio)

        i = 0
        while w > 0 and i < len(inp):
            cur_weight, cur_value = inp[i][0], inp[i][1]
            if cur_weight <= w:
                result += cur_value
                w -= cur_weight
            else:
                result += (cur_value / cur_weight) * w
                w = 0
            i += 1

        return result
```

---

#### 3. Maximum Activities

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Greedy | Activity Selection | Same as N meetings - sort by finish time, greedily select non-overlapping activities | O(n log n) | O(n) |

**Problem Statement:**
Given `N` activities with start and finish times, return the maximum number a single person can perform (start time may coincide with another's end time).

Example:
```
Input:  start = [1,6,2,4], finish = [2,7,5,8]   ->  Output: 3
```

**Solution:**
```python
# Time: O(N log N) | Space: O(N)

def maximumActivities(start, finish):
    n = len(start)
    tasks = []
    for i in range(n):
        tasks.append([start[i], finish[i]])

    tasks.sort(key=lambda arr: arr[1])       # sort by finish time
    task_pos_count = 0
    cur_int_end = -1

    for cur_task in tasks:
        if cur_task[0] >= cur_int_end:
            task_pos_count += 1
            cur_int_end = cur_task[1]

    return task_pos_count
```

---

### Recursion & Backtracking

#### 1. Subset Sums

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Pick / Not Pick | Generate all possible subset sums using pick/not-pick pattern | O(2^n) | O(2^n) |

**Problem Statement:**
Given an array `nums` of `n` integers, return all subset sums in non-decreasing order.

Example:
```
Input:  nums = [1,2,3]   ->  Output: 0 1 2 3 3 4 5 6
```

**Solution:**
```python
# Time: O(n * 2^n) | Space: O(2^n)

def subsetSum(num: List[int]) -> List[int]:
    n = len(num)
    result = []
    def sum_of_subset(index, num, sum):
        if index == n:
            result.append(sum)
            return
        sum_of_subset(index+1, num, sum + num[index])   # pick
        sum_of_subset(index+1, num, sum)                # unpick

    sum_of_subset(0, num, 0)
    result.sort()
    return result
```

---

#### 2. Subsets II

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Backtracking with Duplicates | Sort array, skip duplicates at same recursion level | O(2^n) | O(2^n) |

**Problem Statement:**
Given an integer array `nums` that may contain duplicates, return all unique subsets (the power set).

Example:
```
Input:  nums = [1,2,2]   ->  Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**Solution:**
```python
# Time: O(2^n) | Space: O(2^n)

from copy import deepcopy

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        def get_subset_with_dup(index, num, arr):
            if index == n:
                if arr not in result:            # dedupe subsets
                    result.append(deepcopy(arr))
                return
            arr.append(num[index])               # pick
            get_subset_with_dup(index+1, num, arr)
            arr.remove(num[index])               # unpick
            get_subset_with_dup(index+1, num, arr)

        get_subset_with_dup(0, nums, [])
        return result
```

---

#### 3. Palindrome Partitioning

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Recursion | Backtracking | At each position, try all possible palindromic partitions | O(2^n * n) | O(n) |

**Problem Statement:**
Given a string `s`, partition it so every substring is a palindrome, and return all possible partitionings.

Example:
```
Input:  s = "aab"   ->  Output: [["a","a","b"],["aa","b"]]
```

**Solution:**
```python
# Time: O(2^n * n) | Space: O(n)

class Solution:
    result = []

    def partition(self, s: str) -> list[list[str]]:
        self.result = []
        if len(s) == 1:
            return [[s]]
        return self.valid_palindrome_partition(s[0:1]+"|"+s[1:])

    def is_valid_palindrome(self, arr: list) -> bool:
        def is_palindrome(s, l, r):
            if not s[l] == s[r]:
                return False
            if l < r:
                return is_palindrome(s, l+1, r-1)
            return True

        for item in arr:
            if not is_palindrome(item, 0, len(item)-1):
                return False
        return True

    def valid_palindrome_partition(self, cur_seq: str):
        if cur_seq[-1] == "|":
            temp_arr = cur_seq[:len(cur_seq)-1].split("|")
            if self.is_valid_palindrome(temp_arr):
                self.result.append(temp_arr)
            return

        index = cur_seq.rfind("|")
        self.valid_palindrome_partition(cur_seq[0:index+2]+"|"+cur_seq[index+2:])
        self.valid_palindrome_partition(cur_seq[0:index]+cur_seq[index+1:index+2]+"|"+cur_seq[index+2:])
        return self.result
```

---

#### 4. N-Queens

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Backtracking | Constraint Satisfaction | For each row, try placing queen in each column. Check if safe (no attacks): same column, diagonal, anti-diagonal. If safe, place queen and recurse to next row. BACKTRACK by removing queen | O(n!) | O(n) |

**Problem Statement:**
Place `n` queens on an `n x n` board so no two attack each other. Return all distinct solutions as board configurations.

Example:
```
Input:  n = 4   ->  Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
```

**Solution:**
```python
# Time: O(N!) | Space: O(N^2)
# repo places queens column by column, checking left / left-up / left-down rays

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["." for _ in range(n)] for _ in range(n)]
        result = []

        def can_queen_be_placed(row, col, grid):
            if row < 0 or col < 0 or row >= n or col >= n:
                return True
            if grid[row][col] == "Q":
                return False
            # left
            temp_col = col
            while temp_col >= 0:
                if grid[row][temp_col] == "Q":
                    return False
                temp_col -= 1
            # left-up diagonal
            temp_row, temp_col = row, col
            while temp_row >= 0 and temp_col >= 0:
                if grid[temp_row][temp_col] == "Q":
                    return False
                temp_row -= 1; temp_col -= 1
            # left-down diagonal
            temp_row, temp_col = row, col
            while temp_row < n and temp_col >= 0:
                if grid[temp_row][temp_col] == "Q":
                    return False
                temp_row += 1; temp_col -= 1
            return True

        def solveNQueensProblem(row, col, grid):
            if col == n:
                result.append(["".join(r) for r in grid])
                return
            if row == n:
                return
            if can_queen_be_placed(row, col, grid):
                grid[row][col] = "Q"
                solveNQueensProblem(0, col+1, grid)
                grid[row][col] = "."             # backtrack
                solveNQueensProblem(row+1, col, grid)
            else:
                solveNQueensProblem(row+1, col, grid)

        solveNQueensProblem(0, 0, grid)
        return result
```

---

### String

#### 1. Reverse Words in String

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| String | Two Pointers | Parse words from right to left, build result string | O(n) | O(n) |

**Problem Statement:**
Given an input string `s`, reverse the order of the words, collapsing multiple spaces and trimming leading/trailing spaces.

Example:
```
Input:  s = "the sky is blue"   ->  Output: "blue is sky the"
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        n = len(s)
        start, end = 0, 0
        while start < n:
            if s[start] == " ":
                start += 1
                end = start
                continue
            while not (end == n or s[end] == " "):
                end += 1
            res = s[start:end] + " " + res
            start = end

        return res[:-1]
```

---

### Stack & Queue

#### 1. Implement Stack using Arrays

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Stack | Array Implementation | Use array with top pointer, resize when needed | O(1) | O(n) |

**Problem Statement:**
Implement a stack (LIFO) with a fixed capacity supporting `push`, `pop`, `top`, `isEmpty`, and `isFull`.

**Solution:**
```python
# Time: O(1) per op | Space: O(n)

class Stack:
    def __init__(self, n: int):
        self.arr = []
        self.max_length = n

    def push(self, num: int):
        if len(self.arr) < self.max_length:
            self.arr.append(num)

    def pop(self) -> int:
        return self.arr.pop() if self.arr else -1

    def top(self) -> int:
        return self.arr[-1] if self.arr else -1

    def isEmpty(self) -> int:
        return 1 if len(self.arr) == 0 else 0

    def isFull(self) -> int:
        return 1 if len(self.arr) == self.max_length else 0
```

---

#### 2. Implement Queue using Array

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Queue | Circular Array | Use front and rear pointers, wrap around using modulo | O(1) | O(n) |

**Problem Statement:**
Implement a queue (FIFO) using an array, supporting `enqueue` and `dequeue` (returns `-1` if empty), each in O(1).

**Solution:**
```python
# Time: O(1) per op | Space: O(n)

class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.arr = [0] * 100001

    def enqueue(self, e: int) -> None:
        self.arr[self.rear] = e
        self.rear += 1

    def dequeue(self) -> int:
        if self.front == self.rear:
            return -1
        self.front += 1
        return self.arr[self.front-1]
```

---

#### 3. Implement Stack using Queue

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Stack | Queue Operations | Use one/two queues, move elements to simulate LIFO behavior | O(n) push | O(n) |

**Problem Statement:**
Implement a LIFO stack using only queues, supporting `push`, `pop`, `top`, and `empty`.

**Solution:**
```python
# Time: O(N) push | Space: O(N)

from collections import deque

class MyStack:
    def __init__(self):
        self.queue_1 = deque()
        self.queue_2 = deque()

    def push(self, x: int) -> None:
        self.queue_2.append(x)
        while self.queue_1:                       # move all elements behind x
            self.queue_2.append(self.queue_1.popleft())
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1

    def pop(self) -> int:
        return self.queue_1.popleft()

    def top(self) -> int:
        return self.queue_1[0]

    def empty(self) -> bool:
        return not self.queue_1
```

---

#### 4. Implement Queue using Stacks

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Queue | Stack Operations | Use two stacks: one for enqueue, transfer to other for dequeue | O(1) amortized | O(n) |

**Problem Statement:**
Implement a FIFO queue using only stacks, supporting `push`, `pop`, `peek`, and `empty`.

**Solution:**
```python
# Time: O(N) push | Space: O(N)

from collections import deque

class MyQueue:
    def __init__(self):
        self.stack_1 = deque()
        self.stack_2 = deque()

    def push(self, x: int) -> None:
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        self.stack_1.append(x)                    # new element goes to the bottom
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

    def pop(self) -> int:
        return self.stack_1.pop()

    def peek(self) -> int:
        return self.stack_1[-1]

    def empty(self) -> bool:
        return not self.stack_1
```

---

#### 5. Valid Parentheses

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Stack | Matching Pairs | Use stack to match opening brackets with closing ones | O(n) | O(n) |

**Problem Statement:**
Given a string of `()[]{}`, determine if it is valid (brackets closed by the same type in the correct order).

Example:
```
Input:  s = "()[]{}"   ->  Output: true
Input:  s = "(]"       ->  Output: false
```

**Solution:**
```python
# Time: O(n) | Space: O(n)

from collections import deque

def isValid(s: str) -> bool:
    stack = deque()
    for curr_char in s:
        if not len(stack) == 0:
            if (curr_char == "}" and stack[-1] == "{"
                    or curr_char == ")" and stack[-1] == "("
                    or curr_char == "]" and stack[-1] == "["):
                stack.pop()
                continue
        stack.append(curr_char)

    return len(stack) == 0
```

---

#### 6. Next Greater Element

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Stack | Monotonic Stack | Use stack to track elements waiting for next greater element | O(n) | O(n) |

**Problem Statement:**
Given `nums1` (a subset of `nums2`), for each element find its next greater element in `nums2`; `-1` if none.

Example:
```
Input:  nums1 = [4,1,2], nums2 = [1,3,4,2]   ->  Output: [-1,3,-1]
```

**Solution:**
```python
# Time: O(M+N) | Space: O(N+M)

from collections import deque

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = self.get_nge(nums2)
        return [nge.get(x) for x in nums1]

    def get_nge(self, nums):
        dq = deque()
        nge = {}
        for i in range(len(nums)-1, -1, -1):     # scan right to left
            nge[nums[i]] = -1
            while dq and dq[-1] <= nums[i]:
                dq.pop()
            if dq:
                nge[nums[i]] = dq[-1]
            dq.append(nums[i])
        return nge
```

---

#### 7. Sort a Stack

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Stack | Recursion | Use recursion to sort: remove top, sort remaining, insert in sorted position | O(n²) | O(n) |

**Problem Statement:**
Given a stack of `N` integers, sort it in descending order using recursion only (no loops).

Example:
```
Input:  [5,-2,9,-7,3]   ->  Output: [9,5,3,-2,-7]
```

**Solution:**
```python
# Time: O(N^2) | Space: O(N)

def sortStack(stack):
    sort_stack(stack)

def sort_stack(stack):
    if not stack:
        return
    temp = stack.pop()
    sort_stack(stack)
    fit_element(stack, temp)

def fit_element(stack, element):
    if not stack:
        stack.append(element)
        return
    if stack[-1] < element:
        stack.append(element)
    else:
        temp = stack.pop()
        fit_element(stack, element)
        stack.append(temp)
```

---

### Advanced Stack & Queue

#### 1. Next Smaller Element

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Stack | Monotonic Stack | Similar to next greater, but maintain increasing stack | O(n) | O(n) |

**Problem Statement:**
Given an array `a`, for each element check whether its immediate right element is smaller. If so, replace it with that element; otherwise `-1`. The last element becomes `-1`.

Example:
```
Input:  a = [4,7,8,2,3,1]   ->  Output: [-1,-1,2,-1,1,-1]
```

**Solution:**
```python
# Time: O(N) | Space: O(1)
# (repo solves the "immediate smaller element" variant in place)

def immediateSmaller(a: List[int]) -> None:
    n = len(a)
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i] = a[i+1]
        else:
            a[i] = -1
    a[n-1] = -1
```

---

#### 2. LRU Cache

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Design | Hash + Doubly LL | HashMap stores key->node mapping for O(1) access. Doubly LinkedList maintains usage order: head=most recent, tail=least recent. On GET: move to head. On PUT: add to head, remove tail if over capacity | O(1) | O(capacity) |

**Problem Statement:**
Design an LRU cache with `get` and `put` in O(1). On overflow, evict the least recently used key.

Example:
```
capacity=2; put(1,1); put(2,2); get(1)->1; put(3,3) evicts 2; get(2)->-1
```

**Solution:**
```python
# Time: O(1) get/put | Space: O(capacity)
# repo's clean version leans on Python's OrderedDict

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.ordered_dict = OrderedDict()
        self.capacity = capacity
        self.key_size = 0

    def get(self, key: int) -> int:
        value = self.ordered_dict.get(key)
        if value is None:
            return -1
        del self.ordered_dict[key]
        self.ordered_dict[key] = value       # move to most-recent end
        return value

    def put(self, key: int, value: int) -> None:
        if self.ordered_dict.get(key) is not None:
            del self.ordered_dict[key]
            self.key_size -= 1
        if self.key_size == self.capacity:
            self.ordered_dict.popitem(last=False)   # evict least recent
            self.key_size -= 1
        self.ordered_dict[key] = value
        self.key_size += 1
```

---

#### 3. Largest Rectangle in Histogram

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Stack | Next/Prev Smaller | For each bar, find area using next smaller and previous smaller elements | O(n) | O(n) |

**Problem Statement:**
Given histogram bar heights (width 1 each), return the area of the largest rectangle.

Example:
```
Input:  heights = [2,1,5,6,2,3]   ->  Output: 10
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        dq = deque()
        heights.append(float("-inf"))       # sentinel to flush the stack
        n = len(heights)

        area = 0
        for i in range(n):
            while dq and heights[dq[-1]] > heights[i]:
                cur_index = dq.pop()
                left_index = dq[-1] if dq else -1
                area = max(area, heights[cur_index]*(i-(left_index+1)))
            dq.append(i)

        heights.pop()
        return area
```

---

#### 4. Sliding Window Maximum

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Queue | Deque | Use deque to maintain decreasing order of elements in current window | O(n) | O(k) |

**Problem Statement:**
Given `nums` and window size `k`, return the maximum of each sliding window as it moves left to right.

Example:
```
Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3   ->  Output: [3,3,5,5,6,7]
```

**Solution:**
```python
# Time: O(n) | Space: O(n)

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()

        for i in range(len(nums)):
            while dq and nums[dq[-1]] < nums[i]:      # keep deque decreasing
                dq.pop()
            dq.append(i)

            window_start = i - (k - 1)
            while dq and dq[0] < window_start:        # drop indices out of window
                dq.popleft()

            if i >= k-1:
                result.append(nums[dq[0]])

        return result
```

---

#### 5. Min Stack

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Stack | Auxiliary Stack | Use additional stack to track minimum at each level | O(1) | O(n) |

**Problem Statement:**
Design a stack supporting `push`, `pop`, `top`, and `getMin` all in O(1).

Example:
```
push(-2); push(0); push(-3); getMin()->-3; pop(); top()->0; getMin()->-2
```

**Solution:**
```python
# Time: O(1) all ops | Space: O(N)

from collections import deque

class MinStack:
    def __init__(self):
        self.min_stack = deque()
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0 or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])   # carry current min

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack):
            return self.min_stack[-1]
```

---

#### 6. Rotten Oranges

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| BFS | Multi-source BFS | Start BFS from all rotten oranges simultaneously, track time | O(m*n) | O(m*n) |

**Problem Statement:**
In an `m x n` grid (0 empty, 1 fresh, 2 rotten), each minute fresh oranges adjacent to rotten ones rot. Return minutes until none are fresh, or `-1`.

Example:
```
Input:  grid = [[2,1,1],[1,1,0],[0,1,1]]   ->  Output: 4
```

**Solution:**
```python
# Time: O(m*n) | Space: O(m*n)

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        m, n = len(grid), len(grid[0])
        visited = [[False if grid[i][j] == 1 else True for j in range(n)] for i in range(m)]
        total_oranges = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    total_oranges += 1
                    dq.append((i, j, 0))
                if grid[i][j] == 1:
                    total_oranges += 1

        cur_time = 0
        total_queue_items = 0
        while dq:
            i, j, time = dq.popleft()
            cur_time = time
            total_queue_items += 1
            self.add_fresh_tomatoes_queue(dq, i-1, j, visited, m, n, cur_time)
            self.add_fresh_tomatoes_queue(dq, i, j+1, visited, m, n, cur_time)
            self.add_fresh_tomatoes_queue(dq, i+1, j, visited, m, n, cur_time)
            self.add_fresh_tomatoes_queue(dq, i, j-1, visited, m, n, cur_time)

        return cur_time if total_oranges == total_queue_items else -1

    def add_fresh_tomatoes_queue(self, dq, row_index, col_index, visited, m, n, cur_time):
        if 0 <= row_index < m and 0 <= col_index < n and not visited[row_index][col_index]:
            visited[row_index][col_index] = True
            dq.append((row_index, col_index, cur_time+1))
```

---

#### 7. Stock Span Problem

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Stack | Monotonic Stack | Use stack to store (price, index), find spans by comparing with previous greater elements | O(n) | O(n) |

**Problem Statement:**
Design a `StockSpanner`: for each day's price, return the number of consecutive days (up to today, going back) with price ≤ today's price.

Example:
```
next: 100,80,60,70,60,75,85   ->  spans: 1,1,1,2,1,4,6
```

**Solution:**
```python
# Time: O(N) amortized | Space: O(N)

from collections import deque

class StockSpanner:
    def __init__(self):
        self.dq = deque()
        self.count = 0

    def next(self, price: int) -> int:
        while self.dq and self.dq[-1][0] <= price:
            self.dq.pop()
        # distance to the previous strictly-greater price (or start)
        res = self.count - self.dq[-1][1] if self.dq else self.count + 1
        self.dq.append((price, self.count))
        self.count += 1
        return res
```

---

### Binary Search Tree

#### 1. Populate Next Right Pointers

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Tree | Level-order Traversal | Connect nodes at same level using BFS or recursion | O(n) | O(1) |

**Problem Statement:**
Given a perfect binary tree, populate each node's `next` pointer to point to its next right node at the same level (or `NULL`).

Example:
```
Input:  root = [1,2,3,4,5,6,7]   ->  each level linked left-to-right
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        dq = deque()
        prev_node_level = 0
        dq.append((root, prev_node_level))
        prev_node = None

        while dq:
            cur_node, cur_node_level = dq.popleft()
            if cur_node and cur_node.left and cur_node.right:
                dq.append((cur_node.left, cur_node_level+1))
                dq.append((cur_node.right, cur_node_level+1))
            if prev_node:
                prev_node.next = None if cur_node_level > prev_node_level else cur_node
            prev_node = cur_node
            prev_node_level = cur_node_level

        prev_node.next = None
        return root
```

---

#### 2. Search in BST

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| BST | Binary Search Property | Navigate left/right based on value comparison | O(log n) | O(log n) |

**Problem Statement:**
Given the root of a BST and an integer `val`, return the subtree rooted at the node with value `val`, or `null`.

Example:
```
Input:  root = [4,2,7,1,3], val = 2   ->  Output: [2,1,3]
```

**Solution:**
```python
# Time: O(log N) | Space: O(1)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if node.val < val:
                node = node.right
            elif node.val > val:
                node = node.left
            else:
                break
        return node
```

---

#### 3. Floor in BST

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| BST | Lower Bound | Track largest value <= target while traversing BST | O(log n) | O(log n) |

**Problem Statement:**
Given a BST and a value `X`, find the greatest node value that is smaller than or equal to `X` (the floor).

Example:
```
Input:  BST {2,5,6,10,15}, X = 7   ->  Output: 6
```

**Solution:**
```python
# Time: O(H) | Space: O(1)

def floorInBST(root, X):
    def floor_in_bst(node, floor):
        if not node:
            return floor
        if node.data > X:
            return floor_in_bst(node.left, floor)
        elif node.data < X:
            floor = node.data                # candidate; look right for a bigger valid one
            return floor_in_bst(node.right, floor)
        else:
            return node.data

    return floor_in_bst(root, -1)
```

---

### Binary Tree Advanced

#### 1. All Tree Traversals in One

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Tree Traversal | Single Function | Use one recursive function to build all three traversal lists | O(n) | O(n) |

**Problem Statement:**
Given a binary tree, return its in-order, pre-order, and post-order traversals — all computed in a single traversal.

Example:
```
Input:  tree 1(2, 3(6))   ->  in: [2,1,3,6]  pre: [1,2,3,6]  post: [2,6,3,1]
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

def getTreeTraversal(root):
    pre_order, in_order, post_order = [], [], []

    def single_traversal(cur_node):
        if not cur_node:
            return
        pre_order.append(cur_node.data)      # before going left
        single_traversal(cur_node.left)
        in_order.append(cur_node.data)       # between left and right
        single_traversal(cur_node.right)
        post_order.append(cur_node.data)     # after both children

    single_traversal(root)
    return [in_order, pre_order, post_order]
```

---

#### 2. Root to Node Path

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Tree Traversal | Path Tracking | Use recursion with path building to find all root-to-leaf paths | O(n) | O(h) |

**Problem Statement:**
Given a binary tree, find all root-to-leaf paths.

Example:
```
Input:  1(2, 3(4(_,5(_,7)), 6))   ->  Output: [[1,2],[1,3,4,5,7],[1,3,6]]
```

**Solution:**
```python
# Time: O(N) | Space: O(H)

class Solution:
    def Paths(self, root: Optional['Node']) -> List[List[int]]:
        res = []

        def in_order_path(cur_node, path):
            if not cur_node:
                return
            in_order_path(cur_node.left, path + [cur_node.data])
            if not cur_node.left and not cur_node.right:      # leaf -> record path
                res.append(path + [cur_node.data])
            in_order_path(cur_node.right, path + [cur_node.data])

        in_order_path(root, [])
        return res
```

---

#### 3. Left View Binary Tree

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Tree View | Level-order First | For each level, first node encountered is part of left view | O(n) | O(h) |

**Problem Statement:**
Given a binary tree, return its left view — the nodes visible when the tree is viewed from the left side.

Example:
```
Input:  1(2, 3(4(_,5(_,7)), 6))   ->  Output: [1,2,4,5,7]
```

**Solution:**
```python
# Time: O(n) | Space: O(h)

def LeftView(root):
    def left_view(res, cur_node=root, cur_level=0):
        if cur_node is None:
            return
        if cur_level == len(res):            # first node reached at this depth
            res.append(cur_node.data)
        left_view(res, cur_node.left, cur_level+1)
        left_view(res, cur_node.right, cur_level+1)

    res = []
    left_view(res)
    return res
```

---

#### 4. Bottom View Binary Tree

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Tree View | Horizontal Distance | Track rightmost node at each horizontal distance using level-order | O(n) | O(n) |

**Problem Statement:**
Given a binary tree, print its bottom view left to right (the last node seen at each horizontal distance).

Example:
```
Input:  2(7(2, 6(5, 11)), 5(_, 9(4, _)))   ->  Output: [2,5,6,4,9]
```

**Solution:**
```python
# Time: O(n) | Space: O(n)

from collections import deque

class Solution:
    def bottomView(self, root):
        if not root:
            return []

        queue = deque([(root, 0)])
        res_dict = {}
        while queue:
            cur_node, ver_level = queue.popleft()
            res_dict[ver_level] = cur_node.data      # overwrite -> keep the lowest node
            if cur_node.left:
                queue.append((cur_node.left, ver_level-1))
            if cur_node.right:
                queue.append((cur_node.right, ver_level+1))

        return [res_dict[index] for index in sorted(res_dict)]
```

---

#### 5. Top View Binary Tree

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Tree View | Horizontal Distance | Track first node at each horizontal distance using level-order | O(n) | O(n) |

**Problem Statement:**
Given a binary tree, print its top view (the first node seen at each horizontal distance from the top).

Example:
```
Input:  10(20(40,60), 30(90,100))   ->  Output: [40,20,10,30,100]
```

**Solution:**
```python
# Time: O(N) + O(K log K) | Space: O(N)

from collections import deque

class Solution:
    def topView(self, root):
        queue = deque()
        result_dict = {}
        queue.append((root, 0))

        while queue:
            cur_node, line = queue.popleft()
            if line not in result_dict:              # first node at this line stays
                result_dict[line] = cur_node.data
            if cur_node.left:
                queue.append((cur_node.left, line-1))
            if cur_node.right:
                queue.append((cur_node.right, line+1))

        return [result_dict[item] for item in sorted(result_dict)]
```

---

#### 6. Vertical Order Traversal

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Tree Traversal | Coordinates | Sort nodes by (col, row, value) to get vertical column-wise order | O(n log n) | O(n) |

**Problem Statement:**
Given a binary tree, return its vertical order traversal (columns left to right; within a column, top to bottom; ties in the same cell sorted by value).

Example:
```
Input:  root = [3,9,20,null,null,15,7]   ->  Output: [[9],[3,15],[20],[7]]
```

**Solution:**
```python
# Time: O(N) + O(K log K) | Space: O(N)

from collections import deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res_dict = {}
        queue = deque([(root, 0)])

        while queue:
            size = len(queue)
            row_dict = {}                    # values seen at this level, by column
            for _ in range(size):
                cur_node, ver_level = queue.popleft()
                if not row_dict.get(ver_level):
                    row_dict[ver_level] = [cur_node.val]
                    if not res_dict.get(ver_level):
                        res_dict[ver_level] = []
                else:
                    row_dict[ver_level].append(cur_node.val)
                if cur_node.left:
                    queue.append((cur_node.left, ver_level-1))
                if cur_node.right:
                    queue.append((cur_node.right, ver_level+1))

            for key in row_dict:
                if len(row_dict[key]) > 1:
                    row_dict[key] = sorted(row_dict[key])    # same cell -> sort by value
                res_dict[key] += row_dict[key]

        return [res_dict[key] for key in sorted(res_dict)]
```

---

#### 7. Maximum Width Binary Tree

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Tree Property | Level Indexing | Use position indices to calculate width, handle overflow with offset | O(n) | O(w) |

**Problem Statement:**
Given a binary tree, return its maximum width — the max over all levels of the distance between the leftmost and rightmost non-null nodes (counting the nulls between them).

Example:
```
Input:  root = [1,3,2,5,3,null,9]   ->  Output: 4
```

**Solution:**
```python
# Time: O(N) | Space: O(N)

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])           # (node, index as in a complete tree)
        res = 0

        while queue:
            min_s_no, max_s_no = None, None
            size = len(queue)
            for _ in range(size):
                cur_node, s_no = queue.popleft()
                min_s_no = s_no if (min_s_no is None) or (s_no < min_s_no) else min_s_no
                max_s_no = s_no if (max_s_no is None) or (s_no > max_s_no) else max_s_no
                if cur_node.left:
                    queue.append((cur_node.left, s_no * 2))
                if cur_node.right:
                    queue.append((cur_node.right, s_no * 2 + 1))

            res = max(res, max_s_no - min_s_no + 1)

        return res
```

---

### Heaps

#### 1. Implement Min Heap

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Heap | Array Implementation | Use array with heapify up/down, parent at (i-1)//2, children at 2*i+1, 2*i+2 | O(log n) | O(n) |

**Problem Statement:**
Implement a Min Heap supporting two queries: `0 X` inserts `X`; `1` prints and removes the minimum element.

Example:
```
Insert 2, Insert 1, ExtractMin -> 1
```

**Solution:**
```python
# Time: O(log N) per op | Space: O(N)

def minHeap(N: int, Q: [[]]) -> []:
    min_heap = []
    res = []

    def get_parent(i): return (i-1) // 2
    def get_left_child(i): return 2*i + 1
    def get_right_child(i): return 2*i + 2
    def is_index_in_heap(i): return 0 <= i < len(min_heap)

    def heapify(cur_index):                  # sift down
        left, right = get_left_child(cur_index), get_right_child(cur_index)
        smallest = cur_index
        if is_index_in_heap(left) and min_heap[left] < min_heap[smallest]:
            smallest = left
        if is_index_in_heap(right) and min_heap[right] < min_heap[smallest]:
            smallest = right
        if not smallest == cur_index:
            min_heap[cur_index], min_heap[smallest] = min_heap[smallest], min_heap[cur_index]
            heapify(smallest)

    def check_with_par(cur_index):           # sift up
        if cur_index <= 0:
            return
        par_index = get_parent(cur_index)
        if min_heap[par_index] > min_heap[cur_index]:
            min_heap[par_index], min_heap[cur_index] = min_heap[cur_index], min_heap[par_index]
            check_with_par(par_index)

    def insert(val):
        min_heap.append(val)
        check_with_par(len(min_heap)-1)

    def pop_min():
        if len(min_heap) == 1:
            return min_heap.pop()
        min_val = min_heap[0]
        min_heap[0] = min_heap.pop()
        heapify(0)
        return min_val

    for query in Q:
        if len(query) == 1:
            res.append(pop_min())
        else:
            insert(query[1])

    return res
```

---

### Graph Algorithms

#### 1. BFS

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Graph Traversal | Level-order | Use queue to visit nodes level by level | O(V+E) | O(V) |

**Problem Statement:**
Given an adjacency list of a graph with `n` vertices, return the BFS traversal starting from vertex 0.

Example:
```
Input:  adj = [[1,2,3],[2],[],[]]   ->  Output: [0,1,2,3]
```

**Solution:**
```python
# Time: O(N + 2E) | Space: O(N)

from collections import deque

def bfsTraversal(n: int, adj: List[List[int]]) -> List[int]:
    dq = deque()
    visited_nodes = [0] * n
    res = []
    dq.append(0)
    while dq:
        node = dq.popleft()
        if not visited_nodes[node]:
            visited_nodes[node] = 1
            res.append(node)
            for adjacent_node in adj[node]:
                dq.append(adjacent_node)
    return res
```

---

#### 2. DFS

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Graph Traversal | Depth-first | Use recursion or stack to go deep before exploring siblings | O(V+E) | O(V) |

**Problem Statement:**
Given a connected undirected graph, perform a DFS traversal from vertex 0.

Example:
```
Input:  V = 5, adj = [[2,3,1],[0],[0,4],[0],[2]]   ->  Output: [0,2,4,3,1]
```

**Solution:**
```python
# Time: O(V + 2E) | Space: O(V)

class Solution:
    def dfsOfGraph(self, V, adj):
        visited_nodes = [0] * V
        result = []

        def dfs(cur_node):
            if not visited_nodes[cur_node]:
                visited_nodes[cur_node] = 1
                result.append(cur_node)
                for adj_node in adj[cur_node]:
                    dfs(adj_node)

        for node in range(V):
            if not visited_nodes[node]:
                dfs(node)
        return result
```

---

#### 3. Cycle Detection (Undirected BFS)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Cycle Detection | BFS with Parent | If adjacent is visited and not parent, cycle exists | O(V+E) | O(V) |

**Problem Statement:**
Given an undirected graph with `V` vertices and `E` edges (no self-loops), return `true` if it contains a cycle (BFS, carrying each node's parent).

Example:
```
Input:  4 vertices, edges 0-1,1-2,2-3,3-0   ->  Output: True
```

**Solution:**
```python
# Time: O(N + 2E) | Space: O(N)

from collections import deque

def bfs(node, parent_node, node_graph, visited_nodes):
    dq = deque()
    dq.append((node, parent_node))
    while dq:
        cur_node, parent_node = dq[0][0], dq[0][1]
        if not visited_nodes[cur_node]:
            visited_nodes[cur_node] = 1
            dq.popleft()
            for adj_node in node_graph[cur_node]:
                if not adj_node == parent_node and not adj_node == cur_node:
                    dq.append((adj_node, cur_node))
        else:
            return True
    return False
```

---

#### 4. Cycle Detection (Undirected DFS)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Cycle Detection | DFS with Parent | If adjacent is visited and not parent, cycle exists | O(V+E) | O(V) |

**Problem Statement:**
Given an undirected graph with `V` vertices and `E` edges (no self-loops), return `true` if it contains a cycle (DFS passing the parent).

Example:
```
Input:  4 vertices, edges 0-1,1-2,2-3,3-0   ->  Output: True
```

**Solution:**
```python
# Time: O(N + 2E) | Space: O(N)

def dfs(node, parent_node, node_graph, visited_nodes):
    res = False
    if not visited_nodes[node]:
        visited_nodes[node] = 1
        for adj_node in node_graph[node]:
            if not adj_node == parent_node and not adj_node == node:
                if dfs(adj_node, node, node_graph, visited_nodes):
                    res = True
                    break
    else:
        res = True
    return res
```

---

#### 5. Cycle Detection (Directed DFS)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Cycle Detection | DFS with Colors | Use 3 colors: white (unvisited), gray (visiting), black (visited) | O(V+E) | O(V) |

**Problem Statement:**
Detect a cycle in a directed graph via Course Schedule: return `true` if all courses can be finished.

Example:
```
Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]   ->  Output: False
```

**Solution:**
```python
# Time: O(V+E) | Space: O(V+E)
# course_completed = black, per-DFS visited_nodes = gray

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        node_graph = [[] for i in range(numCourses)]
        for main_course, pre_req_course in prerequisites:
            node_graph[main_course].append(pre_req_course)

        course_completed = [0] * numCourses

        def courseFinish(node, visited_nodes):
            if course_completed[node]:
                return True
            if not course_completed[node] and visited_nodes[node]:
                return False                  # reached a gray node -> cycle
            visited_nodes[node] = 1
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

#### 6. Topological Sort (BFS - Kahn's)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Topological Sort | Indegree | Start with 0 indegree nodes, reduce indegree of neighbors | O(V+E) | O(V) |

**Problem Statement:**
Given a DAG with `V` vertices, return a topological ordering using Kahn's algorithm (BFS on in-degrees).

Example:
```
Input:  adj = [[],[0],[0],[0]]   ->  Output: [1,2,3,0]
```

**Solution:**
```python
# Time: O(V + E) | Space: O(E)

from collections import deque

class Solution:
    def topoSort(self, V, adj):
        in_degree = [0] * V
        dq = deque()
        result = []

        for i in range(len(adj)):
            for item in adj[i]:
                in_degree[item] += 1
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                dq.append(i)

        while dq:
            node = dq.popleft()
            for adj_node in adj[node]:
                in_degree[adj_node] -= 1
                if in_degree[adj_node] == 0:
                    dq.append(adj_node)
            result.append(node)

        return result
```

---

#### 7. Topological Sort (DFS)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Topological Sort | Finish Time | Add to result when finishing DFS (all neighbors processed) | O(V+E) | O(V) |

**Problem Statement:**
Given a DAG with `V` vertices and `E` edges, return any topological ordering using DFS.

Example:
```
Input:  edges 0->1, 0->2   ->  Output: [0,2,1] (one valid order)
```

**Solution:**
```python
# Time: O(V + E) | Space: O(V)

from collections import deque

def topologicalSort(adj, v, e):
    node_graph = [[] for i in range(v)]
    for item in adj:
        if item[0] is not None:
            node_graph[item[0]].append(item[1])

    visited_nodes = [0] * v
    dq = deque()

    def topoSort(node):
        if visited_nodes[node]:
            return
        visited_nodes[node] = 1
        for adj_node in node_graph[node]:
            topoSort(adj_node)
        dq.append(node)

    for cur_node in range(v):
        topoSort(cur_node)

    res = []
    while dq:
        res.append(dq.pop())         # reverse finish order
    return res
```

---

### Dynamic Programming

#### 1. Maximum Product Subarray

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Array DP | Track Min/Max | Track maxProduct and minProduct ending at current position. For each element: newMax = max(num, maxProduct*num, minProduct*num), newMin = min(num, maxProduct*num, minProduct*num). Update global max | O(n) | O(1) |

**Problem Statement:**
Given an integer array `nums`, find a contiguous subarray with the largest product and return that product.

Example:
```
Input:  nums = [2,3,-2,4]   ->  Output: 6
Input:  nums = [-2,0,-1]    ->  Output: 0
```

**Solution:**
```python
# Time: O(N) | Space: O(1)
# prefix/suffix products: a max product ends at some prefix or suffix boundary

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float("-inf")
        prefix = 1
        suffix = 1
        n = len(nums)

        for i in range(n):
            prefix = prefix * nums[i]
            suffix = suffix * nums[n-1-i]
            result = max(result, max(prefix, suffix))
            if prefix == 0:
                prefix = 1                 # reset across zeros
            if suffix == 0:
                suffix = 1

        return result
```

---

#### 2. Min Path Sum (Grid)

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| 2D DP | Path Optimization | dp[i][j] = grid[i][j] + min(top, left) | O(m*n) | O(m*n) |

**Problem Statement:**
Given an `m x n` grid of non-negative numbers, find a top-left to bottom-right path (moving right/down) minimizing the sum along it.

Example:
```
Input:  grid = [[1,3,1],[1,5,1],[4,2,1]]   ->  Output: 7
```

**Solution:**
```python
# Time: O(N*M) | Space: O(M*N)

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[-1]*n for _ in range(m)]

        def get_min_path_sum(i, j):
            if i >= m or j >= n:
                return float("inf")
            if i == m-1 and j == n-1:
                return grid[i][j]
            if not memo[i][j] == -1:
                return memo[i][j]
            memo[i][j] = grid[i][j] + min(get_min_path_sum(i, j+1), get_min_path_sum(i+1, j))
            return memo[i][j]

        return get_min_path_sum(0, 0)
```

---

### Trie

#### 1. Implement Trie

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trie | Prefix Tree | Use array of 26 children + end flag for each node | O(word_length) | O(total_chars) |

**Problem Statement:**
Implement a Trie with `insert`, `search` (exact word), and `startsWith` (prefix).

**Solution:**
```python
# Time: O(word_length) per op | Space: O(total_chars)

class Node:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False

    def contains_key(self, ch): return self.links[ord(ch)-ord("a")]
    def get(self, ch): return self.links[ord(ch)-ord("a")]
    def put(self, ch, node): self.links[ord(ch)-ord("a")] = node
    def set_end(self): self.flag = True
    def is_end(self): return self.flag

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
```

---

#### 2. Implement Trie II

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trie | Count Tracking | Add count variables to track word frequency and prefix count | O(word_length) | O(total_chars) |

**Problem Statement:**
Implement a Trie supporting `insert`, `countWordsEqualTo`, `countWordsStartingWith`, and `erase` (words may repeat).

**Solution:**
```python
# Time: O(word_length) per op | Space: O(total_chars)

class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.end_with = 0
        self.count_prefix = 0

    def contains_key(self, ch): return self.links[ord(ch)-ord("a")] is not None
    def get(self, ch): return self.links[ord(ch)-ord("a")]
    def put(self, ch, node): self.links[ord(ch)-ord("a")] = node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                node.put(cur_char, TrieNode())
            node = node.get(cur_char)
            node.count_prefix += 1
        node.end_with += 1

    def countWordsEqualTo(self, word):
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                return 0
            node = node.get(cur_char)
        return node.end_with

    def countWordsStartingWith(self, word):
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                return 0
            node = node.get(cur_char)
        return node.count_prefix

    def erase(self, word):
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                return
            node = node.get(cur_char)
            node.count_prefix -= 1
        node.end_with -= 1
```

---

#### 3. Longest String with All Prefixes

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trie | Prefix Chain | String is complete if all its prefixes exist in trie | O(total_chars) | O(total_chars) |

**Problem Statement:**
(Repo file solves *Longest Common Prefix* iteratively) Given an array of strings, find the longest common prefix among all of them.

Example:
```
Input:  ["applejuice","applepie","apple"]   ->  Output: "apple"
```

**Solution:**
```python
# Time: O(N*M) | Space: O(1)  (iterative scan variant in repo)

def longestCommonPrefix(arr, n):
    result = ""
    for i in range(len(arr[0])):
        fir_elem_char = arr[0][i]
        is_further_processing_req = True
        ind = 1
        while ind < len(arr):
            if i >= len(arr[ind]) or not arr[ind][i] == fir_elem_char:
                is_further_processing_req = False
                break
            ind += 1
        if not is_further_processing_req:
            break
        else:
            result += fir_elem_char
    return result
```

---

#### 4. Complete String

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trie | Prefix Validation | Check if every prefix of string exists as complete word in trie | O(total_chars) | O(total_chars) |

**Problem Statement:**
Given an array of strings, find the longest string such that every prefix of it is also present in the array. Ties broken lexicographically; return `None` if no such string exists.

Example:
```
Input:  ["n","ni","nin","ninj","ninja","ninga"]   ->  Output: "ninja"
```

**Solution:**
```python
# Time: O(N * Len) | Space: O(total_chars)

class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.is_end_flag = False

    def contains_key(self, ch): return self.links[ord(ch)-ord("a")] is not None
    def get(self, ch): return self.links[ord(ch)-ord("a")]
    def put(self, ch, node): self.links[ord(ch)-ord("a")] = node
    def set_end(self): self.is_end_flag = True
    def is_end(self): return self.is_end_flag

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                node.put(cur_char, TrieNode())
            node = node.get(cur_char)
        node.set_end()

    def search_complete_string(self, word):
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                return False
            node = node.get(cur_char)
            if not node.is_end():        # some prefix isn't itself a word
                return False
        return True

def completeString(n: int, a: List[str]) -> str:
    trie = Trie()
    for word in a:
        trie.insert(word)

    result = ""
    for word in a:
        if trie.search_complete_string(word):
            if len(word) > len(result):
                result = word
            elif len(word) == len(result):
                result = word if word < result else result

    return result if result else None
```

---

#### 5. Number of Distinct Substrings

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trie | Suffix Insertion | Insert all suffixes into trie, count total nodes created | O(n²) | O(n²) |

**Problem Statement:**
Given a string `S`, return the number of distinct substrings (including the empty substring) using a trie.

Example:
```
Input:  S = "abc"   ->  Output: 7
```

**Solution:**
```python
# Time: O(n^2) | Space: O(n^2)
# Insert every suffix into a trie; each new node created is one new distinct substring (+1 for empty).
# (repo file provides the count-tracking Trie building block used for this.)

class TrieNode:
    def __init__(self):
        self.links = [None] * 26

    def contains_key(self, ch): return self.links[ord(ch)-ord("a")] is not None
    def get(self, ch): return self.links[ord(ch)-ord("a")]
    def put(self, ch, node): self.links[ord(ch)-ord("a")] = node

def countDistinctSubstrings(s: str) -> int:
    root = TrieNode()
    count = 0
    for i in range(len(s)):
        node = root
        for j in range(i, len(s)):
            ch = s[j]
            if not node.contains_key(ch):
                node.put(ch, TrieNode())
                count += 1               # a new node == a new distinct substring
            node = node.get(ch)
    return count + 1                     # +1 for the empty substring
```

---

#### 6. Max XOR of Two Numbers

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trie | Bit Trie | Build binary trie, for each number find max XOR by going opposite bits | O(n*32) | O(n*32) |

**Problem Statement:**
Given an integer array `nums`, return the maximum value of `nums[i] XOR nums[j]`.

Example:
```
Input:  nums = [3,10,5,25,2,8]   ->  Output: 28
```

**Solution:**
```python
# Time: O(N*32) | Space: O(N*32)

class TrieNode:
    def __init__(self):
        self.links = [None]*2

    def contains_key(self, bit): return self.links[bit] is not None
    def get(self, bit): return self.links[bit]
    def put(self, bit, node): self.links[bit] = node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for cur_char in '{:032b}'.format(num):
            cur_bit = int(cur_char)
            if not node.contains_key(cur_bit):
                node.put(cur_bit, TrieNode())
            node = node.get(cur_bit)

    def find_max_xor(self, num):
        node = self.root
        result = ""
        for cur_char in '{:032b}'.format(num):
            cur_bit = int(cur_char)
            reverse_bit = 1 - cur_bit
            if node.contains_key(reverse_bit):
                result += "1"            # opposite bit maximizes XOR
                node = node.get(reverse_bit)
            else:
                result += "0"
                node = node.get(cur_bit)
        return int(result, 2)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)
        result = float("-inf")
        for num in nums:
            result = max(result, trie.find_max_xor(num))
        return result
```

---

#### 7. Max XOR with Element from Array

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Trie | Offline Queries | Sort queries by limit, add numbers to trie as limit increases | O(q*32 + n*32) | O(n*32) |

**Problem Statement:**
Given `nums` and queries `[xi, mi]`, for each query return the max `nums[j] XOR xi` over all `nums[j] <= mi`, or `-1` if none qualify.

Example:
```
Input:  nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]   ->  Output: [3,3,7]
```

**Solution:**
```python
# Time: O(N log N + Q log Q) | Space: O(N+M)
# reuses the bit-Trie above; process queries offline, sorted by limit

class Solution:
    def maximizeXor(self, nums: list[int], queries: list[List[int]]) -> list[int]:
        trie = Trie()
        for i in range(len(queries)):
            queries[i].append(i)              # remember original index

        queries.sort(key=lambda x: x[1])      # by limit m
        nums.sort()

        result = [-1]*len(queries)
        old_index = 0
        for item in queries:
            limit = item[1]
            while old_index < len(nums) and nums[old_index] <= limit:
                trie.insert(nums[old_index])
                old_index += 1
            original_index = item[2]
            if old_index == 0:
                result[original_index] = -1
            else:
                result[original_index] = trie.find_max_xor(item[0])
        return result
```

---
