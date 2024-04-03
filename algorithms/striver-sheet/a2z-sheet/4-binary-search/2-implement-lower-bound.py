"""
Implement Lower Bound

Problem Link:
https://www.naukri.com/code360/problems/lower-bound_8165382

Statement
You are given an array 'arr' sorted in non-decreasing order and a number 'x'.
You must return the index of lower bound of 'x'.

Note:
For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 'idx' such that the 
value 'arr[idx]' is not less than 'x'
If all numbers are smaller than 'x', then 'n' should be the 'lower_bound' of 'x', where 'n' is the size of array.
Consider 0-based indexing.



Constraints:
- 1 <= ‘n’ <= 10^5
- 0 <= ‘arr[i]’ <= 10^5
- 1 <= ‘x’ <= 10^5


Test Case:
Sample Input 1:
6
1 2 2 3 3 5
0

Sample Output 1:
0

Explanation Of Sample Input 1 :
Index '0' is the smallest index such that 'arr[0]' is not less than 'x'.

"""

"""
Time complexity: O(log n)
Space complexity: O(1)
"""
def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    
    low = 0
    high = n - 1
    res = n
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] < x:
            low = mid + 1
            
        
        if  arr[mid] >= x:
            res = mid
            high = mid - 1
        
    return res
        












            
