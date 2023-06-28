import heapq
from typing import *
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(lambda : defaultdict(float))

        for (n1, n2), prob in zip(edges, succProb):
            graph[n1][n2] = graph[n2][n1] = prob
        
        probs = [0.0 for _ in range(n)]
        probs[start] = 1.0

        pq = [ (-1.0, start) ]
        vis = set();

        while pq:
            prob, node = heapq.heappop(pq)
            prob *= -1

            if node == end:
                return prob

            if node in vis: 
                continue
            vis.add(node)

            for neighbor in graph[node]:
                if prob * graph[node][neighbor] > probs[neighbor]:
                    probs[neighbor] = prob * graph[node][neighbor]
                    heapq.heappush(pq, (-1 * prob * graph[node][neighbor], neighbor))
        
        return 0.0

        

        
 