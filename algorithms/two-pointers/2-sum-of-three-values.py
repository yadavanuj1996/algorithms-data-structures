"""
Statement
Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums whose sum equals the target. Return TRUE if three such integers are found in the array. Otherwise, return FALSE.

Note: A valid triplet consists of elements with distinct indexes. This means, for the triplet nums[i], nums[j], and nums[k],
i != j, i!=k, j!=k

Constraints:
- 3 <= nums.length <= 1000
- -10^3 <= nums[i] <= 10^3
- -10^3 <= target <= 10^3

Sample Example:
Input 
target: 20
nums: [3,7,1,2,8,4,5]

result:
True
"""

def find_sum_of_three(nums, target):
   # your code will replace this placeholder return statement
   size = len(nums)
   if size < 3:
      return False

   nums.sort()
   current = 0
   low = current + 1
   high = size - 1

   while current <= size-3:
      if low >= high:
         current = current + 1
         low = current + 1
         high = size - 1

      if nums[low]+nums[high]+nums[current] > target:
         high=high-1
      elif nums[low]+nums[high]+nums[current] < target:
         low = low+1
      else:
         return True
      
   return False


