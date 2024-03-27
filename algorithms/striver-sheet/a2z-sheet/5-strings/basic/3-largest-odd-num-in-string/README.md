# Algorithm Summary: Finding the Largest Odd Number

## Intuition
- A number is odd if the last digit of a number itself is odd.


## Approach
1. Start iterating the string `num` from right to left.
2. Check each digit from right to left.
3. If a digit is odd, return the substring from the beginning of `num` up to and including that digit.
4. If no odd digit is found, return an empty string.

