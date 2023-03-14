from collections import defaultdict

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num_rows, num_cols = len(strs), len(strs[0])
        cols = defaultdict(list)

        for row in range(num_rows):
            for col in range(num_cols):
                cols[col].append(strs[row][col])
            
        cnt = 0
        for col_idx in cols:
            col = "".join(cols[col_idx])
            col_asc = "".join(sorted(col[:]))
            if col == col_asc:
                continue
            cnt += 1
        
        return cnt
