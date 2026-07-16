"""
TC: O(n)
SC: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            cur_price = prices[i]
            max_profit = max(max_profit, cur_price - min_price)

            if cur_price < min_price:
                min_price = cur_price

        return max_profit
