"""
Count Good Numbers

Statement
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are
prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) 
at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, 
return it modulo 10^9 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

Constraints:
- 1 <= n <= 10^15

Test Case:

Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".

Input: n = 4
Output: 400
"""



"""
Time Complexity: O(log n), 
Space Complexity: O(1), 

"""
import math 

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        no_of_even_digit = 5
        no_of_prime_digit = 4
        res = pow(no_of_even_digit, ((n+1)//2), MOD) * pow(no_of_prime_digit, (n//2), MOD)
        
        return res % MOD