"""
TC: O(1) (fixed 32 iterations)
SC: O(1)
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            n_last_bit = n & 1
            res = res << 1
            res = (res | n_last_bit)

            n = n >> 1

        return res
