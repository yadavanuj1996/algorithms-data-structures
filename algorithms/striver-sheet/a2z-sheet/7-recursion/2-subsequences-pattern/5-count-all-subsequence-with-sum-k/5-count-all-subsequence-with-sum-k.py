"""
Subarrays with Sum k

Problem Link:
https://www.codingninjas.com/studio/problems/subarrays-with-sum-%E2%80%98k'_6922076

Statement
You are given an array 'A' of size 'N' and an integer'K'. You need to generate and return all subarrays
of array A whose sum = K.

Note: In the output, you will see the 2D array lexicographically sorted.

Example:
Input: N = 6 K = 3
A = [1, 2, 3, 1, 1, 1]
Output: 3
Explanation: Subarrays whose sum = 3 are:
[1, 2], [3], and [1, 1, 1]


Constraints:
1 <= 'N' <= 20
- Time limit: 1 second

Test Case:

Sample Input 1:
6 3
1 2 3 1 1 1

Sample Output 1:
3

Explanation Of Sample Input 1:

Input: N = 6 K = 3
A = [1, 2, 3, 1, 1, 1]
Output: 3
Explanation: Subarrays whose sum = 3 are:
[1, 2], [3], and [1, 1, 1]
"""



"""
Brute Force Solution (Not all test cases will pass)

Time Complexity: O(N^2)
Space Complexity: O(N) 


def subarraysWithSumK( a:[int], k:int) ->[[int]]:
    # Write your code here
    result = []
    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            
            if sum == k:
                result.append(a[i:j+1])
    
    return result
"""


"""
Two pointer Recursion based Solution
Time complexity: O(n)
Space Complexity: O(n)

def subarraysWithSumK( a:[int], k:int) ->[[int]]:
        result = []
        n = len(a)
        def subarray_with_sum_k(start, end, sum):
            if start >= n or end >= n:
                return 

            if sum <= k:
                if sum == k:
                    result.append(a[start:end+1])
                    
                if end + 1 == n:
                    return

                subarray_with_sum_k(start, end+1, sum + a[end+1])
            elif sum > k:
                subarray_with_sum_k(start+1, end, sum - a[start])
           
        subarray_with_sum_k(0,0,a[0])
        #print(result)
        return result

"""


"""
Prefix sum approach 
Time Complexity: O(N)
Space Complexity: O(N) 
"""

def subarraysWithSumK( a:[int], k:int) ->[[int]]:
    # Write your code here
    pre_sum = 0 # prefix sum
    old_pre_sums = {0: -1}
    result = []
    for i in range(len(a)):
        pre_sum += a[i]
        if pre_sum - k in old_pre_sums:
            result.append(a[old_pre_sums[pre_sum - k]+1:i+1])

        old_pre_sums[pre_sum] = i

    return result
            

