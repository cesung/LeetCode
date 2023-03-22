from typing import *

class UnionFind:
    def __init__(self, size):
        self.parents = [idx for idx in range(size + 1)]
        self.ranks = [1 for _ in range(size + 1)]

    def find(self, n):
        root = n
        while root != self.parents[root]:
            root = self.parents[root]

        cur = n
        while cur != root:
            nxt = self.parents[cur]
            self.parents[cur] = root
            cur = nxt
        
        return root

    def union(self, n1, n2):
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
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        INF = float('inf')

        union_find = UnionFind(n)
        for n1, n2, dist in roads:
            union_find.union(n1, n2)
        
        min_dist = INF
        for n1, n2, dist in roads:
            if union_find.find(1) == union_find.find(n1):
                min_dist = min(
                    min_dist,
                    dist
                )

        return min_dist