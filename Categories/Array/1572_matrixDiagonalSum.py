from typing import *

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat)
        ttl = 0

        for idx in range(size):
            ttl += mat[idx][idx]
        
        for idx in range(size):
            ttl += mat[idx][size - 1 - idx]

        if size % 2 != 0:
            ttl -= mat[size // 2][size // 2]
        
        return ttl