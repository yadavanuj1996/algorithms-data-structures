# Repeated DNA Sequences Problem

## Statement
Given a string, s, that represents a DNA subsequence, and a number k, return all the contiguous subsequences
(substrings) of length k that occur more than once in the string. The order of the returned subsequences does
not matter. If no repeated substring is found, the function should return an empty set.

## Solution
We have solved this problem using rabin karp algorithm that utilizes a sliding window with rolling hash for pattern matching.

```

- We traverse the string by using a sliding window of length k, which slides one character forward on each iteration.
- On each iteration, we compute the hash of the current k-length substring in the window.
- We check if the hash is already present in the set.
  - If it is, the substring is repeated, so we add it to the output.
  - Otherwise, the substring has not yet been repeated, so we add the computed hash to the set.
- We repeat the above process for all k-length substrings by sliding the window one character forward on each iteration.
- After all k-length substrings have been evaluated, we return the output.
```

### Hashing and comparison in constant time
We need a hash function that helps us achieve constant-time hashing.For this purpose, we use the polynomial rolling hash technique:  
H=c1 * a^(k-1) + c2 * a^(k-2) + c3 * a^(k-3) + .. .... + ck a^(0)  

​Here, a is a constant, c1, c2, ..., ck are the characters in a sequence, and k is the substring length. Since we only have 4 possible nucleotides, our a would be 4. We also assign numeric values to the nucleotides A -> 1, C -> 2, G -> 3, T -> 4

```
Hash(Current substring) = (Hash(Previous substring) - Hash(first character of previous substring)) * base + Hash(Last character of current substring)
```

![IMG_6093 (1)](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/5f4c5413-06f2-4e53-b791-0a46ddb1ff1c)

