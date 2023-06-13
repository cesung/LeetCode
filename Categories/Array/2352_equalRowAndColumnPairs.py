from typing import *
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        row_embedding_cntr = defaultdict(int)
        for row in grid:
            row_embedding_cntr[",".join(map(str, row))] += 1

        cnt = 0
        for col_idx in range(num_cols):
            col = []
            for row_idx in range(num_rows):
                col.append(grid[row_idx][col_idx])
            
            col_embedding = ",".join(map(str, col))
            if col_embedding in row_embedding_cntr:
                cnt += row_embedding_cntr[col_embedding]

        return cnt