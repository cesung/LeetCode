from typing import *

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capitals: List[int]) -> int:
        size = len(profits)
        pq = []

        pairs = [
            (capital, profit)
            for capital, profit in zip(capitals, profits)
        ]
        pairs.sort(key = lambda x: x[0])

        cur_idx = 0
        for idx in range(size):
            if pairs[idx][0] > w:
                break
            cur_idx = idx
            heapq.heappush(pq, -1 * pairs[idx][1])

        ttl_profit = w
        while k and pq:
            max_profit = heapq.heappop(pq) * -1
            ttl_profit += max_profit
            for idx in range(cur_idx + 1, size):
                if pairs[idx][0] > ttl_profit:
                    break
                cur_idx = idx
                heapq.heappush(pq, -1 * pairs[idx][1])
            k -= 1
        
        return ttl_profit