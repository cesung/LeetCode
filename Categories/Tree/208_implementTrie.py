from typing import *
from collections import defaultdict

class Trie:

    def __init__(self):
        self.next = defaultdict(Trie)
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            node = node.next[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            if ch not in node.next:
                return False
            node = node.next[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            if ch not in node.next:
                return False
            node = node.next[ch]
        
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)