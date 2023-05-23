from typing import *
from collections import deque
from collections import defaultdict

class Solution:
    def bfs(self, src, tar):
        vis = set()
        queue = deque([[src, 1]])
        
        while queue:
            node, val = queue.popleft()
            if node in vis:
                continue
            vis.add(node)

            if node == tar:
                return val
            
            for neighbor in self.graph[node]:
                queue.append([neighbor, val * self.graph[node][neighbor]])
        
        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = defaultdict(lambda : defaultdict(float))
        for equation, value in zip(equations, values):
            dividend, divisor = equation
            self.graph[dividend][divisor] = value
            self.graph[divisor][dividend] = 1/value

        ret = []
        for query in queries:
            src, tar = query
            if (
                src not in self.graph or
                tar not in self.graph
            ):
                ret.append(-1)
                continue

            ret.append(self.bfs(src, tar))

        return ret