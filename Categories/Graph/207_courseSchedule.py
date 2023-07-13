from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, course: int, stk:List[int]) -> None:
        stk.append(course)
        for neighbor in self.graph[course]:
            if neighbor in stk:
                self.has_cycle = True
                return
            if neighbor in self.vis:
                continue
            self.vis.add(neighbor)
            self.dfs(neighbor, stk)
            stk.pop()

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = defaultdict(list)
        for prev, post in prerequisites:
            self.graph[prev].append(post)

        self.vis = set()
        self.has_cycle = False

        for course in range(numCourses):
            if course in self.vis:
                continue
        
            self.vis.add(course)
            self.dfs(course, [])
        
        return not self.has_cycle