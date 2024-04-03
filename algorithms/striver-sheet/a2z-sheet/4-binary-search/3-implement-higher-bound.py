"""
Implement Upper Bound

Problem Link:
https://www.naukri.com/code360/problems/implement-upper-bound_8165383

Statement
You are given a sorted array ‘arr’ containing ‘n’ integers and an integer ‘x’.
Implement the ‘upperBound’ function to find the index of the upper bound of 'x' in the array.

Note:
The upper bound in a sorted array is the index of the first value that is greater than a given value. 
If the greater value does not exist then the answer is 'n', Where 'n' is the size of the array.
We are using 0-based indexing.
Try to write a solution that runs in log(n) time complexity..

Constraints:
- 1 <= ‘n’ <= 10^5
- 1 <= ‘x’ <= 10^9
- 1 <= ‘arr[i]’ <= 10^9
- Time Limit: 1 sec

Test Case:

Sample Input 1:
5 7
1 4 7 8 10

Sample Output 1:
3   

Explanation of sample output 1:
In the given test case, the lowest value greater than 7 is 8 and is present at index 3(0-indexed). 

"""

"""
Time complexity: O(log n)
Space complexity: O(1)
"""
def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    result = n
    low = 0
    high = n - 1

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] <= x:
            low = mid + 1
        else:
            result = mid
            high = mid -1
        
    return result
