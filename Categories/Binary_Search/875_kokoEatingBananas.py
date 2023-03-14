import math
from typing import *

class Solution:
    def get_hours(self, k):
        num_hours = 0
        for pile in self.piles:
            num_hours += math.ceil(pile / k)

        return num_hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles

        left, right = 1, 10**9 * 10**4
        while left < right:
            mid = left + (right - left) // 2
            if self.get_hours(mid) > h:
                left = mid + 1
            else:
                right = mid
        
        return left