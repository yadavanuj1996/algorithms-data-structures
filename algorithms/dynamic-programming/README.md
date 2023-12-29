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

## References
1. https://takeuforward.org/data-structure/dynamic-programming-introduction/
2. https://www.youtube.com/watch?v=Hdr64lKQ3e4 (Okayish explaination not best)


