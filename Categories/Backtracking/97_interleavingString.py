from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, p1: int, p2: int, p3: int) -> bool:
        if (
            p1 == self.n1 and
            p2 == self.n2 and
            p3 == self.n3
        ):
            return True
        
        if (p1, p2, p3) in self.rcd:
            return self.rcd[ (p1, p2, p3) ]
    
        self.rcd[ (p1, p2, p3) ] = False
        if (
            p1 < self.n1 and 
            p3 < self.n3 and
            self.s1[p1] == self.s3[p3]
        ):
            self.rcd[ (p1, p2, p3) ] |= self.dfs(p1 + 1, p2, p3 + 1)
        if (
            p2 < self.n2 and
            p3 < self.n3 and
            self.s2[p2] == self.s3[p3]
        ):
            self.rcd[ (p1, p2, p3) ] |= self.dfs(p1, p2 + 1, p3 + 1)
        
        return self.rcd[ (p1, p2, p3) ]
        
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.n1, self.n2, self.n3 = len(s1), len(s2), len(s3)
        if self.n1 + self.n2 != self.n3:
            return False
    
        self.s1, self.s2, self.s3 = s1, s2, s3
        self.rcd = defaultdict(bool)
        return self.dfs(0, 0, 0)