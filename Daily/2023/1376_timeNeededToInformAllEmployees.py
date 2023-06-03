from typing import *
from collections import defaultdict


class Solution:
    def dfs(self, node):
        maxt = -self.INF
        for neighbor, t in self.graph[node]:
            maxt = max(
                maxt,
                t + self.dfs(neighbor),
            )

        return maxt if maxt != -self.INF else 0

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.INF = float('inf')
        self.graph = defaultdict(list)

        for idx in range(n):
            self.graph[manager[idx]].append((idx, informTime[idx]))

        return self.dfs(headID) + informTime[headID]
