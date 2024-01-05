"""
Complete String

Problem Link:
https://www.codingninjas.com/studio/problems/complete-string_2687860?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTabValue=PROBLEM

Statement
Ninja developed a love for arrays and strings so this time his teacher gave him an array of strings, ‘A’ of 
size ‘N’. Each element of this array is a string. The teacher taught Ninja about prefixes in the past, so he 
wants to test his knowledge.

A string is called a complete string if every prefix of this string is also present in the array ‘A’. Ninja is 
challenged to find the longest complete string in the array ‘A’.If there are multiple strings with the same
length, return the lexicographically smallest one and if no string exists, return "None".

Constraints:
- 1 <= T <= 10
- 1 <= N <= 10^5
- 1 <= A[i].length <= 10^5
- A[i] only consists of lowercase english letters.
- Sum of A[i].length <= 10^5 over all test cases


Test Case:

Input:
2
6
n ni nin ninj ninja ninga
2
ab bc

Output:
ninja
None

"""

"""
Time complexity: O(N * Len), len is length of word and N is total no of elements in input array
Space Complexity: Cannot be calculated
"""

from os import *
from sys import *
from collections import *
from math import *

from typing import *

class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.is_end_flag = False

    def contains_key(self, ch: str) -> bool:
        return self.links[ord(ch)-ord("a")] is not None
    
    def get(self, ch:str) -> "Node":
        return self.links[ord(ch)-ord("a")]
    
    def put(self, ch: str, node: "Node")->None:
        self.links[ord(ch)-ord("a")] = node
    
    def set_end(self)->None:
        self.is_end_flag = True
    
    def is_end(self)->bool:
        return self.is_end_flag


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str)-> None:
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                node.put(cur_char, TrieNode())
            node = node.get(cur_char)
        node.set_end()
        
    def search_complete_string(self, word: str)->bool:
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                return False
            node = node.get(cur_char)
            if not node.is_end():
                return False

        return True
        

def completeString(n: int, a: List[str])-> str:
    trie = Trie()
    
    for word in a:
        trie.insert(word)
    
    result = ""
    
    for word in a:
        if trie.search_complete_string(word):
            if len(word) > len(result):
                result = word
            elif len(word) == len(result):
                # lexicographical comparison
                result = word if word < result else result


    return result if result else None




