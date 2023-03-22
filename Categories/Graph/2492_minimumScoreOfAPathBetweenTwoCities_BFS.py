from typing import *
from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        INF = float('inf')
        graph = defaultdict(lambda : defaultdict(int))
        for n1, n2, dist in roads:
            graph[n1][n2] = graph[n2][n1] = dist
        
        queue = deque()
        queue.append(1)
        vis = set()
        
        min_dist = INF

        while queue:
            node = queue.popleft()
            vis.add(node)

            for neighbor in graph[node]:
                min_dist = min(
                    min_dist,
                    graph[node][neighbor],
                )
                if neighbor in vis:
                    continue
                queue.append(neighbor)
        
        return min_dist