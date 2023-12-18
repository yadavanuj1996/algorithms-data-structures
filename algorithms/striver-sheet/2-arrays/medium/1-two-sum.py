
"""
Two Sums
"""

"""
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
import copy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original_input = copy.deepcopy(nums)
        nums.sort()
        i, j = 0, len(nums) - 1
        fir_ind, sec_ind = -1, -1
        while i < j:
            if nums[i] + nums[j] == target:
                break
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1

        for ind in range(len(original_input)):
            if original_input[ind] == nums[i] and fir_ind == -1:
                fir_ind = ind 
            elif original_input[ind] == nums[j]:
                sec_ind = ind

        return [fir_ind, sec_ind]


       