from typing import *
from collections import defaultdict


class Trie:
    def __init__(self) -> None:
        self.next = defaultdict(Trie)
        self.end = False

    def insert(self, word: str) -> None:
        root = self

        for ch in word:
            root = root.next[ch]
        root.end = True

    def search(self, word: str) -> bool:
        root = self

        for ch in word:
            if ch not in word:
                return False
            root = root.next[ch]

        return root.end
