from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, node):
        if node in self.vis:
            return
        self.vis.add(node)

        for neighbor in self.graph[node]:
            self.min_dist = min(
                self.min_dist, 
                self.graph[node][neighbor],
            )
            self.dfs(neighbor)

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        INF = float('inf')
        self.graph = defaultdict(lambda : defaultdict(int))
        for n1, n2, dist in roads:
            self.graph[n1][n2] = self.graph[n2][n1] = dist
        
        self.vis = set()
        self.min_dist = INF
        self.dfs(1)

        return self.min_dist