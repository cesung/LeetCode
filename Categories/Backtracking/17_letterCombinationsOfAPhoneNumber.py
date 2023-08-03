from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, idx: int) -> List[str]:
        if idx == self.n:
            return [""]
        
        cur_comb = []
        for ch in self.rcd[self.digits[idx]]:
            for comb in self.dfs(idx + 1):
                cur_comb.append(ch + comb)
        
        return cur_comb
            
    
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        self.n = len(digits)
        self.digits = digits
        
        self.rcd = defaultdict(list, {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z'],
        })

        return self.dfs(0)