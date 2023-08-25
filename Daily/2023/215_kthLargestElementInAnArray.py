from typing import *
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = [-num for num in nums] 
        heapq.heapify(pq)
        ret = -1
        while k:
            ret = heapq.heappop(pq)
            k -= 1
        
        return -1 * ret