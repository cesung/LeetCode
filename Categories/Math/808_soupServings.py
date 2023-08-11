from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, A, B, prob):
        if A == 0.0 and B == 0.0:
            return prob / 2
        elif A == 0.0:
            return prob
        elif B == 0.0:
            return 0.0
        
        if (A, B) in self.dp:
            return self.dp[(A, B)]
        
        self.dp[(A, B)] += self.dfs(max(0, A - 100), B, prob / 4)
        self.dp[(A, B)] += self.dfs(max(0, A - 75), max(0, B - 25), prob / 4)
        self.dp[(A, B)] += self.dfs(max(0, A - 50), max(0, B - 50), prob / 4)
        self.dp[(A, B)] += self.dfs(max(0, A - 25), max(0, B - 75), prob / 4)
        
        return self.dp[(A, B)]
    
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1
        
        self.ret = 0.0
        self.dp = defaultdict(float)
        
        return self.dfs(n, n, 1.0)
