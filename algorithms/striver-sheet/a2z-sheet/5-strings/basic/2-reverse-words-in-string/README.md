## Algorithm Summary: Reverse Words in a String

### Problem Statement:
Given a string `s`, reverse the order of words in the string while maintaining the order of characters within each word.

### Algorithm Steps:
1. Initialize an empty string `res` to store the result.
2. Get the length of the input string `s` and initialize `start` and `end` pointers to `n-1`, where `n` is the length of `s`.
3. Iterate backward through the string using a for loop with a step of -1.
4. Inside the loop:
   - Check if the current character is a space and if `start` and `end` pointers are at the same position. If so, decrement `start` and set `end` to `start`.
   - If the current character is a space, concatenate the substring from `start+1` to `end+1` (inclusive) to the result string `res`, followed by a space. Then update `end` to `start-1`.
   - Decrement `start`.
5. After the loop, concatenate the remaining substring from `start+1` to `end+1` (inclusive) to the result string `res`.
6. Return the result string `res`.

