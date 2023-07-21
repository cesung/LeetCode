from typing import *
import math

class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        size = len(s)
        num_letter_in_sec = num_rows * 2 - 2
        num_secs = math.ceil(size / num_letter_in_sec)
        num_cols = num_secs * (num_rows - 1)

        matrix = [["" for _ in range(num_cols)] for _ in range(num_rows)]

        row, col, idx = 0, 0, 0
        while idx < size:
            while idx < size and row < num_rows:
                matrix[row][col] = s[idx]
                idx += 1
                row += 1

            row -= 2
            col += 1

            while idx < size and row > 0:
                matrix[row][col] = s[idx]
                idx += 1
                row -= 1
                col += 1
        
        ret = []
        for row in range(num_rows):
            for col in range(num_cols):
                if matrix[row][col] != "":
                    ret.append(matrix[row][col])

        return "".join(ret) 
