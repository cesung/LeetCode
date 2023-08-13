from typing import *

class Solution:
    def dfs(self, maze: List[List[int]], row: int, col: int):
        if (
            row == self.tar_row and
            col == self.tar_col
        ):
            return True
        
        for drow, dcol in self.directions:
            nrow, ncol = row, col
            while (
                nrow >= 0 and
                nrow < self.num_rows and
                ncol >= 0 and
                ncol < self.num_cols and
                maze[nrow][ncol] == 0
            ):
                nrow += drow
                ncol += dcol
            nrow -= drow
            ncol -= dcol
            
            if (nrow, ncol) in self.vis:
                continue
            self.vis.add( (nrow, ncol) )
            
            if self.dfs(maze, nrow, ncol):
                return True
            
        return False
    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        self.num_rows, self.num_cols = len(maze), len(maze[0])
        self.tar_row, self.tar_col = destination[0], destination[1]
        self.vis = set()
        self.directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1],
        ]
        return self.dfs(maze, start[0], start[1])