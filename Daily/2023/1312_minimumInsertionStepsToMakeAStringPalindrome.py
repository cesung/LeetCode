from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, left:int, right:int) -> int:
        if left >= right:
            return 0

        if (left, right) in self.dp:
            return self.dp[(left, right)]
        
        if self.s[left] == self.s[right]:
            self.dp[(left, right)] = self.dfs(left + 1, right - 1)
        else:
            self.dp[(left, right)] = min(
                self.dfs(left + 1, right),
                self.dfs(left, right - 1),
            ) + 1
        
        return self.dp[(left, right)]
            
    def minInsertions(self, s: str) -> int:
        self.s = s
        size = len(s)
        self.dp = defaultdict(int)

        return self.dfs(0, size - 1)