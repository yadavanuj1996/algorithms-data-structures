"""
Min Heap

Problem Link:
https://www.naukri.com/code360/problems/min-heap_4691801

Statement
Implement the Min Heap data structure.

You will be given 2 types of queries:-
0 X

Insert X in the heap.
1
Print the minimum element from the heap and remove it.


Constraints:
- 1 <= T <= 5
- 1 <= N <= 10^5
- 1 <= X <= 50
- Time Limit: 1 sec


Test Case:

Sample Input 1 :
2
3
0 2
0 1
1
2
0 1
1

Sample Output 1 :
1
1
"""

"""
Time complexity:
- Insertion  (insert(val)): O(log N), where N is the number of elements in the heap.
- Extraction (pop_min()):   O(log N), where N is the number of elements in the heap.
- The overall time complexity for processing all queries depends on the number of insertions and extractions, typically O(Q log N), where Q is the number of queries.

Space Complexity: The space complexity is O(N), where N is the number of elements stored in the heap at any given time.

"""
from sys import *
from collections import *
from math import *
from heapq import *

def minHeap(N: int, Q: [[]]) -> []:

    min_heap = []
    res = []
    
    def get_parent(child_index):
        return (child_index-1) // 2
    
    def get_left_child(par_index):
        return 2*par_index + 1
    
    def get_right_child(par_index):
        return 2*par_index + 2
    
    def is_index_in_heap(cur_index):
        if cur_index < len(min_heap) and cur_index >= 0:
            return True
        
        return False

    def heapify(cur_index):
        left_child = get_left_child(cur_index)
        right_child = get_right_child(cur_index)
        is_left_child_present = is_index_in_heap(left_child)
        is_right_child_present = is_index_in_heap(right_child)

        smallest = cur_index # this will represent the index with min val between the par and both children

        if is_left_child_present and min_heap[left_child] < min_heap[smallest]:
            smallest = left_child
        
        if is_right_child_present and min_heap[right_child] < min_heap[smallest]:
            smallest = right_child

        if not smallest == cur_index:
            min_heap[cur_index], min_heap[smallest] =  min_heap[smallest], min_heap[cur_index]
            heapify(smallest)
        

    def check_with_par(cur_index):
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
