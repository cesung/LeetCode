from typing import *
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-1 * stone for stone in stones]
        heapq.heapify(pq)

        while len(pq) > 1:
            # stone1 >= stone2
            stone1, stone2 = -1 * heapq.heappop(pq), -1 * heapq.heappop(pq)
            
            if stone1 == stone2:
                continue
            else:
                heapq.heappush(pq, -1 * (stone1 - stone2))
        
        return 0 if not pq else -1 * pq[0]

