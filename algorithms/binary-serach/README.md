# Binary Search
Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 

## Does my problem match this pattern?

### Yes, if all of these conditions are fulfilled:
- The data structure must be sorted.
- Access to any element of the data structure takes constant time.

## Note: 
- Binary search is only applicable in a sorted search space. The sorted search space does not necessarily have to be a sorted array. It can be anything but the search space must be sorted.
- In binary search, we generally divide the search space into two equal halves and then try to locate which half contains the target. According to that, we shrink the search space size.


## Real-world problems
- Searching in dictionary (or any sorted data)



## Algorithm / Intuition 
- Binary Search can be done using both recursive and iterative implementation

<img width="539" alt="Screenshot 2023-10-05 at 4 03 25 PM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/df1b5015-09b2-4765-8f0b-082a8eb13c9e">


The below steps will continue until either we found the target or the search space becomes invalid i.e. high < low. By definition of search space, it will lose its existence if the high pointer is appearing before the low pointer.

#### Step 1: Divide the search space into 2 halves:
- mid = (low+high) // 2 ( ‘//’ refers to integer division)
#### Step 2: Compare the middle element with the target:
- If arr[mid] == target: We have found the target. From this step, we can return the index of the target possibly.
- If target > arr[mid]: This case signifies our target is located on the right half of the array. So, the next search space will be the right half.
- If target < arr[mid]: This case signifies our target is located on the left half of the array. So, the next search space will be the left half.

#### Step 3: Trim down the search space:
- If the target occurs on the left, we should set the high pointer to mid-1. Thus the left half will be the next search space.
- Similarly, if the target occurs on the right, we should set the low pointer to mid+1. Thus the right half will be the next search space.

#### Video explanation
https://www.youtube.com/watch?v=MHf6awe89xw
## Time Complexity
In the algorithm, in every step, we are basically dividing the search space into 2 equal halves. This is actually equivalent to dividing the size of the array by 2, every time. After a certain number of divisions, the size will reduce to such an extent that we will not be able to divide that anymore and the process will stop. The number of total divisions will be equal to the time complexity.

Let’s derive the number of divisions mathematically,
```
If a number n can be divided by 2 for x times:
	2^x = n
Therefore, x = logn (base is 2)
```
So the overall time complexity is **O(logN)**, where N = size of the given array.
