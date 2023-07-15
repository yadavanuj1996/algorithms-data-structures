"""
Find Maximum in Sliding Window

Statement
Given an integer list, nums, find the maximum values in all the contiguous subarrays (windows) of size w.

Note: If the window size is greater than the array size, we consider the entire array as a single window.

Constraints:
- 1 ≤ arr.length <= 10^3
- -10^4 <= arr[i] <= 10^4
- 1 ≤ w

Test Case:

Input:
nums: [-4, 2, -5, 3, 6]
window size: 3

Output:
[2, 3, 6]

"""

from collections import deque

def find_max_sliding_window(nums, w):
    dq = deque()
    result = []
    for i in range(w):
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)
        
    result.append(nums[dq[0]])

    for i in range(w, len(nums)):
        while dq and dq[0] <= i-w:
            dq.popleft()
        
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop() 
        
        dq.append(i)
        result.append(nums[dq[0]])
        

    return result

def main():
    nums = [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67]
    w = 3
    print(find_max_sliding_window(nums, w))


if __name__ == "__main__":
    main()


"""
Steps of solution:
- Create a collection (of your own choice) to process the elements of the input list.
- Process the first window such that, at the end of the iteration, the elements of the first window are 
  present in your collection in descending order.
- When the first window has been processed, add the first element from your collection to the output list, since this will be the maximum in the first window.
- Process the remaining windows using the same logic used to process the first window.
- In each iteration, add the first element from your collection to the output list and slide the window one step forward.
- Return the output list.
"""