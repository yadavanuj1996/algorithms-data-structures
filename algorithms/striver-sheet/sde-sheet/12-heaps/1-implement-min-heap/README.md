## minHeap Algorithm Summary

The `minHeap` function handles a series of heap operations efficiently, supporting insertion and extraction of the minimum element from a min-heap data structure.

### Algorithm Description

1. **Initialization**:
   - Initialize an empty list `min_heap` to represent the heap.
   - Initialize an empty list `res` to store the results of queries.

2. **Helper Functions**:
   - `get_parent(child_index)`: Returns the index of the parent node for a given child node.
     - Formula: \((\text{child_index} - 1) // 2\)

   - `get_left_child(par_index)`: Returns the index of the left child for a given parent node.
     - Formula: \(2 \times \text{par_index} + 1\)

   - `get_right_child(par_index)`: Returns the index of the right child for a given parent node.
     - Formula: \(2 \times \text{par_index} + 2\)

   - `is_index_in_heap(cur_index)`: Checks if a given index is within the heap bounds.
     - Condition: \(\text{cur_index} < \text{len(min_heap)}\) and \(\text{cur_index} \geq 0\)

   - `heapify(cur_index)`: Ensures the heap property is maintained starting from a given index downwards.
     - Find the indices of the left and right children of `cur_index`.
     - Determine if these child indices are within the heap bounds.
     - Identify the smallest value among the current node and its children.
     - If the smallest value is not the current node, swap the current node with the smallest child and recursively call `heapify` on the affected child index.

   - `check_with_par(cur_index)`: Ensures the heap property is maintained starting from a given index upwards.
     - If the current index is not the root, find the parent index.
     - If the parent's value is greater than the current node's value, swap them and recursively call `check_with_par` on the parent index.

   - `insert(val)`: Inserts a new value into the heap and maintains the heap property.
     - Append the new value to the end of `min_heap`.
     - Call `check_with_par` to ensure the heap property is maintained.

   - `pop_min()`: Removes and returns the minimum element from the heap, maintaining the heap property.
     - If the heap has only one element, remove and return it.
     - Replace the root of the heap with the last element.
     - Call `heapify` on the root to maintain the heap property.
     - Return the removed minimum value.

3. **Processing Queries**:
   - Iterate through the list of queries.
   - For a query with a single element, extract the minimum element using `pop_min()` and append the result to `res`.
   - For a query with two elements, insert the given value into the heap using `insert(val)`.

4. **Return Result**:
   - Return the list `res` containing the results of the extraction queries.

### Time and Space Complexity

- **Time Complexity**:
  - Insertion (`insert(val)`): O(log N), where N is the number of elements in the heap.
  - Extraction (`pop_min()`): O(log N), where N is the number of elements in the heap.
  - The overall time complexity for processing all queries depends on the number of insertions and extractions, typically O(Q log N), where Q is the number of queries.

- **Space Complexity**:
  - The space complexity is O(N), where N is the number of elements stored in the heap at any given time.

### Code with Detailed Explanation

```python
from sys import *
from collections import *
from math import *
from heapq import *

def minHeap(N: int, Q: [[]]) -> []:

    min_heap = []
    res = []
    
    # Get the parent index of a child node
    def get_parent(child_index):
        return (child_index - 1) // 2
    
    # Get the left child index of a parent node
    def get_left_child(par_index):
        return 2 * par_index + 1
    
    # Get the right child index of a parent node
    def get_right_child(par_index):
        return 2 * par_index + 2
    
    # Check if the index is within the bounds of the heap
    def is_index_in_heap(cur_index):
        return 0 <= cur_index < len(min_heap)

    # Ensure the heap property is maintained from cur_index downwards
    def heapify(cur_index):
        left_child = get_left_child(cur_index)
        right_child = get_right_child(cur_index)
        is_left_child_present = is_index_in_heap(left_child)
        is_right_child_present = is_index_in_heap(right_child)

        smallest = cur_index  # Index with the smallest value among the current node and its children

        if is_left_child_present and min_heap[left_child] < min_heap[smallest]:
            smallest = left_child
        
        if is_right_child_present and min_heap[right_child] < min_heap[smallest]:
            smallest = right_child

        if smallest != cur_index:
            # Swap the current node with the smallest child and heapify the affected subtree
            min_heap[cur_index], min_heap[smallest] = min_heap[smallest], min_heap[cur_index]
            heapify(smallest)
        

    # Ensure the heap property is maintained from cur_index upwards
    def check_with_par(cur_index):
        if cur_index <= 0:
            return 

        par_index = get_parent(cur_index)

        if min_heap[par_index] > min_heap[cur_index]:
            # Swap the current node with its parent and continue checking up the tree
            min_heap[par_index], min_heap[cur_index] = min_heap[cur_index], min_heap[par_index]
            check_with_par(par_index)

    # Insert a new value into the heap and maintain the heap property
    def insert(val):
        min_heap.append(val)
        check_with_par(len(min_heap) - 1)

    # Remove and return the minimum element from the heap, maintaining the heap property
    def pop_min():
        if len(min_heap) == 1:
            return min_heap.pop()

        min_val = min_heap[0]
        min_heap[0] = min_heap.pop()
        heapify(0)
        return min_val

    # Process each query
    for query in Q:
        if len(query) == 1:
            res.append(pop_min())
        else:
            insert(query[1])
            
    return res
```
