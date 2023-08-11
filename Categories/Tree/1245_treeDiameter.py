from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, node, parent):
        children_length = []
        for child in self.graph[node]:
            if child == parent:
                continue
            children_length.append(self.dfs(child, node))
        
        children_length.sort(reverse=True)

        if len(children_length) > 0:
            self.ret = max(
                self.ret,
                children_length[0] + (0 if len(children_length) == 1 else children_length[1])
            )
            
        return 1 if not children_length else children_length[0] + 1
    
    def treeDiameter(self, edges: List[List[int]]) -> int:
        self.ret = 0
        self.graph = defaultdict(list)
        
        for n1, n2 in edges:
            self.graph[n1].append(n2)
            self.graph[n2].append(n1)
        
        self.dfs(0, -1)
        
        return self.ret