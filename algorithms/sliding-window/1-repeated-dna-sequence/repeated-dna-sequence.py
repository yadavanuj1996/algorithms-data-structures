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

# Time Complexity: O(n)
# Space Complexity: O(n)
def find_repeated_sequences(s, k):
    size = len(s)
    # Taking base 4 as there are total 4 characters in dna sequence
    base = 4
    # Mapping of character to 4 numbers
    mapping = {'A': 1, 'C': 2, 'G':3, 'T':4}
    result = set()
    all_dna_hash = set()
    # if k is greater than size then return empty set
    if size < k:
        return result
    # Converting the characters into numbers
    nums = []
    for i in range(size):
        nums.append(mapping.get(s[i]))
    
    prev_hash = 0 
    # Making hash of first k characters of string
    for j in range(k):
        prev_hash += nums[j] * (base ** (k-j-1))
    all_dna_hash.add(prev_hash)
    # Starting from 1 to size-k+1 to accommodate all the windows except the first one as it is already done before
    for i in range(1, size-k+1):
        # Calculating hash of current window using prev_hash instead of calculating from scratch, doing it in constant time
        current_hash = (prev_hash - (nums[i-1]*(base ** (k-1)))) * base + nums[i+k-1]
        result.add(s[i:i+k]) if current_hash in all_dna_hash else all_dna_hash.add(current_hash)
        prev_hash = current_hash
        
    return result
            
def main():
    # Case 1
    print(find_repeated_sequences("AAAAACCCCCAAAAACCCCCC", 8))
    # Case 2
    #print(find_repeated_sequences("ACTCT", 2))

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

"""
Steps of solution:
- Iterate over the k-length substrings of the input string.
- Store the hash of the current substring to keep track of all unique substrings.
- If the hash of a substring has already been stored, the substring is repeated, so we add it to the output.
- When all substrings have been evaluated, return the output.
"""