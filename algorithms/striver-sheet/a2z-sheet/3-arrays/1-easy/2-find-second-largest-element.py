""" 
Second Largest Element

Problem Link:
https://www.geeksforgeeks.org/problems/second-largest3735/1

Statement
Given an array Arr of size N, print the second largest distinct element from an array. 
If the second largest element doesn't exist then return -1.

Constraints:
- 2 ≤ N ≤ 10^5
- 1 ≤ Arr[i] ≤ 10^5

Test Case:

Input: 
N = 6
Arr[] = {12, 35, 1, 10, 34, 1}

Output: 34

Explanation: The largest element of the 
array is 35 and the second largest element
is 34.
"""

"""
Time Complexity: O(N) 
Space Complexity: O(1)
"""

def secondSmallest(arr, n):
    if (n < 2):
        return -1
    small = float('inf')
    second_small = float('inf')
    for i in range(n):
        if (arr[i] < small):
            second_small = small
            small = arr[i]
        elif (arr[i] < second_small and arr[i] != small):
            second_small = arr[i]
    return second_small


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


        

        