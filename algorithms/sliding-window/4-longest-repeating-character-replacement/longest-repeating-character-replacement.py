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
- We iterate over the input string using two pointers.
- In each iteration:
    - If the new character is not present in the hash map, we add it. Otherwise, we increment its frequency by 1
    - We slide the window one step forward if the number of replacements required in the current window has exceeded our limit.
    - If the current window is the longest so far, then we update the length of the longest substring that has the same character.
- Finally, we return the length of the longest substring with the same character after replacements.
"""