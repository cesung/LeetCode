from typing import *

class UnionFind:
    def __init__(self, size):
        self.parent = [idx for idx in range(size)]
        self.ranks = [1 for _ in range(size)]

    def find(self, n):
        root = n
        while root != self.parent[root]:
            root = self.parent[root]
        
        cur = n
        while cur != root:
            nxt = self.parent[cur]
            self.parent[cur] = root
            cur = nxt

        return root

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return 1
        
        if self.ranks[p1] < self.ranks[p2]:
            self.parent[p1] = p2
            self.ranks[p2] += self.ranks[p1]
        else:
            self.parent[p2] = p1
            self.ranks[p1] += self.ranks[p2]
        
        return 0

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        union_find = UnionFind(n)

        num_redundant = 0
        for n1, n2 in connections:
            num_redundant += union_find.union(n1, n2)

        components = set()
        for nid in range(n):
            components.add(union_find.find(nid))
        
        return -1 if num_redundant < len(components) - 1 else len(components) - 1
        