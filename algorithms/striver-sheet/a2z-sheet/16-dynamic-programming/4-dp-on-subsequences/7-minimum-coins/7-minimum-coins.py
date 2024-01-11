"""
Coin Change

Problem Link:
https://leetcode.com/problems/coin-change/description/

Statement
You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be 
made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

Test Case:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

"""


"""
Solution 1: Memorization Solution

Time Complexity: O(N*T), T is amount/target, n is size of coins array
Space Complexity: O(N*T) + O(T), where O(T) is auxilary space used for solving problem 


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for i in range(amount+1)] for j in range(len(coins))]

        def get_min_coins(index, n):
            if n < 0:
                return float("inf")

            if index == 0:
                if n % coins[0] == 0:
                    return n / coins[0]
                else:
                    return float("inf")
            
            if not dp[index][n] == -1:
                return dp[index][n]
            
            
            
            #pick
            pick_min_coins = 1 + get_min_coins(index, n-coins[index])
            # unpick
            unpick_coins = 0 + get_min_coins(index-1, n)
            dp[index][n] = min(pick_min_coins, unpick_coins)
            return dp[index][n]
        
        res = get_min_coins(len(coins)-1, amount) 
        res = -1 if res == float("inf") else res
        return int(res)

"""

"""
Solution 2: Tabulation Solution

Time Complexity: O(N*T), Reason: There are two nested loops
Space Complexity: O(N*T) , Reason: We are using an external array of size ‘N*T’. Stack Space is eliminated.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for i in range(amount+1)] for j in range(len(coins))]
        # step 1:  setting up base case dp values in tabulation
        for target in range(amount+1):
            if target % coins[0] == 0:
                dp[0][target] = target // coins[0]
            else:
                dp[0][target] = float("inf")

        # step 2, check the accomode changing parameters i.e., index and n using two for loops
        for index in range(1, len(coins)):
            for target in range(amount+1):
                # step 3 copy the recurence
                # we are handling the second base case of n < = 0 here in for loop
                pick_coins = float("inf")
                if coins[index] <= target:
                    pick_coins = 1 + dp[index][target-coins[index]]
                # unpick
                unpick_coins = 0 + dp[index-1][target]
                dp[index][target] = min(pick_coins, unpick_coins)
                
            
        res = dp[len(coins)-1][amount]
        res = -1 if res == float("inf") else res
        return int(res)



"""
Solution 3: Space Optimization with Tabulation Solution

Time Complexity: O(N*T), Reason: There are two nested loops
Space Complexity: O(N*T) , Reason: We are using an external array of size ‘N*T’. Stack Space is eliminated.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for i in range(amount+1)] for j in range(len(coins))]
        # step 1:  setting up base case dp values in tabulation
        for target in range(amount+1):
            if target % coins[0] == 0:
                dp[0][target] = target // coins[0]
            else:
                dp[0][target] = float("inf")

        # step 2, check the accomode changing parameters i.e., index and n using two for loops
        for index in range(1, len(coins)):
            for target in range(amount+1):
                # step 3 copy the recurence
                # we are handling the second base case of n < = 0 here in for loop
                pick_coins = float("inf")
                if coins[index] <= target:
                    pick_coins = 1 + dp[index][target-coins[index]]
                # unpick
                unpick_coins = 0 + dp[index-1][target]
                dp[index][target] = min(pick_coins, unpick_coins)
                
            
        res = dp[len(coins)-1][amount]
        res = -1 if res == float("inf") else res
        return int(res)
"""

                


                


"""

Note:
Time Complexity for simple recursion solution will be greater than O(2^n), as in pick case we are repeating it multiple times so it is greater than 2^n, we can call it exponential in this case
Space complexity for simple recursion problem O(amount) as even it is reduced by 1 it will run amount times
"""