from typing import *

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        jdx, cnt = n - 1, 0
        for idx in range(0, m):
            while jdx >= 0 and grid[idx][jdx] < 0:
                cnt += (m - idx)
                jdx -= 1
            
            
        return cnt