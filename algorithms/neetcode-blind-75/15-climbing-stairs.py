"""
TC: O(n)
SC: O(1)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        res = [0, 1, 2]
        first = 1
        second = 2

        for i in range(n-2):
            temp = first + second
            first = second
            second = temp

        return second
