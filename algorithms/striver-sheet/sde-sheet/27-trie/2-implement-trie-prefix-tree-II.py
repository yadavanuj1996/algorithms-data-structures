"""
Implement Trie II

Problem Link:
https://www.codingninjas.com/studio/problems/implement-trie_1387095?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTabValue=SUBMISSION

Statement
Ninja has to implement a data structure ”TRIE” from scratch. Ninja has to complete some functions.

1) Trie(): Ninja has to initialize the object of this “TRIE” data structure.

2) insert(“WORD”): Ninja has to insert the string “WORD”  into this “TRIE” data structure.

3) countWordsEqualTo(“WORD”): Ninja has to return how many times this “WORD” is present in this “TRIE”.

4) countWordsStartingWith(“PREFIX”): Ninjas have to return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.

5) erase(“WORD”): Ninja has to delete one occurrence of the string “WORD” from the “TRIE”.

Note:

1. If erase(“WORD”) function is called then it is guaranteed that the “WORD” is present in the “TRIE”.

2. If you are going to use variables with dynamic memory allocation then you need to release the memory associated with them at the end of your solution.
Can you help Ninja implement the "TRIE" data structure?

Constraints:
- 1 <= “T” <= 50
- 1 <= “N” <= 10000
- “WORD” = {a to z}
- 1 <= | “WORD” | <= 1000


Test Case:
N/A (check the problem link)
"""

"""
Time complexity: N/A
Space Complexity: N/A
"""
from os import *
from sys import *
from collections import *
from math import *

"""
Note: This tree can have same words multiples times, as the words
are not unique we have added end_with and count_prefix flags rather
than a simple is_end flag like Prefix tree I where a word can only be
inserted once(like a dictionary)
"""
class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.end_with = 0
        self.count_prefix = 0
    
    def contains_key(self, ch: str) -> bool:
        return self.links[ord(ch) - ord("a")] is not None

    def get(self, ch: str)->"TrieNode":
        return self.links[ord(ch)-ord("a")]
    
    def put(self, ch:str, node:"TrieNode") -> None:
        self.links[ord(ch)-ord("a")] = node
    
    def get_end_with_count(self)->int:
        return self.end_with

    def increase_end_with(self)->None:
        self.end_with += 1

    def reduce_end_with(self)->None:
        self.end_with -= 1
    
    def get_count_prefix(self)->int:
        return self.count_prefix
    
    def increase_count_prefix(self)->None:
        self.count_prefix += 1
    
    def reduce_count_prefix(self)-> None:
        self.count_prefix -= 1
    


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                node.put(cur_char, TrieNode())

            node = node.get(cur_char)
            node.increase_count_prefix()

        node.increase_end_with()

    def countWordsEqualTo(self, word):
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                return 0

            node = node.get(cur_char)

        return node.get_end_with_count()

    def countWordsStartingWith(self, word):
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                return 0
            node = node.get(cur_char)

        return node.get_count_prefix()

    def erase(self, word):
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                return

            node = node.get(cur_char)
            node.reduce_count_prefix()
        node.reduce_end_with()






