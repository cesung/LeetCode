class Solution:

    def get_val(self, row, col):
        return self.INF if (
            row < 0 or row >= self.num_rows or
            col < 0 or col >= self.num_cols 
        ) else self.img[row][col]

    def get_avg(self, row, col):
        directions = [
            [-1, -1],
            [-1, 0],
            [-1, +1],
            [0, -1],
            [0, 0],
            [0, +1],
            [+1, -1],
            [+1, 0],
            [+1, +1],
        ]

        ttl, cnt = 0, 0
        for drow, dcol in directions:
            nrow, ncol = row + drow, col + dcol
            val = self.get_val(nrow, ncol)
            if val == self.INF:
                continue
            ttl += val
            cnt += 1
    
        return ttl // cnt

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        self.img = img
        self.INF = float('inf')
        self.num_rows, self.num_cols = len(img), len(img[0])
        ret = [[-1 for _ in range(self.num_cols)] for _ in range(self.num_rows)]

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                ret[row][col] = self.get_avg(row, col)
        
        return ret
