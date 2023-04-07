from typing import *

class Solution:

    def dfs(self, row, col):
        if (
            row < 0 or row >= self.num_rows or
            col < 0 or col >= self.num_cols or
            self.grid[row][col] == 0 or
            (row, col) in self.vis
        ):
            return 0
        
        ret = 1
        self.vis.add( (row, col) )
        for drow, dcol in self.directions:
            nrow, ncol = row + drow, col + dcol
            ret += self.dfs(nrow, ncol)
        
        return ret

    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.num_rows, self.num_cols = len(grid), len(grid[0])
        self.grid = grid
        self.directions = [
            [+1, 0],
            [0, +1],
            [0, -1],
            [-1, 0]
        ]
        self.vis = set()

        land = 0; border_land = 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                land += grid[row][col]
                border_land += self.dfs(row, col) if (
                    grid[row][col] == 1 and
                    (row, col) not in self.vis and
                    (
                        row in [0, self.num_rows - 1] or
                        col in [0, self.num_cols - 1]
                    )
                ) else 0

        return land - border_land