from typing import *

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def dfs(self, size, row, col):
        suc = True
        for idx in range(size):
            for jdx in range(size):
                if self.grid[row][col] != self.grid[row + idx][col + jdx]:
                    suc = False
                    break
            if not suc:
                break
        
        if suc:
            return Node(self.grid[row][col], True, None, None, None, None)
        
        size //= 2
        top_left = self.dfs(size, row, col)
        top_right = self.dfs(size, row, col + size)
        bot_left = self.dfs(size, row + size, col)
        bot_right = self.dfs(size, row + size, col + size)
        return Node(1, False, top_left, top_right, bot_left, bot_right)

    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid
        size = len(grid)
        return self.dfs(size, 0, 0)