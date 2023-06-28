# Two Pointers: Introduction

## Overview

As the name suggests, the two pointers pattern uses two pointers to iterate over an array or list until the conditions of the problem are satisfied. This is useful because it allows us to keep track of the values of two different indexes in a single iteration. Whenever there’s a requirement to find two data elements in an array that satisfy a certain condition, the two pointers pattern should be the first strategy to come to mind.

The pointers can be used to iterate the data structure in one or both directions, depending on the problem statement. For example, to identify whether a string is a palindrome, we can use one pointer to iterate the string from the beginning and the other to iterate it from the end. At each step, we can compare the values of the two pointers and see if they meet the palindrome properties.

## Does my problem match this pattern?

### Yes, if all of these conditions are fulfilled:

- The input data can be traversed in a linear fashion, that is, it’s in an array, in a linked list, or in a string of characters.
- The input data is sorted, or else, arranged in a way that is relevant to the problem, such as numeric data sorted in ascending or descending order, or characters arranged symmetrically.
- We are only considering the two elements in the input data that are pointed to by the two pointers rather than the whole set of elements located between the two pointers.

### No, if either of these conditions is fulfilled:

- The input data cannot be traversed in a linear fashion, that is, it’s neither in an array, nor in a linked list, nor in a string of characters.
- The problem requires an exhaustive search of the solution space, that is, eliminating one solution does not eliminate any others.

## Real-world problems
- Transmission errors
- Product suggestions

