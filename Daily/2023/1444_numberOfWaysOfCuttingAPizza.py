from typing import *

class Solution:
    def has_apple(self, row1: int, col1: int, row2: int, col2: int) -> bool:
        return (
            self.num_apples[row2][col2]
            - (self.num_apples[row2][col1 - 1] if col1 - 1 >= 0 else 0)
            - (self.num_apples[row1 - 1][col2] if row1 - 1 >= 0 else 0)
            + (self.num_apples[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0)
        ) > 0

    def dfs(self, row: int, col: int, k: int) -> int:
        if k == 0:
            return 1 if self.has_apple(row, col, self.num_rows - 1, self.num_cols - 1) else 0
        
        if (row, col, k) in self.rcd:
            return self.rcd[(row, col, k)]
        
        self.rcd[(row, col, k)] = 0
        for r in range(row + 1, self.num_rows):
            if not self.has_apple(row, col, r - 1, self.num_cols - 1):
                continue

            self.rcd[(row, col, k)] = (
                self.rcd[(row, col, k)] + 
                self.dfs(r, col, k - 1)
            ) % self.MOD

        for c in range(col + 1, self.num_cols):
            if not self.has_apple(row, col, self.num_rows - 1, c - 1):
                continue
            
            self.rcd[(row, col, k)] = (
                self.rcd[(row, col, k)] + 
                self.dfs(row, c, k - 1)
            ) % self.MOD
             
        return self.rcd[(row, col, k)]


    def ways(self, pizza: List[str], k: int) -> int:
        self.num_rows, self.num_cols = len(pizza), len(pizza[0])
        self.num_apples = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        self.num_apples[0][0] = int(pizza[0][0] == 'A')

        for row in range(1, self.num_rows):
            self.num_apples[row][0] = (
                self.num_apples[row - 1][0] + 
                int(pizza[row][0] == 'A')
            )
        
        for col in range(1, self.num_cols):
            self.num_apples[0][col] = (
                self.num_apples[0][col - 1] + 
                int(pizza[0][col] == 'A')
            )
        
        for row in range(1, self.num_rows):
            for col in range(1, self.num_cols):
                self.num_apples[row][col] = (
                    self.num_apples[row - 1][col]
                    + self.num_apples[row][col - 1]
                    - self.num_apples[row - 1][col - 1]
                ) + int(pizza[row][col] == 'A')

        self.MOD = 10**9 + 7
        self.rcd = defaultdict(int)
        return self.dfs(0, 0, k - 1)