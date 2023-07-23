# Longest Repeating Character Replacement

## Statement
Given a string, s, of lowercase English characters and an integer, k, return the length of the longest 
substring after replacing at most k characters with any other lowercase English character so that all the 
characters in  the substring are the same.

## Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English characters
- 0 <= k <= s.length

## Test Case:
#### Input:
s: "aabccbb"
k: 2 

#### Output:
5


## Algorithm
1. Initialize start=0 and end=−1. They represent the indexes of the window's left most and the most characters resepectively.

2. Initialize a hash map frequencyMap to contain characters and their frequencies.

3. Initially the size of the window is 0, which we consider as valid. Expand the window by moving endendend pointer forward. We do so until the window becomes invalid.

4. Every time end moves forward, we update the frquency map of the newly added element. We update maxFrequency if its frequency is the maximum we have seen so far.

  - We check for validity using the following formula  
  - end + 1 − start − maxFrequency <= k 

5. If the window is invalid, move the start pointer ahead by one step. Every time start moves forward, we update the frequency of the outgoing element in the map. At this point the size of the window is equal to the longest valid window we have seen so far. We make a note of the window size in a variable longestSubstringLength.

6. We repeat the last two steps until the window reaches the right edge of the string.

7. longestSubstringLength contains the answer.
