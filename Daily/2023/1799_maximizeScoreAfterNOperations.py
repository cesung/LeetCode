from typing import *
from collections import defaultdict


class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b

        return abs(a)

    def dfs(self, mask, op):
        if mask in self.dp:
            return self.dp[mask]

        for idx in range(self.size):
            if (1 << idx) & mask:
                continue
            for jdx in range(idx + 1, self.size):
                if (1 << jdx) & mask:
                    continue
                new_mask = mask | (1 << idx) | (1 << jdx)
                self.dp[mask] = max(
                    self.dp[mask],
                    op * self.gcd(self.nums[idx], self.nums[jdx]
                                  ) + self.dfs(new_mask, op + 1)
                )

        return self.dp[mask]

    def maxScore(self, nums: List[int]) -> int:
        self.size = len(nums)
        self.nums = nums
        self.dp = defaultdict(int)

        return self.dfs(0, 1)
