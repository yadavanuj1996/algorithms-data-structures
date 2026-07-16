"""
TC: O(n^2)
SC: O(1) (excluding output)

-1, 0, 1, 2, -1, -4
-4,-1,-1, 0, 1,2
0 0 0


[-4, -2, -1, -1, 0, 0, 0, 0, 1, 2, 2]
[-4, -1, -1, 0, 1, 2 ]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(0, n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first_num = nums[i]

            start = i + 1
            end = n-1

            while start < end:
                second_num = nums[start]
                third_num = nums[end]

                if first_num + second_num + third_num == 0:
                    res.append([first_num, second_num, third_num])
                    start += 1
                    end -= 1
                    while nums[start] == nums[start-1] and start < end:
                        start += 1

                    while nums[end] == nums[end+1] and start < end:
                        end -= 1

                elif first_num + second_num + third_num < 0:
                    start += 1
                else:
                    end -= 1

        return res
