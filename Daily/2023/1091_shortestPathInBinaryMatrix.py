from typing import *
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if (
            grid[0][0] == 1 or
            grid[n - 1][n - 1] == 1
        ):
            return -1

        grid[n - 1][n - 1] = 1
        queue = deque([(n - 1, n - 1, 1)])
        directions = [
            [-1, -1],
            [-1, 0],
            [-1, +1],
            [0, -1],
            [0, +1],
            [+1, -1],
            [+1, 0],
            [+1, +1]
        ]

        while queue:
            row, col, step = queue.popleft()

            if row == 0 == col:
                return step

            for drow, dcol in directions:
                nrow, ncol = row + drow, col + dcol
                if (
                    nrow < 0 or nrow == n or
                    ncol < 0 or ncol == n or
                    grid[nrow][ncol] == 1
                ):
                    continue
                grid[nrow][ncol] = 1
                queue.append((nrow, ncol, step + 1))

        return -1
