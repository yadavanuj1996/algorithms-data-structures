"""
Search a 2D Matrix

Problem Link:
https://leetcode.com/problems/search-a-2d-matrix

Statement
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4


Test Case:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

"""

# Time Complexity:O(log(m*n))
# Space Complexity O(1) 

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        first = 0
        last = (len(matrix) * len(matrix[0])) - 1
        return self.get_element_using_binary_search(matrix, target, first, last)
    
        
    def get_element_using_binary_search(self, nums: list[int], target: int, low: int, high: int) -> int:
        if not low <= high: 
            return False

        mid = (low + high) // 2
        x = mid // (len(nums[0]))
        y = mid % (len(nums[0]))
        if nums[x][y] == target:
            return True
        elif nums[x][y] < target:
            return self.get_element_using_binary_search(nums, target, mid+1, high)
        elif nums[x][y] > target:
            return self.get_element_using_binary_search(nums, target, low, mid-1)
           
def main():
    sol = Solution()
    input = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 16
    print(sol.search(input, target))


if __name__ == "__main__":
    main()

"""
Solution Summary:
- Binary Search Approach**: Utilizes binary search, an efficient divide-and-conquer algorithm, to search for a target element in a sorted 2D matrix.

- Flattening the Matrix**: Treats the 2D matrix as a 1D array by mapping its indices to a linear array index. This simplifies the binary search operation.

- Initialization**: Sets two pointers, `first` and `last`, to the start and end indices of the flattened matrix, respectively.

- Binary Search Iteration**:
  - Calculates the middle index between `first` and `last`.
  - Converts the 1D index back to 2D coordinates to access the corresponding matrix element.
  - Compares the matrix element with the target:
    - If equal, returns `True` as the target is found.
    - If less, updates the `first` pointer to narrow the search range to the right half of the matrix.
    - If greater, updates the `last` pointer to narrow the search range to the left half of the matrix.

- Recursion: Utilizes recursion to perform binary search iteratively, effectively narrowing down the search space with each recursive call.

- Base Case: Terminates the recursion when the `low` pointer surpasses the `high` pointer, indicating that the target element is not present in the matrix.

- Time Complexity: Achieves a time complexity of O(log(m*n)), where m is the number of rows and n is the number of columns in the matrix, due to the efficient binary search technique.

- Space Complexity: Maintains a constant space complexity of O(1) as it only uses a few variables for pointers and calculations, regardless of the input matrix size.

Solution Video:
https://www.youtube.com/watch?v=Ber2pi2C0j0
"""
