from typing import *
from collections import defaultdict

class Solution:
    def rob_198(self, nums):
        size = len(nums)
        nums = [-1] + nums

        dp = defaultdict(lambda : defaultdict(int))
        dp[0][0] = dp[0][1] = 0

        for idx in range(1, size + 1):
            dp[idx][0] = max(
                dp[idx - 1][0],
                dp[idx - 1][1]
            )
            dp[idx][1] = dp[idx - 1][0] + nums[idx]

        return max(dp[size].values())

    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]

        return max(
            self.rob_198(nums[1:]),
            self.rob_198(nums[:-1])
        )