class Solution:

    def dfs(self, row, col):
        if (
            row < 0 or row >= self.num_rows or
            col < 0 or col >= self.num_cols or
            self.land[row][col] == 0 or
            (row, col) in self.vis
        ):
            return

        self.vis.add( (row, col) )
        self.dest_row = max(self.dest_row, row)
        self.dest_col = max(self.dest_col, col)

        for drow, dcol in self.directions:
            nrow, ncol = row + drow, col + dcol
            self.dfs(nrow, ncol)


    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        self.land = land
        self.vis = set()
        self.directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1],
        ]
        self.ret = []

        self.num_rows, self.num_cols = len(land), len(land[0])
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if (
                    land[row][col] == 1 and
                    (row, col) not in self.vis
                ):
                    self.dest_row, self.dest_col = -1, -1
                    self.dfs(row, col)
                    self.ret.append( (row, col, self.dest_row, self.dest_col))

        return self.ret
