"""
TC: O(k * 2^(n + k))
SC: O(n + k^2)
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []

        def combination_sum(cur_index, cur_arr=[], cur_sum=0):
            if cur_index >= n:
                return

            if cur_sum > target:
                return

            if cur_sum == target:
                res.append(cur_arr)
                return

            cur_val = candidates[cur_index]

            combination_sum(cur_index, cur_arr + [cur_val], cur_sum+cur_val)
            combination_sum(cur_index+1, cur_arr, cur_sum)

        combination_sum(0)

        return res
