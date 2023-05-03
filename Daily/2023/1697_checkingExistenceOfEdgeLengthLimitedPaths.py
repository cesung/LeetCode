from typing import *

class UnionFind:
    def __init__(self, size: int) -> None:
        self.parents = [idx for idx in range(size)]
        self.ranks = [1 for _ in range(size)]

    def find(self, n: int) -> int:
        root = n
        while self.parents[root] != root:
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
    def distanceLimitedPathsExist(self, n: int, edge_list: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edge_size = len(edge_list); queries_size = len(queries)
        queries = [
            (p, q, limit, idx)
            for idx, (p, q, limit) in enumerate(queries)
        ]
        edge_list.sort(key = lambda x : x[2]); queries.sort(key = lambda x : x[2])

        union_find = UnionFind(n)
        ret = [None for _ in range(queries_size)]

        jdx = 0
        for idx in range(len(queries)):
            prev_jdx = jdx
            while (
                jdx < edge_size and
                edge_list[jdx][2] < queries[idx][2]
            ):
                jdx += 1

            for kdx in range(prev_jdx, jdx):
                union_find.union(edge_list[kdx][0], edge_list[kdx][1])

            ret[queries[idx][3]] = union_find.find(queries[idx][0]) == union_find.find(queries[idx][1])

        return ret