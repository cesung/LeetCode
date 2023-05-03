from typing import *
import copy

class UnionFind:
    def __init__(self, size):
        self.parents = [idx for idx in range(size)]
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
            return -1
        
        if self.ranks[r1] > self.ranks[r2]:
            self.parents[r2] = r1
            self.ranks[r1] += self.ranks[r2]
        else:
            self.parents[r1] = r2
            self.ranks[r2] += self.ranks[r1]

class Solution:
    def helper(self, n, edges, graph):
        cnt = 0
        for n1, n2 in edges:
            if graph.union(n1, n2) == -1:
                cnt += 1

        group = set()
        for idx in range(1, n + 1):
            group.add(graph.find(idx))
        
        return -1 if len(group) != 1 else cnt

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        shared_graph = UnionFind(n + 1)
        alice_edges, bob_edges = [], []
        ret = 0

        for t, n1, n2 in edges:
            if t == 1:
                alice_edges.append([n1, n2])
            elif t == 2:
                bob_edges.append([n1, n2])
            else:
                if shared_graph.union(n1, n2) == -1:
                    ret += 1
        
        alice_graph = copy.deepcopy(shared_graph)
        bob_graph = copy.deepcopy(shared_graph)

        alice_cnt = self.helper(n, alice_edges, alice_graph)
        bob_cnt = self.helper(n, bob_edges, bob_graph)

        return -1 if (
            alice_cnt == -1 or 
            bob_cnt == -1
        ) else ret + alice_cnt + bob_cnt