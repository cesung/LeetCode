from typing import *
from collections import defaultdict

""" 
replace:
    word1 = [X X X X idx]
    word2 = [Y Y Y Y Y Y jdx]

    idx != jdx, either
        . replace idx -> jdx => dp[idx - 1][jdx - 1] + 1
            word1 = [X X X X] jdx
            word2 = [Y Y Y Y Y Y] jdx

        . replace jdx -> idx => dp[idx - 1][jdx - 1] + 1
            word1 = [X X X X] idx
            word2 = [Y Y Y Y Y Y] idx
"""

"""
insert
    word1 = X X X X idx
    word2 = Y Y Y Y Y Y jdx

    idx != jdx, either
        . insert jdx at the end of word1 => dp[idx][jdx - 1] + 1
            word1 = [X X X X idx] jdx
            word2 = [Y Y Y Y Y Y] jdx

        . insert idx at the end of word2 => dp[idx - 1][jdx] + 1
            word1 = [X X X X] idx
            word2 = [Y Y Y Y Y Y jdx] idx
"""

"""
delete
    word1 = X X X X idx
    word2 = Y Y Y Y Y Y jdx

    idx != jdx, either
        . delete idx at the end of word1 => dp[idx - 1][jdx] + 1
            word1 = [X X X X]
            word2 = [Y Y Y Y Y Y jdx]

        . delete jdx at the end of word2 => dp[idx][jdx - 1] + 1
            word1 = [X X X X idx]
            word2 = [Y Y Y Y Y Y]
"""

"""
Summary:
    dp[idx - 1][jdx] + 1:
        . delete idx at the end of word1 OR
        . insert idx at the end of word2

    dp[idx][jdx - 1] + 1:
        . delete jdx at the end of word2 OR
        . insert jdx at the end of word1

    dp[idx - 1][jdx - 1] + 1:
        . replace idx at the end of word1 to jdx
        . replace jdx at the end of word2 to idx
"""

class Solution:

    def dfs(self, ptr1, ptr2):

        if ptr1 == -1:
            return ptr2 + 1
        elif ptr2 == -1:
            return ptr1 + 1
        
        if (ptr1, ptr2) in self.rcd:
            return self.rcd[ptr1, ptr2]
        
        if self.word1[ptr1] == self.word2[ptr2]:
            self.rcd[ptr1,ptr2] = self.dfs(ptr1 - 1, ptr2 - 1)
        else:
            self.rcd[ptr1,ptr2] = min(
                self.dfs(ptr1 - 1, ptr2),
                self.dfs(ptr1, ptr2 - 1),
                self.dfs(ptr1 - 1, ptr2 - 1)
            ) + 1

        return self.rcd[ptr1,ptr2]

    def minDistance(self, word1: str, word2: str) -> int:
        self.word1, self.word2 = word1, word2
        self.len1, self.len2 = len(word1), len(word2)

        if self.len1 == 0 and self.len2 == 0:
            0
        if self.len1 == 0 or self.len2 == 0:
            return max(
                self.len1,
                self.len2
            )

        self.rcd = defaultdict(int)

        return self.dfs(self.len1 - 1, self.len2 - 1)
