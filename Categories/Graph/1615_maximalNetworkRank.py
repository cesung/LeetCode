from typing import *
from collections import defaultdict
    
        
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(int)
        vis = set()
        for n1, n2 in roads:
            graph[n1] += 1
            graph[n2] += 1
            vis.add( (n1, n2) )

        max_rank = 0
        for n1 in range(n):
            for n2 in range(n1 + 1, n):
                cur_rank = graph[n1] + graph[n2]
                cur_rank -= 1 if (
                    (n1, n2) in vis or 
                    (n2, n1) in vis 
                ) else 0

                max_rank = max(
                    max_rank,
                    cur_rank
                )
        
        return max_rank
