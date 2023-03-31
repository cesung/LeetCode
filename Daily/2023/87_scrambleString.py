from typing import *

class Solution:
    def dfs(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if (s1, s2) in self.dp:
            return self.dp[(s1, s2)]

        if Counter(s1) != Counter(s2):
            return False

        #    idx          size - idx - 1
        # [0 : idx)[idx : size)
        # [size - idx : size)[0:size - idx)
        size = len(s1)
        for idx in range(1, size):
            if (
                self.dfs(s1[:idx], s2[:idx]) and
                self.dfs(s1[idx:], s2[idx:])
            ):
                self.dp[(s1, s2)] = True
            
            if self.dp[(s1, s2)] == True:
                return True
            
            if (
                self.dfs(s1[:idx], s2[size - idx:]) and
                self.dfs(s1[idx:size], s2[:size - idx])
            ):
                self.dp[(s1, s2)] = True

            if self.dp[(s1, s2)] == True:
                return True
        
        return False

    def isScramble(self, s1: str, s2: str) -> bool:
        self.dp = defaultdict(bool)
        return self.dfs(s1, s2)