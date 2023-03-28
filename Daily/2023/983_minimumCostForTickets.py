from typing import *

class Solution:
    def bs(self, target):
        left, right = 0, self.size - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.days[mid] <= target:
                left = mid + 1
            else:
                right = mid
    
        return left

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.size = len(days)
        self.days = days
        dp = defaultdict(int)

        for idx, day in enumerate(days):
            dp[idx + 1] = min(
                dp[idx] + costs[0], # dp[self.bs(day - 1)] + costs[0],
                dp[self.bs(day - 7)] + costs[1],
                dp[self.bs(day - 30)] + costs[2]
            ) 
        
        return dp[self.size]