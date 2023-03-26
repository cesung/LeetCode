from typing import *

class Solution:
    def minTimeToType(self, word: str) -> int:
        ttl = 0
        word = 'a' + word
        size = len(word)
        for idx in range(1, size):
            diff = abs(ord(word[idx]) - ord(word[idx - 1]))
            ttl += min(
                diff,
                26 - diff
            )

        return ttl + len(word) - 1