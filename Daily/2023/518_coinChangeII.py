from typing import *

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # dp[idx][jdx]: the number of combinations that make up jdx amount with first idx coins
        dp = [[0 for _ in range(amount + 1)] for _ in range(n)]
        
        for idx in range(n):
            dp[idx][0] = 1
        
        for idx in range(n):
            for jdx in range(1, amount + 1):
                dp[idx][jdx] += (
                    (dp[idx][jdx - coins[idx]] if jdx - coins[idx] >= 0 else 0) +
                    dp[idx - 1][jdx]
                )
                
        return dp[n - 1][-1]
        