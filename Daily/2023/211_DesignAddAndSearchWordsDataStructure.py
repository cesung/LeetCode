from typing import *
from collections import defaultdict

class Trie:

    def __init__(self):
        self.next = defaultdict(Trie)
        self.is_end = False

    def insert(self, word):
        node = self
        for ch in word:
            node = node.next[ch]
        node.is_end = True

    def search_from(self, node, word):
        for idx, ch in enumerate(word):
            if ch in node.next:
                node = node.next[ch]
            elif ch == '.':
                for next_ch in node.next:
                    if self.search_from(node.next[next_ch], word[idx + 1:]):
                        return True
                return False
            else:
                return False
        
        return node.is_end

    def search(self, word):
        node = self
        return self.search_from(node, word)

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)
        
    def search(self, word: str) -> bool:
        return self.trie.search(word)
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)