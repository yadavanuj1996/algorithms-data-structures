"""
Combination Sum II

Problem Link:
https://leetcode.com/problems/combination-sum-ii

Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique 
combinations in candidates where the candidate numbers sum to target. Each number in candidates may only 
be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Constraints:
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

Test Case:

Input: candidates = [2,5,2,1,2], target = 5
Output: [ [1,2,2], [5] ]
"""

"""
Time Complexity: 
Space Complexity: 
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)        
        candidates.sort()
        def combination_sum_use_once(index, sum ,arr):
            if index == n:
                if sum == 0:
                    result.append(arr.copy())

                return 
                
            if sum < 0 or ():
                return 
            
            # pick
            combination_sum_use_once(index+1, sum - candidates[index], arr + [candidates[index]])
            # unpick
            while index + 1 < n and candidates[index] == candidates[index+1]:
                index += 1

            combination_sum_use_once(index+1, sum, arr)
        
        combination_sum_use_once(0, target ,[])
        
        return result

        