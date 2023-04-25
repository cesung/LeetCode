from typing import *
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.pq = [1]
        self.vis = set(self.pq)
        self.label = 1

    def popSmallest(self) -> int:
        # remove smallest value
        min_num = heapq.heappop(self.pq)
        self.vis.remove(min_num)

        # add min_num + 1 if happen to remove the num with label
        if min_num == self.label:
            self.label += 1
            self.vis.add(min_num + 1)
            heapq.heappush(self.pq, min_num + 1)
            
        return min_num

    def addBack(self, num: int) -> None:
        if (
            num in self.vis or
            num >= self.label
        ):
            return

        self.vis.add(num)
        heapq.heappush(self.pq, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)