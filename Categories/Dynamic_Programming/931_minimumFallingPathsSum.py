from typing import *

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        INF = 10**6 + 5
        size = len(matrix)
        
        dp = defaultdict(lambda : defaultdict(lambda : 10**6+5))

        for col in range(size):
            dp[0][col] = matrix[0][col]

        for row in range(1, size):
            for col in range(size):
                if col - 1 >= 0:
                    dp[row][col] = min(
                        dp[row][col],
                        dp[row - 1][col - 1],
                    )
                dp[row][col] = min(
                    dp[row][col],
                    dp[row - 1][col],
                )
                if col + 1 < size:
                    dp[row][col] = min(
                        dp[row][col],
                        dp[row - 1][col + 1],
                    )
                dp[row][col] += matrix[row][col]

        return min(dp[size - 1].values())