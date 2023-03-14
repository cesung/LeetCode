from typing import *
from collections import defaultdict, deque

class Solution:

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_graph, blue_graph = defaultdict(list), defaultdict(list)

        for red_edge in red_edges:
            red_graph[red_edge[0]].append(red_edge[1])
        for blue_edge in blue_edges:
            blue_graph[blue_edge[0]].append(blue_edge[1])


        ret = [-1 for _ in range(n)]
        
        queue = deque()
        queue.append( (0, None, 0))
        vis = set()
        vis.add( (0, None) )
        
        while queue:
            node, prev, step = queue.popleft()
            if ret[node] == -1:
                ret[node] = step
            
            if prev != "B":
                for blue_neighbor in blue_graph[node]:
                    if (blue_neighbor, "B") in vis:
                        continue
                    vis.add( (blue_neighbor, "B") )
                    queue.append( (blue_neighbor, "B", step + 1) )
            if prev != "R":
                for red_neighbor in red_graph[node]:
                    if (red_neighbor, "R") in vis:
                        continue
                    vis.add( (red_neighbor, "R") )
                    queue.append( (red_neighbor, "R", step + 1) )
        
        return ret