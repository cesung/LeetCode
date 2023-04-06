from typing import *

class Solution:
    def dfs(self, row, col):
        if (row, col) in self.vis:
            return True
        
        # boundary
        if (
            row == 0 or row == self.num_rows - 1 or
            col == 0 or col == self.num_cols - 1
        ):
            return False
        
        self.vis.add( (row, col) )
        suc = True
        for drow, dcol in self.directions:
            nrow, ncol = row + drow, col + dcol
            # out of boundary
            if (
                nrow < 0 or nrow >= self.num_rows or
                ncol < 0 or ncol >= self.num_cols
            ):
                continue

            if self.grid[nrow][ncol] == 1:
                continue
            
            suc &= self.dfs(nrow, ncol)
        
        return suc
            
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.num_rows, self.num_cols = len(grid), len(grid[0])
        self.grid = grid
        self.directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1],
        ]

        self.vis = set()
        cnt = 0

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if (
                    (row, col) not in self.vis and
                    grid[row][col] == 0
                ):
                    cnt += 1 if self.dfs(row, col) else 0

        return cnt