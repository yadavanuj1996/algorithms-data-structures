# Longest Substring without Repeating Characters

## Statement
Given a string, str, return the length of the longest substring without repeating characters.

## Constraints:
- 1 <= str.length <= 5 * 10^4
- str consists of English letters, digits, symbols, and spaces.

## Test Case:
Input:
str: "pwwkew"

Output:
3



Solution Summary:
- Initialize result_len to 0 and two pointers, l and r, both at 0.
- Use the curr_char dictionary to track character counts.
- Enter a while loop while r is less than string length.
- Increment curr_char[string[r]] and move r right.
- If count of string[r] is > 1, decrement curr_char[string[l]] and move l right.
- Update result_len with max length of substrings.
- Return result_len.