import heapq
from typing import *
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        graph = defaultdict(lambda : defaultdict(int))
        for u, v, w in times:
            graph[u][v] = w

        dists = [INF for _ in range(n + 1)]
        dists[k] = 0
        
        vis = set()

        pq = [ (0, k) ]
        while pq:
            dist, node = heapq.heappop(pq)

            if node in vis:
                continue
            vis.add(node)

            for neighbor in graph[node]:
                if dist + graph[node][neighbor] < dists[neighbor]:
                    dists[neighbor] = dist + graph[node][neighbor]
                    heapq.heappush(pq, (dist + graph[node][neighbor], neighbor))
    
        ret = max(dists[1:])

        return ret if ret != INF else -1