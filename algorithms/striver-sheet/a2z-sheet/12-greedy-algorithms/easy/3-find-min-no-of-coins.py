"""
Find Minimum Number Of Coins

Problem Link:
https://www.codingninjas.com/studio/problems/find-minimum-number-of-coins_975277

Statement
Given an infinite supply of Indian currency i.e. [1, 2, 5, 10, 20, 50, 100, 500, 1000] valued coins and
an amount 'N'.

Find the minimum coins needed to make the sum equal to 'N'. You have to return the list containing the value
of coins required in decreasing order.

For Example
For Amount = 70, the minimum number of coins required is 2 i.e an Rs. 50 coin and a Rs. 20 coin.
Note: It is always possible to find the minimum number of coins for the given amount. So, the answer will 
always exist.



Constraints:
- 1 <= 'N' <= 10^5
- Time Limit: 1 sec


Test Case:

Sample Input 1
13

Sample Output 1
10 2 1

Explanation of Sample Input 1
The minimum number of coins to change is 3 {1, 2, 10}.

"""

"""
Time complexity: O(N)
Space complexity: O(1)
"""
from typing import List

def MinimumCoins(n: int) -> List[int]:
    # write your code here
    currency = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    size = len(currency)
    result = []

    for i in range(size-1, -1, -1):

        while n > 0 and currency[i] <= n:
            n = n - currency[i]
            result.append(currency[i])

        
    return result