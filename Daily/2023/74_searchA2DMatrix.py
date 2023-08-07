from typing import *

class Solution:
    # find larger or equal
    def bs_find_row(self, size: int, matrix: List[List[int]], target: int) -> int:
        left, right = 0, size - 1
        while left < right:
            mid = (left + right) // 2
            if matrix[mid][-1] < target:
                left = mid + 1
            else:
                right = mid
        
        if matrix[left][-1] < target:
            return -1

        return left

    # find larger or equal
    def bs_find_col(self, row: int, size: int, matrix: List[List[int]], target: int) -> int:
        left, right = 0, size - 1
        while left < right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # m : number of rows
        m = len(matrix)
        # n : number of cols
        n = len(matrix[0])

        # find row
        row = self.bs_find_row(m, matrix, target)
        if row == -1:
            return False
        
        # find col
        col = self.bs_find_col(row, n, matrix, target)
        return True if matrix[row][col] == target else False