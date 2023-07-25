# Minimum Window Substring

### Leetcode Problem Link
https://leetcode.com/problems/minimum-window-substring/

## Statement
We are given two strings, s and t, find the minimum window substring of t in s.  
The minimum window substring of t in s is defined as follows:  
    - It is the shortest substring of s that includes all of the characters present in t.  
    - The frequency of each character in this substring that belongs to t should be equal to or greater than its frequency in t.  
    - The order of the characters does not matter here.  

## Constraints:
- Strings s and t consist of uppercase and lowercase English characters.
- 1 <= s.length, t.length <= 10^3


## Test Case:
Input:
s: "ABAACBBA"
t: "ABC" 

Output:
"ACB"


<img width="679" alt="Screenshot 2023-07-25 at 5 31 45 PM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/de6b86fc-6324-4c78-ac25-beca7a75c4ba">

## Algorithm Solution

1. Initialize variables:

    - size = length of string "s."
    - result = an empty string to store the minimum window found.
    - result_len = positive infinity to track the length of the minimum window found.
    - l, r = two pointers starting at index 0 of string "s."
    - required_chars = an empty dictionary to store the count of characters needed from string "t."
    - window = an empty dictionary to store the count of characters in the current window.
    - required_len = length of string "t" (the total number of characters needed).
    - current_len = current number of unique characters present in the window.
    - is_new_char_added_in_window = a boolean flag to indicate whether a new character is added to the window.

2. Create the "required_chars" and "window" dictionaries to store the count of characters needed and present in the window, respectively.

3. Loop through each character "curr_char" in string "t":
    - Increment the count of "curr_char" in the "required_chars" dictionary.
    - Set the count of "curr_char" in the "window" dictionary to 0.

4. Start a while loop while "r" is less than the size of "s" and "l" is less than or equal to "r":
    - Check if the character at index "r" in string "s" is in string "t" and if it's a new character added to the window.
    - If the conditions are met, update the count of the character in the "window" dictionary and increment "current_len" if necessary.

5. If "current_len" is equal to "required_len" (meaning all characters from "t" are present in the window):
    - Calculate the current substring "curr_substring" from index "l" to "r+1."
    - If the length of "curr_substring" is smaller than "result_len," update "result" and "result_len" with "curr_substring" and its length, respectively.
  
6. If the character at index "l" of string "s" is not required (i.e., not present in "t"), move the left pointer "l" to the right.

7. If the character at index "l" of string "s" is present in "t" and its count in the window exceeds the required count:
    - Decrease its count in the "window" dictionary and move the left pointer "l" to the right.

8. If the character at index "l" of string "s" is present in "t" and its count in the window does not exceed the required count:
    - Decrease its count in the "window" dictionary and decrement "current_len."

9. Move the right pointer "r" to the right.

10. Return the "result," which contains the minimum window that includes all characters from string "t."




### Time & Space Complexity:
Time Complexity:  O(m+n), m is length of t and n is length of s 
Space Complexity: O(n) n is length of s
