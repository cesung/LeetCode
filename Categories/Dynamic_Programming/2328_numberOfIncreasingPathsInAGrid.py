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

            if self.grid[nrow][ncol] >= self.grid[row][col]:
                continue
            
            self.dp[row][col] = (self.dp[row][col] + self.dfs(nrow, ncol)) % self.MOD
        
        return self.dp[row][col]


    def countPaths(self, grid: List[List[int]]) -> int:
        self.MOD = 10**9 + 7
        self.grid = grid
        # dp[row][col]: strictly increasing path ending in position (row, col)
        self.dp = defaultdict(lambda : defaultdict(int))
        self.num_rows, self.num_cols = len(grid), len(grid[0])
        self.directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1],
        ]

        ret = 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                ret = (ret + self.dfs(row, col)) % self.MOD
        
        return ret