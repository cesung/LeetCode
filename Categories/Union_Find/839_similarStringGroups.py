from typing import *

class UnionFind:
    def __init__(self, size: int) -> None:
        self.parents = [idx for idx in range(size)]
        self.ranks = [1 for _ in range(size)]
    
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

    def union(self, n1: int, n2: int) -> None:
        r1, r2 = self.find(n1), self.find(n2)
        if r1 == r2:
            return
        
        if self.ranks[r1] > self.ranks[r2]:
            self.parents[r2] = r1
            self.ranks[r1] += self.ranks[r2]
        else:
            self.parents[r1] = r2
            self.ranks[r2] += self.ranks[r1]

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        strs_size = len(strs)
        str_size = len(strs[0])

        union_find = UnionFind(strs_size)

        for idx in range(strs_size):
            for jdx in range(idx + 1, strs_size):
                diff = 0
                for kdx in range(str_size):
                    if strs[idx][kdx] != strs[jdx][kdx]: 
                        diff += 1
                if diff == 0 or diff == 2:
                    union_find.union(idx, jdx)
        
        groups = set()
        for idx in range(strs_size):
            groups.add(union_find.find(idx))
        
        return len(groups)