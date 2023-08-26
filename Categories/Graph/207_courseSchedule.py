from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, node: int, stk: List[int]) -> bool:
        if node in stk:
            return False
        stk.append(node)
        
        for neighbor in self.graph[node]:
            if neighbor in self.vis:
                continue
            if not self.dfs(neighbor, stk):
                return False
        
        stk.pop()
        self.vis.add(node)
        
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = defaultdict(list)
        for cur, prev in prerequisites:
            self.graph[prev].append(cur)
        
        self.vis = set()
        for node in range(numCourses):
            if node in self.vis:
                continue
            if not self.dfs(node, []):
                return False
        
        return True