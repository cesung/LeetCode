from typing import *
from collections import defaultdict

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10**9 + 7

        size = len(types)
        types = [[0, 0]] + types
        
        # dp[from 0 to i^th item][ways to earn j points]
        dp = defaultdict(lambda : defaultdict(int))
        dp[0][0] = 1 # before seeing any item, how many ways we can earn 0 point => 1

        for idx in range(1, size + 1):
            for jdx in range(target + 1):
                for kdx in range(types[idx][0] + 1):
                    if jdx - kdx * types[idx][1] < 0:
                        break
                    dp[idx][jdx] = (
                        dp[idx][jdx] + dp[idx - 1][jdx - kdx * types[idx][1]]
                    ) % MOD

        return dp[size][target]