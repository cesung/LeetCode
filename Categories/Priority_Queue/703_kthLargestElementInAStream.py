from typing import *
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.size = 0
        self.k = k
        for num in nums:
            heapq.heappush(self.min_heap, num)
            self.size += 1
            if self.size == self.k + 1:
                self.size -= 1
                heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        self.size += 1
        heapq.heappush(self.min_heap, val)

        if self.size == self.k + 1:
            self.size -= 1
            heapq.heappop(self.min_heap)

        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
