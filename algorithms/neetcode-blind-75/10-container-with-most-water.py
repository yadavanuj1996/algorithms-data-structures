"""
TC: O(n)
SC: O(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = -1

        start = 0
        end = n-1

        while start < end:
            area = min(height[start], height[end]) * (end-start)
            res = max(area, res)

            if height[start] <= height[end]:
                cur_height = height[start]
                while start < end and height[start] <= cur_height:
                    start += 1
            else:
                cur_height = height[end]
                while start < end and height[end] <= cur_height:
                    end -= 1

        return res
