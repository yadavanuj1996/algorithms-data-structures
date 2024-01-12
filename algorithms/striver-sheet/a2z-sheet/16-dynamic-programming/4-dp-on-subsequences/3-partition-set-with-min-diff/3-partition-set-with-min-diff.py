"""
Array partition with minimum difference

Problem Link:
https://www.codingninjas.com/studio/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum._842494?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

Statement

You are given an array 'arr' containing 'n' non-negative integers.



Your task is to partition this array into two subsets such that the absolute difference between subset sums is minimum.



You just need to find the minimum absolute difference considering any valid division of the array elements.



Note:

1. Each array element should belong to exactly one of the subsets.

2. Subsets need not always be contiguous.
For example, for the array : [1, 2, 3], some of the possible divisions are 
   a) {1,2} and {3}
   b) {1,3} and {2}.

3. Subset-sum is the sum of all the elements in that subset. 

Constraints:
- 1 <= 'n' <= 10^3
- 0 <= 'arr'[i] <= 10^3
- 0 <= 𝚺 'arr'[i] <= 10^4, 

Test Case:

Input 2:
3
8 6 5

Output 2:
3

"""

from typing import List

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    n = len(arr)
    total_sum = sum(arr)
    dp = [[-1 for _ in range(total_sum + 1)] for _ in range(n)]


    def get_min_sum_difference(index, s1, s2):
        if index == n:
            return abs(s1 - s2)
        
        if not dp[index][s1] == -1:
            return dp[index][s1]
            
        # pick
        pick = get_min_sum_difference(index+1, s1 + arr[index], s2)
        unpick = get_min_sum_difference(index+1, s1, s2 + arr[index])
        dp[index][s1] = min(pick, unpick)
        return dp[index][s1]

    return get_min_sum_difference(0, 0, 0)


    




