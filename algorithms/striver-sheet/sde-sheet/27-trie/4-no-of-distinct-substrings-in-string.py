"""
Count Distinct Substrings

Problem Link:
https://www.codingninjas.com/studio/problems/count-distinct-substrings_985292?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTabValue=PROBLEM

Statement
Given a string 'S', you are supposed to return the number of distinct substrings(including empty substring) of 
the given string. You should implement the program using a trie.

Note :
A string ‘B’ is a substring of a string ‘A’ if ‘B’ that can be obtained by deletion of, several 
characters(possibly none) from the start of ‘A’ and several characters(possibly none) from the end of ‘A’. 

Two strings ‘X’ and ‘Y’ are considered different if there is at least one index ‘i’  such that the 
character of ‘X’ at index ‘i’ is different from the character of ‘Y’ at index ‘i’(X[i]!=Y[i]).


Constraints:
- 1 <= T <= 5
- 1 <= |S| <= 10^3


Test Case:

Input:
2
sds
abc

Output :
6
7

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






