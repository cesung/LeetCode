from typing import *


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True
        
        x0, y0, x1, y1 = (
            coordinates[0][0], 
            coordinates[0][1], 
            coordinates[1][0], 
            coordinates[1][1],
        )

        # vertical line
        if all([coordinates[x_idx][0] == x0 for x_idx in range(1, n)]):
            return True

        # exception: divide by 0
        if x1 - x0 == 0:
            return False
        slope = (y1 - y0) / (x1 - x0)

        for idx in range(2, n):
            x_prev, y_prev, x_cur, y_cur = (
                coordinates[idx - 1][0],
                coordinates[idx - 1][1],
                coordinates[idx][0],
                coordinates[idx][1],
            )
            
            # exception: divide by 0
            if x_cur - x_prev == 0:
                return False
            if slope != (y_cur - y_prev) / (x_cur - x_prev):
                return False
        
        return True
