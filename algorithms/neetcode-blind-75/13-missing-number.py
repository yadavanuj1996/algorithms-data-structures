"""
TC: O(n)
SC: O(1)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        """
        The idea is
        1. xor of same number cancels each other 5^5 =0 , 11^11=0
        2. xor of number x with 0 = x (as 1 ^ 0 =1 & 0^0 = 0)
        3. here all the numbers present in array will cancel out to 0 and finally that 0 ^ missing number will
           be left
        """
        xor_till_n = 0
        for num in range(n+1):
            xor_till_n = xor_till_n ^ num

        for num in nums:
            xor_till_n = xor_till_n ^ num

        return xor_till_n
