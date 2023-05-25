from typing import *


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0

        # 0, 1, ... k + maxPts - 1
        dp = [0.0 for _ in range(k + maxPts)]
        prob = 1.0 / maxPts

        dp[0] = 1.0
        sumv = 1.0
        for idx in range(1, k + maxPts):
            dp[idx] = prob * sumv
            # when idx >= k, stop
            if idx < k:
                sumv += dp[idx]
            if idx > maxPts - 1:
                sumv -= dp[idx - maxPts]

        ret = 0.0
        for idx in range(k, min(k + maxPts, n + 1)):
            ret += dp[idx]

        return ret
