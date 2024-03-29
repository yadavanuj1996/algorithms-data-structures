"""
Problem Link:
https://takeuforward.org/data-structure/fractional-knapsack-problem-greedy-approach/#google_vignette
https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
"""

#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def sort_by_val_to_weight_ratio(self, element):
        return element[2]
 
    def fractionalknapsack(self, W,arr,n):
        items = arr
        w = W
        inp = []
        result = 0
    
        for item in items:
            weight = item.weight
            value = item.value
            val_to_weight_ratio = value / weight
            inp.append((weight, value, val_to_weight_ratio))
            
        inp.sort(reverse=True, key=self.sort_by_val_to_weight_ratio)
        
        i = 0 
        while w > 0 and i < len(inp):
            cur_weight = inp[i][0]
            cur_value = inp[i][1]
    
            if cur_weight <= w:
                result += cur_value
                w -= cur_weight
            else:
                result +=  (cur_value/cur_weight) * w
                w -= w
            
            i += 1
    
        return result
           
       

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        arr = [Item(0,0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2*i]
            arr[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,arr,n))

# } Driver Code Ends