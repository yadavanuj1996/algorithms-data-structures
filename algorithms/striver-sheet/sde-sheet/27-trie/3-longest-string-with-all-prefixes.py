"""
Longest Common Prefix

Problem Link:
https://www.codingninjas.com/studio/problems/longest-common-prefix_2090383?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

Statement
You are given an array ‘ARR’ consisting of ‘N’ strings. Your task is to find the longest common prefix among all these strings. If there is no common prefix, you have to return an empty string.

A prefix of a string can be defined as a substring obtained after removing some or all characters from the end of the string.

For Example:
Consider ARR = [“coding”, ”codezen”, ”codingninja”, ”coders”]
The longest common prefix among all the given strings is “cod” as it is present as a prefix in all strings. Hence, the answer is “cod”.

Each string consists of only lowercase letters.

Constraints:
- 1 <= T <= 10
- 1 <= N <= 3000
- 1 <= |ARR[i]| <=1000


Test Case:

Input:
2
3
applejuice applepie apple
4
car cus cart carat

Output:
apple
c

"""

"""
NOTE: I have used iterative scanning solution not the trie solution here.

Time complexity: O(N*M), N is len of arr and m is length of shortest string element in array
Space Complexity: O(1)
"""
def longestCommonPrefix(arr, n):
    # Write your code here
    # Return a string
    result = ""
    for i in range(len(arr[0])):
        fir_elem_char = arr[0][i]
        is_further_processing_req = True

        ind = 1
        while ind < len(arr):
            if i >= len(arr[ind]):
                is_further_processing_req = False
                break

            if not arr[ind][i] == fir_elem_char:
                is_further_processing_req = False
                break
            
            ind += 1

        if not is_further_processing_req:
            break
        else:
            result += fir_elem_char
    
    return result
    

