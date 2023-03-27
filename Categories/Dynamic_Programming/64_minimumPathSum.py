from typing import *

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        length, width = len(grid), len(grid[0])
        dp = [[0 for _ in range(width)] for _ in range(length)]
        dp[0][0] = grid[0][0]
        for jdx in range(1, width):
            dp[0][jdx] = dp[0][jdx - 1] + grid[0][jdx]

        for idx in range(1, length):
            dp[idx][0] = dp[idx - 1][0] + grid[idx][0]
        
        for idx in range(1, length):
            for jdx in range(1, width):
                dp[idx][jdx] = min(
                    dp[idx - 1][jdx],
                    dp[idx][jdx - 1]
                ) + grid[idx][jdx]
        
        return dp[-1][-1]