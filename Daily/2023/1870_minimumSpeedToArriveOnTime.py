from typing import *
import math

class Solution:
    def trySpeed(self, speed: int) -> bool:
        ttl = 0.0
        for dist in self.dists[:-1]:
            ttl += math.ceil(dist/speed)

        ttl += self.dists[-1]/speed

        return ttl <= self.hour

    def minSpeedOnTime(self, dists: List[int], hour: float) -> int:
        INT_MAX = 2147483647
        
        self.dists = dists
        self.hour = hour

        self.n = len(dists)
        if self.n > math.ceil(hour):
            return -1

        left, right = 1, INT_MAX
        while left < right:
            mid = (left + right) // 2
            if not self.trySpeed(mid):
                left = mid + 1
            else:
                right = mid

        return left