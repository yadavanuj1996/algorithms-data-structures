## Time complexity related important points:

- Here come the three rules, that we are going to follow while calculating the time complexity:
    - We will always calculate the time complexity for the worst-case scenario.
    - We will avoid including the constant terms.
    - We will also avoid the lower values.


## Space Complexity related important points:
- Space complexity generally represents the summation of auxiliary space and the input space. Auxiliary space refers to the space that we use additionally to solve a problem. And input space refers to the space that we use to store the inputs.


Points to remember:
In competitive programming or in the platforms like Leetcode and GeeksforGeeks, we generally run our codes on online servers. Most of these servers execute roughly 108 operations in approximately 1 second i.e. 1s. We must be careful that if the time limit is given as 2s the operations in our code must be roughly 2*108, not 1016. Similarly, 5s refers to 5*108. Simply, if we want our code to be run in 1s, the time complexity of our code must be around O(108) avoiding the constants and the lower values.