# Algorithms


## Algorithmic Paradigms

### Brute Force
- This method requires us to go through all the possibilities to find a solution to the problem we want to solve. For instance, if we have a list of integers and we want to find the minimum, maximum, or a certain element in that list, the Brute Force approach requires us to go through all the elements to find that specific element.

- ex: linear search

### Greedy Algorithms
- Greedy is an algorithmic paradigm that builds up a solution, piece by piece. This means it chooses the next piece that offers the most obvious and immediate benefit. A Greedy algorithm, as the name implies, always makes the choice that seems to be the best at the time. It makes a locally-optimal choice in the hope that it will lead to a globally optimal solution.
- If you have a problem where the locally-optimal choice leads to a global solution, the best fit is the Greedy technique.

- The Greedy method can solve a problem that satisfies the below-mentioned properties:
  - Greedy choice property: A global optimum can be arrived at by selecting a local optimum.
  - Optimal substructure: An optimal solution to the complete problem contains an optimal solution to subproblems.
- ex: Find the largest path

### Divide and Conquer
- Divide and conquer is an algorithmic paradigm in which the problem is repeatedly divided into subproblems until we reach a point where each problem is similar and atomic (i.e., can’t be further divided).
- It contains 3 steps
  - Divide
  - Conquer
  - Merge

![Screenshot 2023-01-19 at 6 04 15 PM](https://user-images.githubusercontent.com/22169012/213444115-43b95442-86b7-448c-ad8c-66ec1e2cbc34.png)

![Screenshot 2023-01-19 at 6 04 35 PM](https://user-images.githubusercontent.com/22169012/213444194-c460edcd-878b-476e-8e9e-9d36ae278365.png)

![Screenshot 2023-01-19 at 6 04 51 PM](https://user-images.githubusercontent.com/22169012/213444233-944686a5-44d1-4d94-93f2-c35b07599983.png)

- Advantages
  - It can be optimal for a general case solution where the problem is easy to divide, and the subproblem at some level is easy to solve.
  - It makes efficient use of memory cache because, when the problem gets divided into subproblems, it becomes smaller enough to be easily solved in the cache itself.
- Disadvantages
  - It uses a recursive approach and the most common issue with recursion is that it is slow
  - Since the problem is solved using recursion, it may end up duplicating some subproblems and lead to huge recursive stacks, which consequently consumes extra space. 


### Dynamic Programming

- Dynamic programming algorithms solve problems by combining results of subproblems— just like divide and conquer algorithms.

#### Characteristics
  - Overlapping Subproblems: the subproblems of a given problem are not independent. In other words, two subproblems share a problem.
  - Optimal Substructure Property: the overall optimal solution of the problem can be constructed from the optimal solutions of its subproblems.

#### Dynamic programming patterns
- Memoization (top-down)
  - The memoized version of a problem is similar to the regular recursive version, except that it looks for the answer of a subproblem in a lookup table before computing its solution.
- Tabulation (bottom-up)
  - Tabulation is the opposite of the top-down approach and it avoids recursion. In this approach, we solve the problem “bottom-up”. This is typically done by filling up a lookup table and computing the solution to the top/original problem based on the results in the table.

##### Advantages & Disadvantages
- Advantages
  - Being a recursive programming technique, it reduces the lines of code.
  - It speeds up the processing, as we use the answer of a previously-calculated subproblem to get the next one.
- Disadvantages
  - It takes a lot of memory to store the calculated result of every subproblem without ensuring if the stored value will be utilized or not, which leads to unnecessary memory utilization.
  - There is no general form for problems solved by dynamic programming, i.e., every problem has to be solved in its own way.

