from typing import *


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        INF = float('inf')

        size = len(arr)
        # dp[idx] largest sum of the given array after partitioning until index idx
        dp = [0 for _ in range(size)]

        maxv = -INF
        for idx in range(k):
            maxv = max(
                maxv,
                arr[idx]
            )

            dp[idx] = maxv * (idx + 1)

        for idx in range(k, size):
            maxv = -INF
            for jdx in range(k):
                maxv = max(
                    maxv,
                    arr[idx - jdx],
                )
                dp[idx] = max(
                    dp[idx],
                    dp[idx - jdx - 1] + (jdx + 1) * maxv
                )

        return dp[-1]
