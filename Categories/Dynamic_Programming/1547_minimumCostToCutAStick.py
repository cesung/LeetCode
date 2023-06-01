from typing import *
from collections import defaultdict


class Solution:
    def dfs(self, left: int, right: int) -> int:
        if left == right:
            return 0

        if (left, right) in self.dp:
            return self.dp[(left, right)]

        self.dp[(left, right)] = self.INF
        for cut in self.cuts:
            # if it is a valid cut
            if left < cut < right:
                self.dp[(left, right)] = min(
                    self.dp[(left, right)],
                    (
                        right - left +
                        self.dfs(left, cut) +
                        self.dfs(cut, right)
                    ),
                )
        self.dp[(left, right)] = 0 if (
            self.dp[(left, right)] == self.INF
        ) else self.dp[(left, right)]

        return self.dp[(left, right)]

    def minCost(self, n: int, cuts: List[int]) -> int:
        self.INF = float('inf')
        self.cuts = cuts
        self.dp = defaultdict(int)

        return self.dfs(0, n)
