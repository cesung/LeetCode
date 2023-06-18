from typing import *
import sys

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        num_rows, num_cols = len(mat), len(mat[0])
        # dp[row][col]: how many number of valid submatrices ending at cololumn `col` in the row `row`
        dp = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

        for row in range(num_rows):
            cnt = 0
            for col in range(num_cols):
                cnt = (cnt + 1) if mat[row][col] == 1 else 0
                dp[row][col] = cnt
        
        ret = 0
        for row in range(num_rows):
            for col in range(num_cols):
                cnt = sys.maxsize
                for _row in range(row, num_rows):
                    cnt = min(
                        cnt,
                        dp[_row][col],
                    )
                
                    ret += cnt
        
        return ret