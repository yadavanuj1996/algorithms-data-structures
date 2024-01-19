"""
Immediate Smaller Element

Problem Link:
https://www.codingninjas.com/studio/problems/immediate-smaller-element-_1062597?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

Statement:
You are given an integer array 'a' of size 'n'.
For each element in the array, check whether the immediate right element of the array is smaller or not.

If the next element is smaller, update the current index to that element. If not, then -1. The last element
does not have any elements on its right.

Constraints:
- 1 <= 'n' <= 10 ^ 5
- 1 <= 'a[i]' <= 10 ^ 9
- Time Limit : 1 sec

Test Case:

Input:
6
4 7 8 2 3 1

Output:
-1 -1 2 -1 1 -1 

"""
"""
Time Complexity: O(N)
Space Complexity: O(1) , no extra space used
"""
from typing import List

def immediateSmaller(a: List[int]) -> None:
    # Write your code here
    n = len(a)
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i] = a[i+1]
        else:
            a[i] = -1
    
    a[n-1] = -1
