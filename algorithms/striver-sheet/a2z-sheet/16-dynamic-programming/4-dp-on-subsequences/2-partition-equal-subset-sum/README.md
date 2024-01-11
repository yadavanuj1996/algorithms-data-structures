Intuition
- A array can only be divided into two subsets (such that combinigly both contain all the the elements of the
original array) of equal sum if the total sum of all elements in original array in even (Note: array contain
integers only)

ex: an array with sum 21 cannot be divided in 2 subset with equal sum

- Second hunch we get is if both the array will have equal sum we just need to find at least one array that
contains the total sum//2 (half of original array sum).

This basically turns the problem into find a subset whose sum is equal to a given target problem (that too
only for even sum arrays). We have already solved this problem before.