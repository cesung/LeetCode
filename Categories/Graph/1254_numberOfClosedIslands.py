from typing import *

class Solution:
    def dfs(self, row, col):
        if (
            row < 0 or row == self.num_rows or
            col < 0 or col == self.num_cols
        ): 
            return False
        
        if (
            self.grid[row][col] == 1 or
            (row, col) in self.vis
        ):
            return True

        self.vis.add( (row, col) )

        suc = True
        for drow, dcol in self.directions:
            nrow, ncol = row + drow, col + dcol
    
            suc &= self.dfs(nrow, ncol)
        
        return suc
            
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.num_rows, self.num_cols = len(grid), len(grid[0])
        self.grid = grid
        self.directions = [
            [0, +1],
            [+1, 0],
            [0, -1],
            [-1, 0],
        ]
        self.vis = set()

        cnt = 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if (
                    grid[row][col] == 0 and
                    (row, col) not in self.vis
                ):
                    cnt += 1 if self.dfs(row, col) else 0 
        
        return cnt