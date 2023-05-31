from typing import *
from collections import defaultdict


class Solution:
    def dfs(self, idx):
        if idx >= self.size:
            return 0

        if idx in self.dp:
            return self.dp[idx]

        ttl = 0
        for jdx in range(3):
            if idx + jdx == self.size:
                break
            ttl += self.stoneValue[idx + jdx]
            self.dp[idx] = max(
                self.dp[idx],
                (
                    ttl +
                    self.suffix[idx + jdx + 1] -
                    self.dfs(idx + jdx + 1)
                )
            )

        return self.dp[idx]

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        INF = float('inf')

        self.size = len(stoneValue)
        self.stoneValue = stoneValue
        self.dp = defaultdict(lambda: -INF)

        self.suffix = [0]
        for idx in range(self.size - 1, -1, -1):
            self.suffix.append(self.suffix[-1] + self.stoneValue[idx])
        self.suffix.reverse()

        alice = self.dfs(0)
        bob = self.suffix[0] - alice

        if alice == bob:
            return 'Tie'

        return 'Alice' if alice > bob else 'Bob'
