"""
Online Stock Span

Problem Link:
https://leetcode.com/problems/online-stock-span/

Statement:
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price 
for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day 
and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today
is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal
2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, 
then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 
for 3 consecutive days.

Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.

Constraints:
- 1 <= price <= 10^5
- At most 10^4 calls will be made to next.

Test Case:

Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

"""
"""
Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque

class StockSpanner:

    def __init__(self):
        # using the dq as stack
        self.dq = deque()
        self.count = 0

    def next(self, price: int) -> int:  
        # maintaing an increasing order stack (top to bottom)
        while self.dq and self.dq[-1][0] <= price:
            self.dq.pop()
        
        # if all the element on left side are smaller we use self.count + 1 as -1 will be the left 
        # greater element 
        res = self.count - self.dq[-1][1] if self.dq else self.count + 1     # self.count - (-1)

        # simply appending the current price with count in stack 
        self.dq.append((price, self.count))
        self.count += 1 

        return res

        
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
        