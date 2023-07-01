"""
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

"""

"""
Iteration 1
# Time Complexity: O(n-k) * k
# Space Complexity: O(n-k) * k
"""
def find_repeated_sequences(s, k):
    result = set()
    all_dna_seq = set()
    size = len(s)
    
    if size < k:
        return result

    for i in range(size-k+1):
        cur_dna_seq = s[i:i+k]
        if cur_dna_seq in all_dna_seq:
            result.add(cur_dna_seq)
        else:
            all_dna_seq.add(cur_dna_seq)
    
    return result
