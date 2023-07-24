from typing import *

class Solution:
    def dfs(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n % 2 == 1:
            return x * self.dfs(x*x, (n-1)//2)
        else:
            return self.dfs(x*x, n // 2)
    
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        
        return self.dfs(x, n) if n > 0 else 1.0 / self.dfs(x, -n)