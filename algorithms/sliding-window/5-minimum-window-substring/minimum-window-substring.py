
"""
Minimum Window Substring

Statement
We are given two strings, s and t, find the minimum window substring of t in s.
The minimum window substring of t in s is defined as follows:
    - It is the shortest substring of s that includes all of the characters present in t.
    - The frequency of each character in this substring that belongs to t should be equal to or greater than its frequency in t.
    - The order of the characters does not matter here.

Constraints:
- Strings s and t consist of uppercase and lowercase English characters.
- 1 <= s.length, t.length <= 10^3

Test Case:

Input:
s: "ABAACBBA"
t: "ABC" 

Output:
"ACB"
"""

"""
Time Complexity:  O(m+n), m is length of t and n is length of s 
Space Complexity: O(n) n is length of s
"""
def min_window(s, t):
    size = len(s)
    result = ""
    result_len = float("inf")
    l, r = 0, 0
    required_chars = {}
    window = {}
    required_len = len(t)
    current_len = 0
    is_new_char_added_in_window = True
    for curr_char in t:
        required_chars[curr_char] = 1 + required_chars.get(curr_char, 0)
        window[curr_char] = 0
    
    while r < size and l <= r:
        if s[r] in t and is_new_char_added_in_window:
            window[s[r]] += 1
            if window[s[r]] <= required_chars[s[r]]:
                current_len += 1

        #print(required_len, current_len, window)
        if required_len == current_len:
            curr_substring = s[l:r+1]
            if len(curr_substring) < result_len:
                result = curr_substring
                result_len = len(curr_substring)
                #print(result)

            if not required_chars.get(s[l]):
                l += 1
                is_new_char_added_in_window = False
                continue

            if window[s[l]] > required_chars[s[l]]:
                window[s[l]] -= 1
                l += 1
                is_new_char_added_in_window = False
                continue
        
            window[s[l]] -= 1
            current_len -= 1
            l += 1
            is_new_char_added_in_window = True

        r += 1

    return result

def main():
    s = "XYZYX"
    t = "XYZ"
    #s = "ABAACBBA"
    #t = "ABC"
    print(min_window(s, t))
    #print(is_substring_valid("BA", "ABA"))
    
if __name__ == "__main__":
    main()
    
    
"""
Iteration 1 

def min_window(s, t):
    size = len(s)
    result = ""
    result_len = float("inf")
    l, r = 0, 0

    while r < size and l <= r:
        curr_substring = s[l:r+1]
        if is_substring_valid(curr_substring, t):
            if  len(curr_substring) < result_len:
                result = curr_substring
                result_len = len(curr_substring)
            l += 1
            continue

        r += 1

    return result
    
def is_substring_valid(curr_substring, t):
    for item in t:
        if curr_substring.find(item) > -1:
            curr_substring = curr_substring.replace(item, "1", 1)
        else:
            return False
    
    return True

"""