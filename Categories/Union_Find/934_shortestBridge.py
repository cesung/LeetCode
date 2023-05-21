from typing import *
from collections import deque
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parents = [idx for idx in range(size)]
        self.ranks = [1 for _ in range(size)]

    def find(self, n):
        root = n
        while root != self.parents[root]:
            root = self.parents[root]
        
        cur = n
        while cur != root:
            nxt = self.parents[cur]
            self.parents[cur] = root
            cur = nxt
        
        return root

    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)
        if r1 == r2:
            return
        
        if self.ranks[r1] > self.ranks[r2]:
            self.parents[r2] = r1
            self.ranks[r1] += self.ranks[r2]
        else:
            self.parents[r1] = r2
            self.ranks[r2] += self.ranks[r1]

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        size = len(grid)
        union_find = UnionFind(size * size)

        for row in range(size):
            for col in range(size):

                if grid[row][col] == 0:
                    continue
                
                if (
                    row != size - 1 and
                    grid[row + 1][col] == 1
                ):
                    union_find.union(
                        row * size + col,
                        (row + 1) * size + col,
                    )
                
                if (
                    col != size - 1 and
                    grid[row][col + 1] == 1
                ):
                    union_find.union(
                        row * size + col,
                        row * size + col + 1
                    )

        islands = defaultdict(list)
        for row in range(size):
            for col in range(size):
                if grid[row][col] == 0:
                    continue
                islands[union_find.find(row * size + col)].append( (row , col ))

        islands = list(islands.values())
        vis, island2 = set(islands[0]), set(islands[1])

        queue = deque(
            (row, col, 0)
            for row, col in islands[0]
        )

        directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1],
        ]

        while queue:
            row, col, step = queue.popleft()
            for drow, dcol in directions:
                nrow, ncol = row + drow, col + dcol

                if (
                    nrow < 0 or ncol < 0 or
                    nrow == size or ncol == size
                ):
                    continue
                
                if (nrow, ncol) in vis:
                    continue
                elif (nrow, ncol) in island2:
                    return step
                else:
                    vis.add( (nrow, ncol) )
                    queue.append( (nrow, ncol, step + 1) )   