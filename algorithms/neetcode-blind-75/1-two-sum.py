import copy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_diff_dict = {}
        n = len(nums)

        for i in range(n):
            cur_no = nums[i]
            
            if num_diff_dict.get(cur_no) is not None:
                return [num_diff_dict[cur_no], i]
            
            num_diff_dict[target-cur_no] = i
        






       
