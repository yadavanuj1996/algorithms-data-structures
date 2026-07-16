"""
TC: O(n * amount)
SC: O(n * amount) (memo) + O(amount) recursion stack
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = [[-1] * (amount+1) for _ in range(n)]

        def coin_change(index, target):
            if target < 0:
                return float("inf")

            if index == 0:
                return target // coins[index] if target % coins[index] == 0 else float("inf")

            if not memo[index][target] == -1:
                return memo[index][target]

            pick = 1 + coin_change(index, target-coins[index])

            unpick = coin_change(index-1, target)

            memo[index][target] = min(pick, unpick)

            return memo[index][target]

        res = coin_change(n-1, amount)

        return -1 if res == float("inf") else res
