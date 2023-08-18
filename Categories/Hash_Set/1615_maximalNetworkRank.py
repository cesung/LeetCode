from typing import *
from collections import defaultdict
    
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = defaultdict(int)
        vis = set()
        
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            vis.add( (a,b) )
        
        ret = -1
        for n1 in range(n):
            for n2 in range(n1 + 1, n):
                ret = max(
                    ret,
                    (
                        degree[n1] + 
                        degree[n2] - 
                        (1 if ((n1, n2) in vis or (n2, n1) in vis) else 0)
                    )
                )
        
        return ret
        