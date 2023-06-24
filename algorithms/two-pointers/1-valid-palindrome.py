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

