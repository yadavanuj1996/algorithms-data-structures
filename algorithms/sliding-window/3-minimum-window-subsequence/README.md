# Minimum Window Subsequence

## Statement
Given two strings, str1 and str2, find the shortest substring in str1 such that str2 is a subsequence of that substring.

A substring is defined as a contiguous sequence of characters within a string. A subsequence is a sequence that can be derived from another sequence by deleting zero or more elements without changing the order of the remaining elements.

Let’s say you have the following two strings:
str1 = "abbcb"
str2 = "ac"

In this example, “abbc” is a substring of str1, from which we can derive str2 simply by deleting both the instances of the character b.
Therefore, str2 is a subsequence of this substring. Since this substring is the shortest among all the substrings in which str2 is present as a subsequence, 
the function should return this substring, that is, “abbc”.

#### Note:
If there is no substring in str1 that covers all characters in str2, return an empty string.
If there are multiple minimum-length substrings that meet the subsequence requirement, return the one with the left-most starting index.

## Constraints:
- 1 <= str1.length <= 2 * 10^3
- 1 <= str2.length <= 100
- str1 and str2 consist of uppercase and lowercase English letters.

## Test Case:

Input:
str1: "abcdebdde"
str2: "bde"

Output:
"bcde"



## Solution Summary

<img width="825" alt="Screenshot 2023-07-17 at 6 07 28 PM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/4d042608-fbeb-44db-8900-64ac371cbff0">

- Initialize two indexes, index_s1 and index_s2, to zero for iterating both strings.
- If the character pointed by index_s1 in str1 is the same as the character pointed by index_s2 in str2, increment both pointers. Otherwise, only increment index_s1.
- Once index_s2 reaches the end of str2, initialize two new indexes (start and end). With these two indexes, we’ll slide the window backward.
- Set start and end to index_s1.
- If the characters pointed to by index_s2 and start are the same, decrement both of them. Otherwise, only decrement start.
- Once, str2 has been discovered in str1 in the backward direction, calculate the length of the substring.
- If this length is less than the current minimum length, update the min_sub_len variable and the min_subsequence string.
- Resume the search in the forward direction from start + 1 in str1.
- Repeat until index_s1 reaches the end of str1.


## Time Complexity Explanation:
The outer loop iterates over the string str1, so the time complexity of this loop will be O(n) , where n is the length of string str1. 
Inside this loop, there is a while loop that is used to iterate back over the window once all the characters of str2 have been found in the current window. The time complexity of this loop will be O(m), where m is the length of string str2. 

Therefore, the overall time complexity of this solution is O(n×m)

Let’s consider another example where the inner loop travels for more than O(m) iterations. For example, when str1 = “abcdefg” and str2 = “af”. When all characters of str2 have been found (using outer loop in O(n) time), the inner loop iterates back from ‘f’ till ‘a’, taking O(n)
 time. After that, the outer loop will start from ‘b’ and traverse all characters till the end of str1 without initiating the inner loop. This is because the outer loop will never find a subsequence containing str2. This will take O(n) time. Therefore, the total time complexity in this case will be O(n+n+n), which is O(n).
