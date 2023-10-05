# Binary Search
Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 

## Does my problem match this pattern?

### Yes, if all of these conditions are fulfilled:
- The data structure must be sorted.
- Access to any element of the data structure takes constant time.

## Note: 
- Binary search is only applicable in a sorted search space. The sorted search space does not necessarily have to be a sorted array. It can be anything but the search space must be sorted.
- In binary search, we generally divide the search space into two equal halves and then try to locate which half contains the target. According to that, we shrink the search space size.
- Binary Search can be done using both recursive and iterative implementation

## Real-world problems
- Searching in dictionary (or any sorted data)


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