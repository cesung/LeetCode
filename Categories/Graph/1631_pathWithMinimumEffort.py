from typing import *

class Solution:
    def hikeWithEffort(self, row: int, col: int, effort:int, vis: set) -> bool:
        
        if (
            row == self.num_rows - 1 and
            col == self.num_cols - 1
        ):
            return True
        
        for drow, dcol in self.directions:
            nrow, ncol = row + drow, col + dcol

            # invalid cell
            if (
                nrow < 0 or
                nrow >= self.num_rows or
                ncol < 0 or
                ncol >= self.num_cols
            ):
                continue
            
            if (nrow, ncol) in vis:
                continue
            vis.add( (row, col) )

            # > effort limit
            if abs(self.heights[row][col] - self.heights[nrow][ncol]) > effort:
                continue
            
            if self.hikeWithEffort(nrow, ncol, effort, vis):
                return True
        
        return False

    
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.num_rows, self.num_cols = len(heights), len(heights[0])
        self.heights = heights
        self.directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1],
        ]

        left, right = 0, 10**6 + 1
        while left < right:
            mid = left + (right - left) // 2
            vis = set([0, 0])
            if self.hikeWithEffort(0, 0, mid, vis):
                right = mid
            else:
                left = mid + 1
        
        return left