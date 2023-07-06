Repeated DNA Sequences Problem

Statement
Given a string, s, that represents a DNA subsequence, and a number k, return all the contiguous subsequences
(substrings) of length k that occur more than once in the string. The order of the returned subsequences does
not matter. If no repeated substring is found, the function should return an empty set.

Constraints:
- 1 ≤ s.length ≤ 10^4
- s[i] is either A, C, G, or T.
- 1 <= k <= 10

Test Case:

Input:
"AAAAACCCCCAAAAACCCCCC"
8
Output:
["AAACCCCC", "AAAACCCC", "AAAAACCC"]


