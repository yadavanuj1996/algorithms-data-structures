"""
Sort Stack

Statement
You are given a stack ‘S’. Your task is to sort the sack recursively.
Note:
Looping through the stack is not allowed. You need to return a stack that is sorted in descending order.



Constraints:
- 1 <= T <= 5
- 1 <=  N <= 2000
- 0 <= S[i] <= 1000


Test Case:

Sample Input 2 :
2
4
1 2 3 4     
3    
5 1 2
Sample Output 2 :
4 3 2 1 
5 2 1

"""



"""
Time Complexity: O(N^2), for each element in recursion we might need to call fit element for all n elements
Space Complexity: O(N),  recursion stack in worse case will have n elements

"""

from os import *
from sys import *
from math import *
from collections import deque

# S is a list of integers

def sortStack(s):

    def fit_element(s, temp):
        if not s or s[-1] < temp:
            s.append(temp)
        else:
            s_temp = s.pop()
            fit_element(s, temp)
            s.append(s_temp)
    
    def sort_stack(s):
        if not s:
            return 
        
        temp = s.pop()
        sort_stack(s)
        fit_element(s, temp)

    sort_stack(s)   
    
    return s





