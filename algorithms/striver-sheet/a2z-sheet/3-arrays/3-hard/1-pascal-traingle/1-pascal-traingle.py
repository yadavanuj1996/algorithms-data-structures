"""
Pascal's Triangle

Problem Link:
https://leetcode.com/problems/pascals-triangle/

Statement
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above

Constraints:
- 1 <= numRows <= 30


Test Case:
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

"""

class Solution:
    """
    Approach 1: factorial calculation in array approach
    Time Complexity: O(n^2)
    Space Complexity: O(n^2) + O(n), o(n^2) is for storing result and O(n) for saving factorial values
    we need to imporve the SC as array used for storing cannot be changed but we can imporve by not using
    array to store factorial values

    def generate(self, numRows: int) -> List[List[int]]:
        fact = [1] * (numRows+1)
        res = [[] for _ in range(numRows)]

        for n in range(numRows):
            # calculating factorial value
            if n > 0:
                fact[n] = fact[n-1] * n
            # calculating the pascal triangle place value using factorial
            for r in range(n+1):
                val = fact[n] // (fact[n-r] * fact[r])
                res[n].append(val)    
                
        return res
    """
    
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n^2) , o(n^2) is for storing, improvement of O(n) SC as we are not using
    an array to store fact value in this solution
    """
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for r in range(numRows):
            # appending the first val 1
            res.append([1])
            # calculating factorial value
            ans = 1
            
            # calculating the pascal triangle place value using factorial
            for c in range(1, r+1):
                ans = ans * (r-c+1)
                ans = ans // c
                res[r].append(ans)    
                
        return res



       