from typing import *


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0 for _ in range(high + 1)]
        dp[0] = 1
        for idx in range(1, high + 1):
            dp[idx] += dp[idx - zero] if idx - zero >= 0 else 0
            dp[idx] %= MOD
            dp[idx] += dp[idx - one] if idx - one >= 0 else 0
            dp[idx] %= MOD

        return sum(dp[low: high + 1]) % MOD
