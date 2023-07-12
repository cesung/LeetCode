from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, node):
        if node in self.safe:
            return self.safe[node]
        
        # handling cycle
        self.safe[node] = False
        for neighbor in self.graph[node]:
            if not self.dfs(neighbor):
                return False

        self.safe[node] = True
        
        return self.safe[node]

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        self.graph = graph
        self.safe = defaultdict(bool)

        self.ret = []
        for node in range(n):
            if self.dfs(node):
                self.ret.append(node)

        self.ret.sort()

        return self.ret