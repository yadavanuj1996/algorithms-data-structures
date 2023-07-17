"""
Minimum Window Subsequence

Statement
Given two strings, str1 and str2, find the shortest substring in str1 such that str2 is a subsequence of that substring.

A substring is defined as a contiguous sequence of characters within a string. A subsequence is a sequence that can be derived from another sequence by deleting zero or more elements without changing the order of the remaining elements.

Let’s say you have the following two strings:
str1 = "abbcb"
str2 = "ac"

In this example, “abbc” is a substring of str1, from which we can derive str2 simply by deleting both the instances of the character b.
Therefore, str2 is a subsequence of this substring. Since this substring is the shortest among all the substrings in which str2 is present as a subsequence, 
the function should return this substring, that is, “abbc”.

Note:
If there is no substring in str1 that covers all characters in str2, return an empty string.
If there are multiple minimum-length substrings that meet the subsequence requirement, return the one with the left-most starting index.

Constraints:
- 1 <= str1.length <= 2 * 10^3
- 1 <= str2.length <= 100
- str1 and str2 consist of uppercase and lowercase English letters.

Test Case:

Input:
str1: "abcdebdde"
str2: "bde"

Output:
"bcde"
"""

"""
Time Complexity: O(n*m)
Space Complexity: O(1)
"""

def min_window(str1, str2):
    index_s1 = 0
    index_s2 = 0
    min_subsequence = ""
    min_subsequence_len = float('inf')
    size_str1 = len(str1)
    size_str2 = len(str2)

    while index_s1 < size_str1:
        if str1[index_s1] == str2[index_s2]:
            index_s2 += 1
            
        if index_s2 == size_str2:
            index_s2 -= 1
            start = index_s1
            end = index_s1

            while index_s2 >= 0: 
                if str1[start] == str2[index_s2]:
                    index_s2 -= 1
                start -= 1
            
            start += 1
            index_s2 += 1

            if end - start + 1 < min_subsequence_len:
                min_subsequence_len = end-start + 1
                min_subsequence = str1[start:end+1]
            
            index_s1 = start
                
        index_s1 += 1

    return min_subsequence

"""
Solution Summary
- Initialize two indexes, index_s1 and index_s2, to zero for iterating both strings.
- If the character pointed by index_s1 in str1 is the same as the character pointed by index_s2 in str2, increment both pointers. Otherwise, only increment index_s1.
- Once index_s2 reaches the end of str2, initialize two new indexes (start and end). With these two indexes, we’ll slide the window backward.
- Set start and end to index_s1.
- If the characters pointed to by index_s2 and start are the same, decrement both of them. Otherwise, only decrement start.
- Once, str2 has been discovered in str1 in the backward direction, calculate the length of the substring.
- If this length is less than the current minimum length, update the min_sub_len variable and the min_subsequence string.
- Resume the search in the forward direction from start + 1 in str1.
- Repeat until index_s1 reaches the end of str1.

"""

def main():
    #str1 = "bbbbbbcdbd"
    #str2 = "bd"
    #str1 = "abcdebdde"
    #str2 = "bde"
    str1 = "bdbb"
    str2 = "bb"
    print(min_window(str1, str2))

if __name__ == "__main__":
    main()


"""
Iteration 1
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def min_window(str1, str2):
    ptr2 = 0
    result = ""
    result_len = sys.maxsize
    n = len(str1)
    i = 0
    while i < n:
        if str1[i] == str2[ptr2]:
            ptr2 += 1
        
        if ptr2 == len(str2):
            ptr2 -= 1
            start = i
            end = i

            while True: 
                if str1[start] == str2[ptr2]:
                    ptr2 -= 1
                    if ptr2 == -1:
                        ptr2 = 0
                        if end - start + 1 < result_len:
                            result_len = end-start + 1
                            result = str1[start:end+1]
                            i = start
                        break
                start -= 1

        i += 1

    return result

"""