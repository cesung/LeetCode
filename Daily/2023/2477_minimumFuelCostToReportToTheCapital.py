import math
from typing import *
from collections import defaultdict

class Solution:

    def dfs(self, node, parent):
        # leaf node
        if len(self.graph[node]) == 1 and self.graph[node][0] == parent:
            return 1
        
        cnt = 0
        for neighbor in self.graph[node]:
            if neighbor == parent:
                continue
            neighbor_cnt = self.dfs(neighbor, node)
            cnt += neighbor_cnt
            # cost
            self.ttl += math.ceil(neighbor_cnt/ self.seats)
    
        return cnt + 1
            
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.seats = seats
        
        self.graph = defaultdict(list)
        for n1, n2 in roads:
            self.graph[n1].append(n2)
            self.graph[n2].append(n1)
        
        self.ttl = 0
        self.dfs(0, -1)

        return self.ttl