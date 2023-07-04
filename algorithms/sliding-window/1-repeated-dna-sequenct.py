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
# Time Complexity: O(n)
# Space Complexity: O(n-k)
"""
def find_repeated_sequences(s, k):
    size = len(s)
    if size < k:
        return result
    
    result = set()
    all_dna_hashes = set()
    
    base = 4
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    # converting characters to numbers
    nums = []
    for item in range(size):
        nums.append(mapping.get(s[item]))
        
    # Storing hash value for first k letters and then using it for each next slide in window
    prev_hash = 0
    for j in range(k):
        prev_hash += nums[j] * (base ** (k-j-1))
    
    all_dna_hashes.add(prev_hash)

    for i in range(1, size-k+1):
        current_window_hash = (prev_hash - (nums[i-1] * (4 ** (k-1)))) * 4 + nums[i + k -1]
        if current_window_hash in all_dna_hashes:
            result.add(s[i:i+k])
        else:
            all_dna_hashes.add(current_window_hash)
            
        prev_hash = current_window_hash
    
    return result

def main():
    print(find_repeated_sequences("AAAAACCCCCAAAAACCCCCC", 8))

if __name__ == "__main__":
    main()


"""
Iteration 1
# Time Complexity: O( (n-k) * k )
# Space Complexity: O( (n-k) * k )

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

"""