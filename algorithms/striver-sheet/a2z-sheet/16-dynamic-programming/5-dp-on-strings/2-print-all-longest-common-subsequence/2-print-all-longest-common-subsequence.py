"""
Print all LCS sequences

Problem Link:
https://www.geeksforgeeks.org/problems/print-all-lcs-sequences3413/1

Statement
You are given two strings s and t. Now your task is to print all longest common sub-sequences in 
lexicographical order.

Note -  A Sub-sequence is derived from another string by deleting some or none of the elements without 
changing the order of the remaining elements.


Constraints:
- 1 ≤ Length of both strings ≤ 50

Test Case:

Input: s = abaaa, t = baabaca
Output: aaaa abaa baaa
Explanation - Length of lcs is 4, in lexicographical order they are aaaa, abaa, baaa

"""


"""
Time Complexity: O(N*M) 
Space Complexity: O(N*M) + O(N+M) , O(N*M) for dp array, O(N+M) for auxillary stack space

"""
class Solution:
    def all_longest_common_subsequences(self, s, t):
        # dp[i][j] represents value of common subsequence between two strings
        # for first string text1 (0 -> i) index and for second string text2 (0->j)
        text1 = s
        text2 = t
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        
        # Step1: Set up base that i.e., for 0th row and 0th col the dp val will be 0(shifting the -ve to 0 index by 1)
        for ind in range(n+1):
            dp[ind][0] = 0

        for ind in range(m+1):
            dp[0][ind] = 0

        # Step 2 iterate over the indexes in reverese order
        # We are starting from 1 as we have shifted indexes and took -1 to 0, 0 to 1 so on
        for i in range(1, n+1):
            for j in range(1, m+1):
                # Step 3 : Copy the recurrence
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0 + max(dp[i-1][j], dp[i][j-1])
            
        
        res_len = dp[n][m]
        res = set()
        
        def add_answer(row, col, temp_str=""):
                    
            while row > 0 and col > 0:
                if text1[row-1] == text2[col-1]:
                    temp_str = text1[row-1] + temp_str
                    row -= 1
                    col -= 1
                else:
                    if dp[row-1][col] > dp[row][col-1]:
                        row -=1
                    elif dp[row-1][col] < dp[row][col-1]:
                        col -= 1
                    # if both top and left side of array element is same
                    # that means there are two lcs of same len that includes
                    # the current selected subseqeuence at the end
                    elif dp[row-1][col] == dp[row][col-1]:
                        add_answer(row-1, col, temp_str)
                        add_answer(row, col-1, temp_str)
                        return 
                    
            res.add(temp_str)
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if dp[i][j] == res_len and text1[i-1] == text2[j-1]:
                    add_answer(i, j)
                    
        #res.sort()
        
        return sorted(res)
                    
   