"""
Subset Sum

Problem Link:
https://www.codingninjas.com/studio/problems/subset-sum_3843086

Statement
You are given an array 'nums' of n integers. Return all subset sums of 'nums' in a non-decreasing order.

Note:
Here subset sum means sum of all elements of a subset of 'nums'. A subset of 'nums' is an array formed 
by removing some (possibly zero or all) elements of 'nums'.


For example
Input: 'nums' = [1,2]

Output: 0 1 2 3


Constraints:
- 1 <= n <= 15
- 0 <= nums[i] <= 5000

Test Case:

3
1 2 3
Sample output 1 :
0 1 2 3 3 4 5 6
"""

"""
Time Complexity: O(2^n)+O(2^n log(2^n)). Each index has two ways. You can either pick it up or not pick it. So for n index time complexity for O(2^n) and for sorting it will take (2^n log(2^n)).
Space Complexity: O(2^n) for storing subset sums, since 2^n subsets can be generated for an array of size n.
"""
from sys import *
from collections import *
from math import *

from typing import List


def subsetSum(num: List[int]) -> List[int]:
    # Write your code here.
    n = len(num)
    result = []
    def sum_of_subset(index, num, sum):
        if index == n:
            result.append(sum)
            return
        
        #pick 
        sum_of_subset(index+1, num, sum + num[index])
        #unpick
        sum_of_subset(index+1,num, sum)
    
    sum_of_subset(0,num, 0)
    result.sort()
    return result





        