from typing import *


class UnionFind:
    def __init__(self, n):
        self.parents = [idx for idx in range(n + 1)]
        self.ranks = [1 for _ in range(n + 1)]

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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        union_find = UnionFind(n)

        for idx in range(1, n + 1):
            for jdx in range(idx + 1, n + 1):
                if idx == jdx:
                    continue
                if isConnected[idx - 1][jdx - 1]:
                    union_find.union(idx, jdx)

        vis = set()
        for idx in range(1, n + 1):
            vis.add(union_find.find(idx))

        return len(vis)
