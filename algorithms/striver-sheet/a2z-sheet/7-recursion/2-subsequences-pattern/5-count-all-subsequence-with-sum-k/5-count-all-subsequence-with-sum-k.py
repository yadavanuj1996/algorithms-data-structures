"""
Subarrays with Sum k'

Problem Link:
https://www.codingninjas.com/studio/problems/subarrays-with-sum-%E2%80%98k'_6922076

Statement
You are given an array 'A' of size 'N' and an integer'K'. You need to generate and return all subarrays
of array A whose sum = K.

Note: In the output, you will see the 2D array lexicographically sorted.

Example:
Input: N = 6 K = 3
A = [1, 2, 3, 1, 1, 1]
Output: 3
Explanation: Subarrays whose sum = 3 are:
[1, 2], [3], and [1, 1, 1]


Constraints:
1 <= 'N' <= 20
- Time limit: 1 second

Test Case:

Sample Input 1:
6 3
1 2 3 1 1 1

Sample Output 1:
3

Explanation Of Sample Input 1:

Input: N = 6 K = 3
A = [1, 2, 3, 1, 1, 1]
Output: 3
Explanation: Subarrays whose sum = 3 are:
[1, 2], [3], and [1, 1, 1]
"""



"""
Time Complexity: O(2^n) 
Space Complexity: O(n) 
"""
from typing import List

def generateString(N: int) -> List[str]:
    # write your code here
    result = []
    def generate_string(index, sub_string, last=None):
        if index == N:
            result.append(sub_string)
            return
        
        # pick
        if not last == 1:
            generate_string(index+1, sub_string+"1", 1)
        #unpick
        generate_string(index+1, sub_string+"0", 0)

    generate_string(0, "")
    return result