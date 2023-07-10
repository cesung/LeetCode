from typing import *
import heapq

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)

        rcd = []
        for idx in range(n - 1):
            rcd.append(weights[idx] + weights[idx + 1])
        
        m = len(rcd)

        min_heap = []
        for idx in range(m):
            heapq.heappush(min_heap, -1 * rcd[idx])

            if len(min_heap) > k - 1:
                heapq.heappop(min_heap)

        max_heap = []
        for idx in range(m):
            heapq.heappush(max_heap, rcd[idx])

            if len(max_heap) > k - 1:
                heapq.heappop(max_heap)

        return sum(max_heap) - (-1 * sum(min_heap))