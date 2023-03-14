from collections import deque

class Solution:
    def get_row_col(self, label):
        label -= 1
        q, r = label // self.size, label % self.size
        row, col = self.size - 1 - q, r if q % 2 == 0 else self.size - 1 - r

        return row, col
    
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self.size = len(board)

        vis = set()
        vis.add(1)

        queue = deque()
        queue.append( (1, 0) )

        while queue:
            cur_label, step = queue.popleft()

            if cur_label == self.size ** 2:
                return step

            for nxt_label in range(cur_label + 1, min(cur_label + 6, self.size ** 2) + 1):
                if nxt_label in vis:
                    continue

                vis.add(nxt_label)

                row, col = self.get_row_col(nxt_label)
                if board[row][col] != -1:
                    nxt_label = board[row][col]
                queue.append( (nxt_label, step + 1) )
        
        return -1
