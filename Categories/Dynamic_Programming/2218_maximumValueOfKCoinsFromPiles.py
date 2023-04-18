from typing import *

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        size = len(piles)

        prefix_piles = []
        for idx in range(size):
            prefix_piles.append([0])
            for jdx in range(len(piles[idx])):
                prefix_piles[idx].append(prefix_piles[idx][-1] + piles[idx][jdx])

        rcd = [[0 for _ in range(k + 1)] for _ in range(size)]
        for jdx in range(min(k, len(piles[0]))):
            rcd[0][jdx + 1] = prefix_piles[0][jdx + 1]

        for idx in range(1, size):
            for jdx in range(k + 1):
                for kdx in range(min(jdx, len(piles[idx])) + 1):
                    rcd[idx][jdx] = max(
                        rcd[idx][jdx],
                        rcd[idx - 1][jdx - kdx] + prefix_piles[idx][kdx]
                    )
                    
        return rcd[-1][k]