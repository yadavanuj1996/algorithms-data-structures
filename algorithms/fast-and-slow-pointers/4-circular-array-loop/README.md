# Circular Array Loop Problem

### This solution contains two approaches (Both are present in solution file)
1. Two pointers (Iteration 1)
2. Fast and slow pointers (More efficient than above)

Test Case 1:
Input:
[2,-1,1,2,2]

Output: 
True

<img width="539" alt="Screenshot 2023-06-30 at 5 54 21 PM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/ed45d1ec-a6af-4823-9375-8efdc4a4eb22">

Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --> 2 --> 3 --> 0 --> ..., and all of its nodes are white (jumping in the same direction).

Test Case 2:
Input:
[3, 3, 1, -1, 2]
Output:
True

![IMG_5764](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/239ea3b8-812d-4ae3-9ffb-9d98e7a7e37b)





