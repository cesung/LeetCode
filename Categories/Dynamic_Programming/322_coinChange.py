from typing import *
import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = sys.maxsize
        dp = [INF for _ in range(amount + 1)]
        dp[0] = 0

        for amt in range(1, amount + 1):
            for deno in coins:
                if amt - deno >= 0:
                    dp[amt] = min(
                        dp[amt - deno] + 1,
                        dp[amt]
                    )
        
        return dp[-1] if dp[-1] != INF else -1