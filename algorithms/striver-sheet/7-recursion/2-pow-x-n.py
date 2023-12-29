
"""
Pow(x, n)

Statement
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Constraints:
- -100.0 < x < 100.0
- -2^31 <= n <= 2^31-1
- n is an integer.
- Either x is not zero or n > 0.
- -10^4 <= xn <= 10^4


Test Case:

Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.00000, n = -2
Output: 0.25000

"""



"""
Time Complexity: O(n), 
Space Complexity: O(n), 

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:   
        if n == 0:
            return 1
        if n > 0:
            return x * pow(x, n-1)
        else:
            return pow(x, n+1) / x
