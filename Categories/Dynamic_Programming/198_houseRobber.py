from typing import *
from collections import defaultdict

class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        nums = [-1] + nums

        # dp[house #][0:don't rob, 1:rob]
        dp = defaultdict(lambda : defaultdict(int))
        dp[0][0] = dp[0][1] = 0

        for idx in range(1, size + 1):
            dp[idx][1] = dp[idx - 1][0] + nums[idx]
            dp[idx][0] = max(
                dp[idx - 1][0],
                dp[idx - 1][1],
            )
        
        return max(dp[size].values())