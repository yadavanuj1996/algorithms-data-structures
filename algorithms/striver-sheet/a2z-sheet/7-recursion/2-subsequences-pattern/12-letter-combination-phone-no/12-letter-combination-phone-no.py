"""
Combination Sum III

Problem Link:
https://leetcode.com/problems/combination-sum-iii/

Statement
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used. Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, 
and the combinations may be returned in any order.

Constraints:
- 2 <= k <= 9
- 1 <= n <= 60


Test Case:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]

Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
"""

"""
Approach 1: Simple pick/ unpick approach with digit in arr
Time Complexity:
Space Complexity:

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result= []
        input = [1,2,3,4,5,6,7,8,9]
        size = len(input)

        def combination_sum_3(index, sum, arr):
            if sum < 0 or len(arr) > k:
                return

            if index == size:
                if sum == 0 and len(arr) == k:
                    print(arr)
                    result.append(arr.copy())

                return
            
            # pick 
            combination_sum_3(index+1, sum-input[index], arr+[input[index]])
            # unpick
            combination_sum_3(index+1, sum, arr)
        
        combination_sum_3(0, n, [])
        return result
            

"""


"""
Time complexity: O(2^9)
Space complexity: O(k)
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result= []
        size = 10

        def combination_sum_3(index, sum, arr):
            if sum < 0 or len(arr) > k:
                return

            if index == size:
                if sum == 0 and len(arr) == k:
                    result.append(arr.copy())

                return
            
            # pick 
            combination_sum_3(index+1, sum - index, arr+[index])
            # unpick
            combination_sum_3(index+1, sum, arr)
        
        combination_sum_3(1, n, [])
        return result
            
                
            

            

            
            
