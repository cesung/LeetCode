from typing import *

class Solution:
    def get_days(self, max_load):
        cur_load = num_days = 0
        for idx in range(self.size):
            if cur_load + self.weights[idx] > max_load:
                num_days += 1
                cur_load = 0
            cur_load += self.weights[idx]
        
        return num_days + 1

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights = weights
        self.size = len(self.weights)
        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            if self.get_days(mid) > days:
                left = mid + 1
            else:
                right = mid
        
        return left