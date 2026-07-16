"""
TC: O(n log n)
SC: O(1) (excluding output)
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [-1] * (n+1)

        def get_one_count(n):
            res = 0
            while n:
                res += n % 2
                n = n >> 1

            return res

        for i in range(0, n+1):
            result[i] = get_one_count(i)

        return result
