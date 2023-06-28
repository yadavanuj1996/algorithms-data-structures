"""
Write a function that takes a string, s, as an input and determines whether or not it is a palindrome.

Note: A palindrome is a word, phrase, or sequence of characters that reads the same backward as forward.

Constraints:
- 1 <= s.length <= 2x10^5
- The string s will not contain any white space and will only consist of ASCII characters.

Examples
Test Case 1:
Input: 
ABCBA

Output: 
True

Test Case 2:
Input: 
ABCCA

Output: 
False

"""
def is_palindrome(s):
  # Write your code here
  # Tip: You may use the code template provided
  # in the two_pointers.py file
  left_index = 0
  right_index = len(s)-1
  is_palindrome = True

  while left_index < right_index:
    if s[left_index:left_index+1] != s[right_index:right_index+1]:
      is_palindrome = False
      break

    left_index += 1
    right_index -= 1
  
  return is_palindrome

