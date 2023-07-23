"""
Longest Repeating Character Replacement

Statement
Given a string, s, of lowercase English characters and an integer, k, return the length of the longest 
substring after replacing at most k characters with any other lowercase English character so that all the 
characters in  the substring are the same.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English characters
- 0 <= k <= s.length

Test Case:

Input:
s: "aabccbb"
k: 2 

Output:
5
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
def longest_repeating_character_replacement(s, k):
    l ,r = 0, 0
    char_freq = {}
    max_freq = 1
    size = len(s)
    is_window_len_changed = True

    while r < size:
        window_len = r - l + 1
        if is_window_len_changed:
            char_freq[s[r]] =  char_freq.get(s[r]) + 1 if char_freq.get(s[r]) else 1
            max_freq = char_freq[s[r]] if max_freq < char_freq[s[r]] else max_freq
        else:
            char_freq[s[l-1]] =  char_freq.get(s[l-1]) - 1
        
        if window_len - max_freq <= k:
            r += 1
            is_window_len_changed = True
        else:
            l += 1
            is_window_len_changed = False

    return r-l
 
def main():
    #s = "aaacbbbaabab"
    #k = 1
    s = "aaacbbbaabab"
    k = 2
    # s = "aaacbbbaabab"
    # k = 1
    
    print(longest_repeating_character_replacement(s, k))

if __name__ == "__main__":
    main()


"""
Solution Summary
1. Initialize start=0 and end=−1. They represent the indexes of the window's left most and the most characters resepectively.
2. Initialize a hash map frequencyMap to contain characters and their frequencies.
3. Initially the size of the window is 0, which we consider as valid. Expand the window by moving endendend pointer forward. We do so until the window becomes invalid.
4. Every time end moves forward, we update the frquency map of the newly added element. We update maxFrequency if its frequency is the maximum we have seen so far.
  - We check for validity using the following formula  
  - end + 1 − start − maxFrequency <= k 
5. If the window is invalid, move the start pointer ahead by one step. Every time start moves forward, we update the frequency of the outgoing element in the map. At this point the size of the window is equal to the longest valid window we have seen so far. We make a note of the window size in a variable longestSubstringLength.
6. We repeat the last two steps until the window reaches the right edge of the string.
7. longestSubstringLength contains the answer.


"""