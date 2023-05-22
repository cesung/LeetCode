from typing import *

class UnionFind:
    def __init__(self, size):
        self.parents = [ _ for _ in range(size)]
        self.ranks = [1 for _ in range(size)]

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
    def isBipartite(self, graph: List[List[int]]) -> bool:
        size = len(graph)
        union_find = UnionFind(size)

        for node in range(len(graph)):
            for neighbor in graph[node]:
                # is belongs to same group?
                if union_find.find(node) == union_find.find(neighbor):
                    return False
                else:
                    union_find.union(graph[node][0], neighbor)

        return True