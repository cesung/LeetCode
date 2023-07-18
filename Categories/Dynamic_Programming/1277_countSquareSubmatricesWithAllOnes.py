from typing import *


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        ret = 0
        for idx in range(m):
            ret += matrix[idx][0]
            dp[idx][0] = matrix[idx][0]
        for jdx in range(1, n):
            ret += matrix[0][jdx]
            dp[0][jdx] = matrix[0][jdx]
        
        for idx in range(1, m):
            for jdx in range(1, n):
                if matrix[idx][jdx] == 0:
                    continue

                dp[idx][jdx] = min(
                    dp[idx - 1][jdx],
                    dp[idx][jdx - 1],
                    dp[idx - 1][jdx - 1],
                ) + 1

                ret += dp[idx][jdx]

        return ret