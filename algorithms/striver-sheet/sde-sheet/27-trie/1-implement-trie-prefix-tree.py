"""
Implement Trie (Prefix Tree)

Problem Link:
https://leetcode.com/problems/implement-trie-prefix-tree/description/

Statement
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.



Test Case:
N/A (check the problem link)
"""

"""
Time complexity: N/A
Space Complexity: N/A
"""

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
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)