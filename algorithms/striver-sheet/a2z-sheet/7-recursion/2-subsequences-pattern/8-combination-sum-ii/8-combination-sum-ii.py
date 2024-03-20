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
Approach 1: try all combinations (loop thorugh the indexes)

Time Complexity:  O(2^n*k)
Space Complexity: O(k*x)

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)        
        candidates.sort()
        def combination_sum_use_once(index, sum ,arr):
            print(index, sum , arr)
            if sum == 0:
                result.append(arr[:])
                return 

            if sum < 0:
                return 
            
            for i in range(index, n):
                if i > index and i < n and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > target:
                    break
                
                combination_sum_use_once(i+1, sum-candidates[i] ,arr+[candidates[i]])
        
        combination_sum_use_once(0, target ,[])
        return result
                

            


"""

"""
Approach 2: Pick / unpick
Time Complexity:  O(2^n*k) ,  Reason: Assume if all the elements in the array are unique then the no. of subsequence you will get will be O(2^n). we also add the ds to our ans when we reach the base case that will take “k”//average space for the ds.
Space Complexity: O(k*x)
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
                
            if sum < 0:
                return 
            
            # pick
            combination_sum_use_once(index+1, sum - candidates[index], arr + [candidates[index]])
            # unpick
            while index + 1 < n and candidates[index] == candidates[index+1]:
                index += 1

            combination_sum_use_once(index+1, sum, arr)
        
        combination_sum_use_once(0, target ,[])
        
        return result

        