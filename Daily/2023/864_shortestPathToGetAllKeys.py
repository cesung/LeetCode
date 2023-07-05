from typing import *
from collections import defaultdict, deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        all_keys_state = 0
        start_row, start_col = -1, -1
        for row in range(num_rows):
            for col in range(num_cols):
                # key
                if grid[row][col].islower():
                    all_keys_state |= (1 << (ord(grid[row][col]) - ord('a')))
                if grid[row][col] == '@':
                    start_row, start_col = row, col
        
        directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1],
        ]

        vis = defaultdict(set)
        queue = deque([ (start_row, start_col, 0, 0) ])
        while queue:
            row, col, keys_state, dist = queue.popleft()

            for drow, dcol in directions:
                nrow, ncol = row + drow, col + dcol

                # invalid visit
                if (
                    nrow < 0 or nrow >= num_rows or
                    ncol < 0 or ncol >= num_cols or
                    grid[nrow][ncol] == '#' or
                    keys_state in vis[(nrow, ncol)]
                ):
                    continue
            
                # lock
                if grid[nrow][ncol].isupper():
                    # key is not obtained, invalid visit
                    if keys_state & (1 << (ord(grid[nrow][ncol]) - ord('A'))) == 0:
                        continue

                    # key is obtained
                    else:
                        vis[(nrow, ncol)].add(keys_state)
                        queue.append( (nrow, ncol, keys_state, dist + 1))

                # key
                elif grid[nrow][ncol].islower():
                    keys_state |= (1 << (ord(grid[nrow][ncol]) - ord('a')))
                    if keys_state == all_keys_state:
                        return dist + 1
            
                    vis[(nrow, ncol)].add(keys_state)
                    queue.append( (nrow, ncol, keys_state, dist + 1) )
                
                # '.' or '@'
                else:
                    vis[(nrow, ncol)].add(keys_state)
                    queue.append( (nrow, ncol, keys_state, dist + 1) )
        
        return -1