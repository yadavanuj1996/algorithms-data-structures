"""
insert/search: O(L)
SC: O(total chars)
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
