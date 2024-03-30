"""
Candy

Problem Link:
https://leetcode.com/problems/candy/

Statement
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Constraints:
- 1 <= 'N' <= 10^5
- 1 <= jobs[i][0] <= 'N'
- 1 <= jobs[i][1] <= 'N'
- 1 <= jobs[i][2] <= 10^3


Test Case:

Input: ratings = [1,2,2]
Output: 4

Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

"""

"""
Time complexity: O(N), acutally O(3N) two iterations over the ratings array and sum function in python
Space complexity: O(N), size of candy_arr
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy_arr = [1] * n # initialize with 1 candy to each child as it is an requirement
        # left to right
        for i in range(1, n):
            if ratings[i-1] < ratings[i] and candy_arr[i] < candy_arr[i-1] + 1:
                candy_arr[i] = candy_arr[i-1] + 1

        # right to left
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and candy_arr[i] < candy_arr[i+1] + 1:
                candy_arr[i] = candy_arr[i+1] + 1
        
        return sum(candy_arr)

        