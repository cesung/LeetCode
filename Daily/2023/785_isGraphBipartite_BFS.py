from typing import *
from collections import deque, defaultdict

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        size = len(graph)
        colors, vis = defaultdict(set), set()
        for node in range(size):
            if node in vis:
                continue

            queue = deque([ (node, 0) ])
        
            while queue:
                node, color = queue.popleft()
                vis.add(node)

                for neighbor in graph[node]:
                    if neighbor in vis:
                        continue

                    if neighbor in colors[color]:
                        return False
                    
                    colors[1-color].add(neighbor)
                    queue.append( (neighbor, 1 - color) )
        
        return True
