from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        size = len(grid)
        queue = deque()
        
        for row in range(size):
            for col in range(size):
                if grid[row][col] == 1:
                    queue.append([row, col])
        
        if not queue or len(queue) == size*size:
            return -1
        
        directions = [
            [+1, 0],
            [-1, 0],
            [0, +1],
            [0, -1],
        ]
        
        max_dist = -1
        while queue:
            row, col = queue.popleft()
            for drow, dcol in directions:
                nrow, ncol = row + drow, col + dcol
                if (
                    nrow < 0 or nrow == size or
                    ncol < 0 or ncol == size or
                    grid[nrow][ncol] != 0
                ):
                    continue
        
                grid[nrow][ncol] = grid[row][col] + 1
                max_dist = grid[nrow][ncol]
                queue.append( [nrow, ncol] )
        
        return max_dist - 1
