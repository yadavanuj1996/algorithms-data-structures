"""
Coin Change II

Problem Link:
https://leetcode.com/problems/coin-change-ii/description/

Statement
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Constraints:
- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- All the values of coins are unique.
- 0 <= amount <= 5000


Test Case:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1


Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
"""


"""
Solution 1: Memorization Solution

Time Complexity: O(N*T), T is amount/target, n is size of coins array
Space Complexity: O(N*T) + O(T), where O(T) is auxilary space used for solving problem 

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]

        def get_change_total_ways(index, target):
            if target == 0:
                return 1
            
            if index == 0:
                return 1 if target % coins[0] == 0 else 0
            
            if target < 0:
                return 0
            
            if not dp[index][target] == -1:
                return dp[index][target]
            
            # pick
            pick = get_change_total_ways(index, target-coins[index])
            #unpick
            unpick = get_change_total_ways(index-1, target)
            dp[index][target] = pick + unpick
            return dp[index][target]
        
        return get_change_total_ways(len(coins)-1, amount)
        
"""

"""
Solution 2: Tabulation Solution

Time Complexity: O(N*T), Reason: There are two nested loops
Space Complexity: O(N*T) , Reason: We are using an external array of size ‘N*T’. Stack Space is eliminated.
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        n = len(coins)
        # Step 1: setup the base case
        # target is 0
        for i in range(n):
            dp[i][0] = 1
        
        for target in range(1, amount+1):
            dp[0][target] = 1 if target % coins[0] == 0 else 0
        
        # Step 2: Look at changing parameters from recurence function
        for index in range(1, n):
            for target in range(1, amount+1):
                # Step 3 copy the recurence
                # pick
                pick = 0
                if target-coins[index] >= 0:
                    pick = dp[index][target-coins[index]]
                #unpick
                unpick = dp[index-1][target]
                dp[index][target] = pick + unpick
        
        return dp[n-1][amount]


"""
Solution 3: Space Optimization with Tabulation Solution

Time Complexity: O(N*T), Reason: There are two nested loops
Space Complexity: O(T) , Reason: We are using an external array of size ‘N*T’. Stack Space is eliminated.
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev = [0 for _ in range(amount+1)]
        
        n = len(coins)
        # Step 1: setup the base case
        for j in range(amount+1):
            prev[j] = 1 if j % coins[0] == 0 else 0
        
        # Step 2: Look at changing parameters from recurence function
        for index in range(1, n):
            cur = [0 for _ in range(amount+1)]
            for target in range(amount+1):
                # Step 3 copy the recurence
                # pick
                pick = 0
                if target-coins[index] >= 0:
                    pick = cur[target-coins[index]]
                #unpick
                unpick = prev[target]
                cur[target] = pick + unpick

            prev = cur
        
        return prev[amount]




       
"""

                


                
