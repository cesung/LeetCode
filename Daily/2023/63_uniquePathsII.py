from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, row: int, col: int) -> int:
        # invalid cell
        if (
            row < 0 or
            col < 0
        ):
            return 0
        
        # obstacle
        if self.obstacleGrid[row][col] == 1:
            return 0
        
        # seen
        if (row, col) in self.dp:
            return self.dp[ (row, col) ]
        
        for drow, dcol in self.directions:
            nrow, ncol = row + drow, col + dcol
            self.dp[ (row, col) ] += self.dfs(nrow, ncol)
        
        return self.dp[ (row, col) ]
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # m * n matrix
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        self.obstacleGrid = obstacleGrid
        self.dp = defaultdict(int, {
            (0, 0) : 1
        })
        self.directions = [
            [-1, 0],
            [0, -1],
        ]
        
        return self.dfs(m - 1, n - 1)