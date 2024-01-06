# Trie

## Introduction
- Trie and is also known as a Prefix Tree. 
- Trie is a tree-like data structure that proves to be really efficient while solving programming problems related to strings.
- The tree trie is derived from “retrieval.” As you can guess, the main purpose of using this structure is to provide fast retrieval. 
- Tries are mostly used in dictionary word searches, search engine auto-suggestions, and IP routing as well.

![Screenshot 2022-11-16 at 7 29 59 PM](https://user-images.githubusercontent.com/22169012/202200371-1ea62f17-df5e-4e34-92cc-4e4d3961f3e1.png)


## Applications of Tries
- Autocomplete Words
- Spell-Checking
- Searching for a Phone Contact

## Properties of a Trie
- Tries are similar to graphs as they are a combination of nodes where each node represents a unique letter.
- Each node can point to None or other children nodes.
- The size of a trie depends upon the number of characters. For example, in the English alphabet, there are 26 letters so the number of unique nodes cannot exceed 26.
- The depth of a trie depends on the longest word that it stores.
- Another important property of a trie is that it provides the same path for words which share a common prefix. For example, “there” and “their” have a common prefix “the.” Hence, they will share the same path till “e.” After that, the path will split into two branches. This is the backbone of the trie functionality.


### Code implemetation of Trie
- TrieNode will contain a links array and a end flag

![IMG_4863](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/0c4ac27d-2363-4d82-a041-375af2a30f42)

```
class Node:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False
        
    def contains_key(self, ch: str) -> 'Node':
        return self.links[ord(ch)-ord("a")]     # ord returns ascii code of character

    # fn that returns node reference for char ch
    def get(self, ch: str) -> 'Node':
        return self.links[ord(ch)-ord("a")]
    
    def put(self, ch: str, node: 'Node') -> None:
        self.links[ord(ch)-ord("a")] = node
    
    def set_end(self) -> 'Node':
        self.flag = True
    
    def is_end(self) -> bool:
        return self.flag




class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                node.put(cur_char, Node())
            node = node.get(cur_char)
        node.set_end()

    def search(self, word: str) -> bool:
        node = self.root
        for cur_char in word:
            if not node.contains_key(cur_char):
                return False

            node = node.get(cur_char)
        
        return node.is_end()

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for cur_char in prefix:
            if not node.contains_key(cur_char):
                return False

            node = node.get(cur_char)
        
        return True
        

```


### Code implementation of trie with prefix count and ends with
This trie will be used in case same words can be added multiple times or we need to know the prefix count as well

```
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

```


### Trie Xor related problems approach
We will use a TrieNode with links length 2, 0 and 1 index to represent the two allowed bits of a binary no.

![Screenshot 2024-01-06 at 1 17 45 PM](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/0af5505c-4f49-4447-aaa1-ff39aec17915)


```

class TrieNode:
    def __init__(self):
        self.links = [None]*2
    
    def contains_key(self, bit: int)->bool:
        return self.links[bit] is not None

    def get(self, bit: int)-> "TrieNode":
        return self.links[bit]
    
    def put(self, bit: int, node: "TrieNode")->None:
        self.links[bit] = node
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num: int):
        binary_str = '{:032b}'.format(num)
        node = self.root
        for cur_char in binary_str:
            cur_bit = int(cur_char)
            if not node.contains_key(cur_bit):
                node.put(cur_bit, TrieNode())

            node = node.get(cur_bit)
    
    def find_max_xor(self, num: int):
        binary_str = '{:032b}'.format(num)
        node = self.root
        result = ""
        for cur_char in binary_str:
            cur_bit = int(cur_char)
            reverse_bit = 1 - cur_bit   # 0 for 1 and 1 for 0, flipping the bit

            if node.contains_key(reverse_bit):
                result += "1"                # cur_bit^reverse_bit will alwasy give 1
                node = node.get(reverse_bit)
            else:
                result += "0"                 # cur_bit^cur_bit will alwasy give 0
                node = node.get(cur_bit)
            
        return int(result, 2)


```

![Screenshot 2024-01-06 at 1 18 41 PM](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/e4be2d8f-58b2-4100-b4cb-dd6751e2bed7)




