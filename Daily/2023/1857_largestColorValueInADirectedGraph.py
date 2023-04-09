from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, node, path):
        if node not in self.graph:
            self.rcd[node][self.colors[node]] = 1
            return

        if node in path:
            self.is_cycle = True
            return
        if node in self.rcd:
            return

        path.add(node)
        rst = defaultdict(int)
        for neighbor in self.graph[node]:
            self.dfs(neighbor, path)
            if self.is_cycle == True:
                return
            for color in self.rcd[neighbor]:
                rst[color] = max(
                    rst[color],
                    self.rcd[neighbor][color]
                )
        rst[self.colors[node]] += 1
        path.remove(node)

        self.rcd[node] = rst

        return rst
            
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        size = len(colors)
        self.colors = colors
        self.graph = defaultdict(list)
        in_degree = [0 for _ in range(size)]
        for src, dst in edges:
            self.graph[src].append(dst)
            in_degree[dst] += 1

        self.rcd = defaultdict(lambda : defaultdict(int))
        self.is_cycle = False
        
        rst = -1
        for node in range(size):
            self.dfs(node, set())
            if self.is_cycle == True:
                return -1
            rst = max(
                rst,
                max(self.rcd[node].values())
            )

        return rst