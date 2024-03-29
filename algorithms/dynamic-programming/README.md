# Dynamic Programming

## Introduction
In this article, we will be going to understand the concept of dynamic programming.

Dynamic Programming can be described as storing answers to various sub-problems to be used later whenever required to solve
the main problem.

The two common dynamic programming approaches are:
- Memoization: Known as the “top-down” dynamic programming, usually the problem is solved in the direction of the main problem to the base cases.
- Tabulation: Known as the “bottom-up ” dynamic programming, usually the problem is solved in the direction of solving the base cases to the main problem

Note: The base case does not always mean smaller input. It depends upon the implementation of the algorithm.

### Fibonacci problem

We will be using the example of Fibonacci numbers here. The following series is called the Fibonacci series:

0,1,1,2,3,5,8,13,21,…

We need to find the nth Fibonacci number, where n is based on a 0-based index.

Every ith number of the series is equal to the sum of (i-1)th and (i-2)th number where the first and second number is given as 0 and 1 respectively.

- Recursive solution
```
f (n) {
  return f(n-1) + f(n-2)
}
```
- DP Solution
```
def f(n, dp):
    if n <= 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    dp[n] = f(n-1, dp) + f(n-2, dp)
    return dp[n]
```

![Screenshot 2023-12-29 at 9 24 28 AM](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/8272092e-8736-4d88-a401-957506252662)

In DP solution we use a list dp to hold the computed values such that when we require the same value again we won't do the
calculation and simply get the value from list (this will save lot of computation of problems whose solution we already calculated)

![Screenshot 2023-12-29 at 9 31 47 AM](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/2ffbacbd-8b3d-48fd-abc2-078193abb293)


### How to Identify a DP problem?

When we see a problem, it is very important to identify it as a dynamic programming problem. Generally (but not limited to) if the problem statement asks for the following:

- Count the total number of ways
- Given multiple ways of doing a task, which way will give the minimum or the maximum output.
- Creating/ doing actions on all/ specific subsequence or subsets.

We can try to apply recursion. Once we get the recursive solution, we can go ahead to convert it to a dynamic programming one.

### Steps to form the recursive solution
- Express the problem in terms of indexes.
- Explore all possibilities at a given index
- Return the maximum of the choices

### Pick and not pick technique for recursion problems (used in DP as well)

![IMG_4819](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/573b78e7-af27-496e-a5b8-eab6ab27e9eb)

## Tabulation
Tabulation is a ‘bottom-up’ approach where we start from the base case and reach the final answer that we want.

**3 steps to convert memorization solution to tabulation solution**
- Base case (Update dp according to base case)
- Look at changing parameters
- Copy the recurence

[Refer Leetcode Problem solution with both memorization and tabulation in detail](../striver-sheet/a2z-sheet/16-dynamic-programming/4-dp-on-subsequences/7-minimum-coins/7-minimum-coins.py)


## References
1. https://takeuforward.org/data-structure/dynamic-programming-introduction/
2. https://www.youtube.com/watch?v=Hdr64lKQ3e4 (Okayish explaination not best)


