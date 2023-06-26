from typing import *
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        
        pq = []
        for idx in range(n):
            if (
                idx < candidates or
                idx > n - 1 - candidates
            ):
                heapq.heappush(pq, 
                    (
                        costs[idx], 
                        idx,
                    )
                )

        left, right = candidates, n - 1 - candidates
        ret = 0
        while k > 0:
            cost, idx = heapq.heappop(pq)
            ret += cost
            k -= 1

            if left > right:
                continue

            heapq.heappush( 
                pq,
                (
                    costs[left] if idx < left else costs[right],
                    left if idx < left else right,
                )
            )

            if idx < left:
                left += 1
            else:
                right -= 1

        return ret