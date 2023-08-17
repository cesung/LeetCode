import sys
from typing import *

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        INF = sys.maxsize
        num_rows, num_cols = len(mat), len(mat[0])
        dist_mat = [[INF for _ in range(num_cols)] for _ in range(num_rows)]

        for row in range(num_rows):
            for col in range(num_cols):
                if mat[row][col] == 0:
                    dist_mat[row][col] = 0
                else:
                    if row - 1 >= 0:
                        dist_mat[row][col] = min(
                            dist_mat[row][col],
                            dist_mat[row - 1][col] + 1
                        )
                    if col - 1 >= 0:
                        dist_mat[row][col] = min(
                            dist_mat[row][col],
                            dist_mat[row][col - 1] + 1
                        )
        for row in range(num_rows - 1, -1, -1): 
            for col in range(num_cols - 1, -1, -1):
                if row + 1 < num_rows:
                    dist_mat[row][col] = min(
                        dist_mat[row][col],
                        dist_mat[row + 1][col] + 1,
                    )
                if col + 1 < num_cols:
                    dist_mat[row][col] = min(
                        dist_mat[row][col],
                        dist_mat[row][col + 1] + 1,
                    )
        
        return dist_mat