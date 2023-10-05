"""

 Binary Search

Problem Link:
https://leetcode.com/problems/binary-search/

Statement
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.


Test Case:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1

"""

from collections import deque

# Time Complexity: O(log n)
# Space Complexity O(log n) 
# The size of the deque can grow a maximum up to a size of w.
class Solution:
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n: int) -> list[str]:
        self.generatePattern(n, 1, 0, "(")
        return self.result

    def generatePattern(self, n:int, no_of_left_brackets:int, no_of_right_brackets:int, pattern: str):
        if no_of_left_brackets < no_of_right_brackets or no_of_left_brackets > n or no_of_right_brackets > n:
            return
        elif no_of_left_brackets == n and no_of_right_brackets == n: 
            self.result.append(pattern)
            return
        
        self.generatePattern(n, no_of_left_brackets+1, no_of_right_brackets, pattern+'(')
        self.generatePattern(n, no_of_left_brackets, no_of_right_brackets+1, pattern+')')
    

def main():
    n = 3
    sol = Solution()
    print(sol.generateParenthesis(n))


if __name__ == "__main__":
    main()


"""
Solution Summary:
This algorithm efficiently finds the index of the target element in a sorted list by repeatedly dividing the search interval in half.

1. Initialization:
   - Initialize `low` and `high` as the index of the first & last element in the list respectively.

2. Binary Search:
   - While `low` is less than or equal to `high`:
     - Calculate the middle index: `mid = (low + high) // 2`.
     - If `nums[mid]` is equal to the `target`, return `mid` as the index of the target element.
     - If `nums[mid]` is less than the `target`, update `low` to `mid + 1` (search in the right half of the remaining elements).
     - If `nums[mid]` is greater than the `target`, update `high` to `mid - 1` (search in the left half of the remaining elements).

3. Base Case:
   - If `low` is greater than `high`, the target element is not in the list. Return `-1` to indicate that the target element is not found.

   
Time & Space Complexity:

Time Complexity: O(log N) - where N is the number of elements in the input list. Binary search reduces the search space by half in each step.
Space Complexity: O(log N) - due to the recursive nature of the algorithm. The maximum number of recursive calls stored on the call stack is logarithmic in the number of elements in the input list.



Solution Video:
https://www.youtube.com/watch?v=MHf6awe89xw
"""
