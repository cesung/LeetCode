from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, left, right): 
        if left > right:
            return 0

        if left == right:
            return 1
        
        if (left, right) in self.rcd:
            return self.rcd[(left, right)]

        if self.s[left] == self.s[right]:
            self.rcd[(left, right)] = 2 + self.dfs(left + 1, right - 1)
        else:
            self.rcd[(left, right)] = max(
                self.dfs(left + 1, right),
                self.dfs(left, right - 1),
            )
        
        return self.rcd[(left, right)]

    def longestPalindromeSubseq(self, s: str) -> int:
        self.s = s
        self.rcd = defaultdict(int)
        
        return self.dfs(0, len(s) - 1)