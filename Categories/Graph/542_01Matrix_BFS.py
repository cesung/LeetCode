import sys
from typing import *
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        INF = sys.maxsize
        num_rows, num_cols = len(mat), len(mat[0])
        dist_mat = [[INF for _ in range(num_cols)] for _ in range(num_rows)]
        directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1],
        ]

        queue = deque()
        for row in range(num_rows):
            for col in range(num_cols):
                if mat[row][col] == 0:
                    dist_mat[row][col] = 0
                    queue.append( (row, col) )
            
        while queue:
            row, col = queue.popleft()
            for drow, dcol in directions:
                nrow, ncol = row + drow, col + dcol
                if (
                    nrow < 0 or nrow >= num_rows or
                    ncol < 0 or ncol >= num_cols or
                    dist_mat[nrow][ncol] != INF
                ):
                    continue

                dist_mat[nrow][ncol] = dist_mat[row][col] + 1
                queue.append( (nrow, ncol) )
        
        return dist_mat