from typing import *
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = [idx for idx in range(size)]
        self.ranks = [1 for _ in range(size)]
    
    def find(self, n):
        root = n
        while root != self.parent[root]:
            root = self.parent[root]
        
        # path compression
        cur = n
        while cur != root:
            nxt = self.parent[cur]
            self.parent[cur] = root
            cur = nxt

        return root

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return 
        
        # union by ranks
        if self.ranks[p1] > self.ranks[p2]:
            self.parent[p2] = p1
            self.ranks[p1] += self.ranks[p2]
        else:
            self.parent[p1] = p2
            self.ranks[p2] += self.ranks[p1]


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)

        for node1, node2 in edges:
            union_find.union(node1, node2)
        
        group = defaultdict(int)
        for node in range(n):
            root = union_find.find(node)
            group[root] += 1
        
        group_lst = list(group.values())

        cur, ttl = group_lst[0], 0
        for idx in range(1, len(group_lst)):
            ttl += cur * group_lst[idx]
            cur += group_lst[idx]

        return ttl
        