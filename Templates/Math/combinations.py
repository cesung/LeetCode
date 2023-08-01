from typing import *

class Solution:
    def dfs(self, idx: int, cnt: int, comb: List[int]) -> None:
        if cnt == self.k:
            self.combs.append(comb[:])
            return
        
        for jdx in range(idx, self.n + 1):
            self.dfs(jdx + 1, cnt + 1, comb + [jdx])

    def combinations(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.k = k
        self.combs = []
        
        self.dfs(1, 0, [])

        return self.combs