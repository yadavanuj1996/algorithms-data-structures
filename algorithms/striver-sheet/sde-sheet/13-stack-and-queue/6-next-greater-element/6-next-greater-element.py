"""
Next Greater Element I

Problem Link:
https://leetcode.com/problems/next-greater-element-i/description/

Statement
The next greater element of some element x in an array is the first greater element that is to the right of x
in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater
element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.


Constraints:
- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10^4
- All integers in nums1 and nums2 are unique.
- All the integers of nums1 also appear in nums2

Test Case:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]

Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

"""
from collections import deque
"""
Time Complexity: O(M+N)
Space Complexity:  O(N + M)
N is size of nums1 and M is size of nums2
Note: We have used nge to be a dict (hashmap for other language) to make the time complexity O(M+N) if we
have used a list it would convert the solution to O(M*N)
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = self.get_nge(nums2) # O(M)
        result = [-1] * len(nums1)

        for i in range(len(nums1)): # O(N)
            result[i] = nge.get(nums1[i])
        
        return result


    def get_nge(self, nums):
        dq = deque()
        nge = {}
        for i in range(len(nums)-1, -1, -1):
            nge[nums[i]] = -1

            while dq and dq[-1] <= nums[i]:
                dq.pop()
            
            if dq:
                nge[nums[i]] = dq[-1]
            
            dq.append(nums[i])

        return nge






        