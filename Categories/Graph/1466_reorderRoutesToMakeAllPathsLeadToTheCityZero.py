from typing import *
from collections import defaultdict

class Solution:

    def dfs(self, node, parent):
        for neighbor in self.graph[node]:
            if neighbor == parent:
                continue
            if (node, neighbor) in self.edges:
                self.cnt += 1
            self.dfs(neighbor, node)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        self.edges = set()
        self.cnt = 0
        for src, tar in connections:
            self.edges.add( (src, tar) )
            self.graph[src].append(tar)
            self.graph[tar].append(src)
    
        self.dfs(0, -1)

        return self.cnt