from typing import *
from collections import defaultdict

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k

        dp = defaultdict(lambda : defaultdict(int))
        # dp[idx start with 1 ~ n includesive][
        #     0: prev two fences with same color
        #     1: prev two fences with diff color
        # ]
        dp[2][0] = k * (k-1)
        dp[2][1] = k

        for idx in range(3, n + 1):
            dp[idx][0] = dp[idx - 1][0] * (k - 1) + dp[idx - 1][1] * (k - 1)
            dp[idx][1] = dp[idx - 1][0] 

        return sum(dp[n].values())