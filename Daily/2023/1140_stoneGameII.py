from typing import *
from collections import defaultdict


class Solution:
    def dfs(self, idx, M):
        if idx >= self.size:
            return 0

        if (idx, M) in self.dp:
            return self.dp[(idx, M)]

        if 2 * M > self.size - idx:
            self.dp[(idx, M)] = self.suffix_sum[idx]
            return self.dp[(idx, M)]

        self.dp[(idx, M)] = 0
        ttl = 0
        for x in range(1, 2 * M + 1):
            if idx + x - 1 >= self.size:
                break
            ttl += self.piles[idx + x - 1]
            self.dp[(idx, M)] = max(
                self.dp[(idx, M)],
                (
                    ttl
                    + self.suffix_sum[idx + x]
                    - self.dfs(idx + x, max(x, M))
                )
            )

        return self.dp[(idx, M)]

    def stoneGameII(self, piles: List[int]) -> int:
        self.size = len(piles)
        self.piles = piles
        self.dp = defaultdict(int)
        self.suffix_sum = [0]
        for idx in range(self.size - 1, -1, -1):
            self.suffix_sum.append(self.suffix_sum[-1] + piles[idx])
        self.suffix_sum.reverse()

        return self.dfs(0, 1)
