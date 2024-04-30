""" 
Count Of Greater Elements To The Right

Problem Link:
https://www.naukri.com/code360/problems/count-of-greater-elements-to-the-right_8365436

Statement
You are given an array 'arr' of length 'N'.
You are given 'Q' queries, and for each query, you are given an index(0-based indexing).

Answer to each query is the number of the strictly greater elements to the right of the given index 
element.

You must return an array 'answer' of length ’N’, where ‘answer[i]’ is the answer to the ‘ith’ query.


Constraints:
- 1 <= N <= 10^4
- 1 <= Q <= 100
- 1 <= arr[i] <= 10^5.
- 0 <= query[i] <= ‘N’-1
- Time Limit: 1 sec

Test Case:
Sample Input 1:

arr = [5, 2, 10, 4], N=4, Q=2, query = [0, 1]
Output:
1 2

Explanation: The element at index 0 is 5 for the first query. There is only one element greater than 5 towards the right, i.e., 10.
For the second query, the element at index 1 is 2. There are two elements greater than 2 towards the right, i.e., 10 and 4. 

Sample Input 2:

Sample Input 1:
8 3
1 3 6 5 8 9 13 4
0 1 5

Sample Output 1:
7 6 1

"""

"""
Time Complexity: O(N*Q) 
Space Complexity: O(Q)
"""
from typing import *

def countGreater(N: int, Q: int, arr: List[int], query: List[int]) -> List[int]:
    # Write your code here
    res = [0] * Q
    for q_ind in range(Q):
        cur_q = query[q_ind]

        for i in range(cur_q+1, N):
            if arr[cur_q] < arr[i]:
                res[q_ind] += 1
        
    return res

