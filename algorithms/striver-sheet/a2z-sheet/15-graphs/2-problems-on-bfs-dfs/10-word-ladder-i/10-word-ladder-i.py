"""
Word Ladder

Problem Link:
https://leetcode.com/problems/word-ladder/

Statement:
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> sk such that:

- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest 
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Constraints:
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters.
- beginWord != endWord
- All the words in wordList are unique.

Test Case:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5

Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 
words long.

"""
"""
Time Complexity: O(W * M * log W), where W is length of Word list and M is length of begin word log W is used because operation of search a word in set is in general O(1) but in worst case is O(N) so we put it as O(log N)
-> Detailed TC -> O(W) (setup word_set) + O(W) * O(M) * 26 * O(log W) for iterating over queue then iterating over a word and then searching the word in set
 
Space Complexity: O(W), actually O(2W) -> O(W) for word_set & O(W) for queue
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        queue = []

        if not endWord in word_set:
            return 0
        
        queue.append((beginWord, 1))

        while queue:
            cur_word, word_count = queue.pop(0)
            
            if cur_word == endWord:
                return word_count

            for i in range(len(cur_word)):
                # iterate over 0 to 25, 0 -> a, z -> 25
                for alphabet_no in range(26):
                    replaced_character = chr(ord("a") + alphabet_no)
                    replaced_word = cur_word[0:i] + replaced_character + cur_word[i+1:] 

                    if replaced_word in word_set:
                        queue.append((replaced_word, word_count + 1))
                        word_set.remove(replaced_word)
        
        return 0


        
