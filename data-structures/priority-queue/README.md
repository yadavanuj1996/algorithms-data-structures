## Priority Queue in Python

A priority queue is a data structure where each element has a "priority" associated with it. Elements are served based on their priority: the element with the highest priority is served before other elements with lower priority. In a min-heap, the element with the smallest value has the highest priority.

### How Priority Queue Works Using Python

In Python, the `heapq` module provides an implementation of the priority queue using a binary heap. The heap is a complete binary tree where each node is smaller than or equal to its children. The smallest element is at the root, making it a min-heap.

### Key Operations

1. **Insertion**:
   - Adding a new element to the heap while maintaining the heap property.

2. **Extraction**:
   - Removing and returning the smallest element from the heap, then reheapifying to maintain the heap property.

3. **Peek**:
   - Accessing the smallest element without removing it.

### Functions in `heapq` Module

- `heapq.heappush(heap, item)`: Adds `item` to the `heap`.
- `heapq.heappop(heap)`: Removes and returns the smallest item from the `heap`.
- `heapq.heapify(list)`: Converts a list into a heap, in-place, in linear time.
- `heapq.heappushpop(heap, item)`: Pushes a new item on the heap, then pops and returns the smallest item from the heap.
- `heapq.heapreplace(heap, item)`: Pops and returns the smallest item from the heap, then pushes the new item.

### Examples

#### Example 1: Basic Operations

```python
import heapq

# Create an empty min-heap
min_heap = []

# Insert elements
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 5)

print("Heap after insertions:", min_heap)  # Output: [1, 1, 4, 3, 5]

# Extract the smallest element
smallest = heapq.heappop(min_heap)
print("Smallest element:", smallest)  # Output: 1
print("Heap after extraction:", min_heap)  # Output: [1, 3, 4, 5]

# Peek at the smallest element without popping
print("Smallest element:", min_heap[0])  # Output: 1
```

#### Example 2: Using `heapify`

```python
import heapq

# Create a list
data = [9, 5, 1, 3, 7, 2]

# Convert the list into a heap
heapq.heapify(data)
print("Heap:", data)  # Output: [1, 3, 2, 5, 7, 9]

# Extract the smallest element
smallest = heapq.heappop(data)
print("Smallest element:", smallest)  # Output: 1
print("Heap after extraction:", data)  # Output: [2, 3, 9, 5, 7]
```

### Applications of Priority Queues

1. **Dijkstra's Algorithm**:
   - Finding the shortest path in a graph.


## Problem solved using Priority Queue

### Lexicographically Minimum String After Removing Stars

##### Problem Description

You are given a string `s` that may contain any number of '*' characters. Your task is to remove all '*' characters by repeatedly performing the following operation:
- Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.

Return the lexicographically smallest resulting string after removing all '*' characters.

### Examples

#### Example 1
- **Input**: `s = "aaba*"`
- **Output**: `"aab"`
- **Explanation**: We should delete one of the 'a' characters with '*'. If we choose `s[3]`, `s` becomes the lexicographically smallest.

#### Example 2
- **Input**: `s = "abc"`
- **Output**: `"abc"`
- **Explanation**: There is no '*' in the string.

### Constraints

- (1 <= s.length <= 10^5)
- `s` consists only of lowercase English letters and '*'.
- The input is generated such that it is possible to delete all '*' characters.

```
from heapq import *


class Solution:
    def clearStars(self, s: str) -> str:
        priority_queue = []
        temp_s = s
        index_to_remove = set()

        for i in range(len(temp_s)):
            ch = temp_s[i]
            if ch == "*":
                # updating index_to_remove dict to remove this index later
                index_to_remove.add(i)
                _, index = heappop(priority_queue)
                index = -index
                # updating index_to_remove dict to remove this index later
                index_to_remove.add(index)
            else:
                # priority queue holds (ascii_value, -index), storing index as negative
                # as in case two occurences of char i want the rightmose val
                heappush(priority_queue, (ord(ch), -i))
        
        res = ""
        for index in range(len(temp_s)):
            if index not in index_to_remove:
                res += temp_s[index]
        
        return res

```

### Summary

A priority queue is an efficient data structure for managing a collection of elements with associated priorities. Python's `heapq` module 
provides a robust and efficient implementation of a min-heap-based priority queue, supporting essential operations such as insertion and 
extraction.

Understanding and utilizing these operations allows for efficient management of priority-based tasks in various applications.
