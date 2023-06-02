from typing import *
from collections import defaultdict
import math


class Solution:
    def cal_dist(self, x1: int, y1: int, x2: int, y2: int) -> float:
        return math.sqrt(
            (x1 - x2) ** 2 +
            (y1 - y2) ** 2
        )

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)

        for idx in range(n):
            for jdx in range(idx + 1, n):
                x1, y1, r1 = bombs[idx]
                x2, y2, r2 = bombs[jdx]
                dist = self.cal_dist(x1, y1, x2, y2)

                if r1 >= dist:
                    graph[idx].append(jdx)
                if r2 >= dist:
                    graph[jdx].append(idx)

        max_bomb = -1
        for idx in range(n):
            queue = deque([idx])
            vis = set([idx])

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in vis:
                        continue
                    vis.add(neighbor)

                    queue.append(neighbor)

            max_bomb = max(
                max_bomb,
                len(vis)
            )

        return max_bomb
