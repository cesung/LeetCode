from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, row: int, col: int) -> int:
        if self.dp[row][col] != 0:
            return self.dp[row][col]

        self.dp[row][col] = 1
        for direction in self.directions:
            drow, dcol = direction
            nrow, ncol = row + drow, col + dcol
            if (
                nrow < 0 or nrow >= self.num_rows or
                ncol < 0 or ncol >= self.num_cols
            ):
                continue
            if self.matrix[nrow][ncol] >= self.matrix[row][col]:
                continue
            
            self.dp[row][col] = max(
                self.dp[row][col],
                self.dfs(nrow, ncol) + 1,
            )
        
        return self.dp[row][col]
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dp[row][col] stricktly increasing path ending at position (row, col)
        self.matrix = matrix
        self.num_rows, self.num_cols = len(matrix), len(matrix[0])
        self.dp = defaultdict(lambda : defaultdict(int))
        self.directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1],
        ]

        ret = 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                ret = max(
                    ret,
                    self.dfs(row, col)
                )
        
        return ret
                