from typing import *


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = [idx for idx in range(n)]
        self.ranks = [1 for _ in range(n)]
    
    def find(self, n: int) -> int:
        root = n
        while root != self.parents[root]:
            root = self.parents[root]
        
        cur = n
        while cur != root:
            nxt = self.parents[cur]
            self.parents[cur] = root
            cur = nxt
        
        return root
    
    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.ranks[p1] > self.ranks[p2]:
            self.ranks[p1] += self.ranks[p2]
            self.parents[p2] = p1
        else: 
            self.ranks[p2] += self.ranks[p1]
            self.parents[p1] = p2
        
        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()

        union_find = UnionFind(n)

        num_groups = n
        for log in logs:
            t, n1, n2 = log
            if union_find.union(n1, n2):
                num_groups -= 1
        
            if num_groups == 1:
                return t
        
        return -1