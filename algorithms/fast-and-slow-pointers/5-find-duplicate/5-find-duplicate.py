"""
Find The Duplicate Number Problem

Note: Please read and learn relevant concepts of : Floyd's Tortoise and Hare (Cycle Detection) approach
First reduce the problem into Linked List cycle problem (without using extra space of course) and then use
Floyd's Tortoise and hare algorithm 
Details are mentioned in README file


Statement:
Given an unsorted array of positive numbers, nums, such that the values lie in the range  [1,n], inclusive, and
that there are n+1 numbers in the array, find and return the duplicate number present in nums. 
There is only one repeated number in nums.

Important Note: You cannot modify the given array nums. You have to solve the problem using only constant 
extra space.

Constraints:
- 1 ≤ n ≤ 10^5
- nums.length = n+1
- 1 <= nums[i] <= n 
- All the integers in nums are unique, except for one integer that will appear more than once.

Test Case (Please check readme as well):
Input:
[1, 3, 3, 4, 2, 5]
Output:
3
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
def find_duplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while not slow == fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return fast

"""
Steps of solution:
- Traverse in nums using the fast and slow pointers.
- Move pointers until they meet. The slow pointer moves once and the fast pointer moves twice as fast as the slow pointer.
- After the pointers meet, traverse in nums again.
- Move the slow pointer from the start of nums and the fast pointer from the meeting point at the same speed (one step) until they meet again.
- Return the fast pointer.
"""

def main():
    print(find_duplicate([1, 3, 3, 4, 2, 5]))

if __name__ == "__main__":
    main()
