"""
TC: O(n)
SC: O(1)

Greedy: track the furthest index reachable so far. If the current index ever
exceeds reachable, we can't get there. Otherwise extend reachable = max(reachable, i + nums[i]).
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False

            reachable = max(reachable, nums[i] + i)

        return True
