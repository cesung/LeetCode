from typing import *

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        self.n = n
        self.batteries = batteries

        left, right = 0, 10**9 * 10**5 + 1

        while left < right:
            mid = (left + right) // 2 + 1
            if self.tryRun(mid) == False:
                right = mid - 1
            else:
                left = mid
        
        return left

    def tryRun(self, time):
        return True if sum([
            min(time, battery)
            for battery in self.batteries
        ]) >= self.n * time else False