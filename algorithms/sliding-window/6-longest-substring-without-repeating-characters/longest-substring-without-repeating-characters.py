
"""
Longest Substring without Repeating Characters

Statement
Given a string, str, return the length of the longest substring without repeating characters.

Constraints:
- 1 <= str.length <= 5 * 10^4
- str consists of English letters, digits, symbols, and spaces.

Test Case:

Input:
str: "pwwkew"


Output:
3
"""

"""
Time Complexity: O(n), n is length of string
Space Complexity: O(n)
"""
def find_longest_substring(string):
    result_len = 0
    l,r = 0, 0
    curr_char = {}
    size = len(string)

    while r < size :
        curr_char[string[r]] = curr_char.get(string[r], 0) + 1
        while curr_char[string[r]] > 1:
            curr_char[string[l]] -= 1
            l += 1
        
        
        if result_len < len(string[l:r+1]):
            result_len = len(string[l:r+1])
            
        r += 1

    return result_len

def main():
    str = "pwwkew"
    print(find_longest_substring(str))

if __name__ == "__main__":
    main()


"""
Solution Summary
- Initialize result_len to 0 and two pointers, l and r, both at 0.
- Use the curr_char dictionary to track character counts.
- Enter a while loop while r is less than string length.
- Increment curr_char[string[r]] and move r right.
- If count of string[r] is > 1, decrement curr_char[string[l]] and move l right.
- Update result_len with max length of substrings.
- Return result_len.
"""