
"""
Binary strings with no consecutive 1s.

Statement
You have been given an integer 'N'. Your task is to generate and return all binary strings of length 'N' 
such that there are no consecutive 1's in the string.
A binary string is that string which contains only ‘0’ and ‘1’.

For Example:
Let ‘N'=3, hence the length of the binary string would be 3. 

We can have the following binary strings with no consecutive 1s:
000 001 010 100 101 


Constraints:
1 <= 'N' <= 20
- Time limit: 1 second

Test Case:

Sample Input 1:
4

Sample Output 1:
0000 0001 0010 0100 0101 1000 1001 1010 

Explanation of sample input 1:
For N = 4 we get the following Strings:

0000 0001 0010 0100 0101 1000 1001 1010 

Note that none of the strings has consecutive 1s. Also, note that they are in a lexicographically increasing
order.
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