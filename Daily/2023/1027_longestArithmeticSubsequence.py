from typing import *
from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for idx in range(n)]

        for idx in range(1, n):
            for jdx in range(idx):
                diff = nums[idx] - nums[jdx]
                dp[idx][diff] = dp[jdx][diff] + 1

        ret = -1
        for idx in range(n):
            ret = max(
                ret,
                max(dp[idx].values())
            )
        
        return ret + 1