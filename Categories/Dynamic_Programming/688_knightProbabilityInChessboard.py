from typing import *

class Solution:
    def knightProbability(self, n: int, k: int, st_row: int, st_col: int) -> float:
        dirs = [
            [+2, +1],
            [+2, -1],
            [+1, +2],
            [+1, -2],
            [-1, +2],
            [-1, -2],
            [-2, +1],
            [-2, -1],
        ]

        dp_prev = [[0 for _ in range(n)] for _ in range(n)]   
        # step 0
        dp_prev[st_row][st_col] = 1.0

        # k steps
        for _ in range(k):
            dp_cur = [[0 for _ in range(n)] for _ in range(n)]

            for row in range(n):
                for col in range(n):
                    for drow, dcol in dirs:
                        nrow, ncol = row + drow, col + dcol
                        if (
                            nrow < 0 or nrow >= n or
                            ncol < 0 or ncol >= n
                        ):
                            continue
                        dp_cur[nrow][ncol] += dp_prev[row][col] * 1/8
            
            dp_prev = dp_cur

        ret = 0.0
        for row in range(n):
            for col in range(n):
                ret += dp_prev[row][col]
        
        return ret