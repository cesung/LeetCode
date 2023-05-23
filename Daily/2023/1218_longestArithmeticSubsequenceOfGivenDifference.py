from typing import *


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        size = len(arr)

        # the lastest index that number arr[idx] shows up
        rcd = defaultdict(int, {
            arr[0]: 0
        })

        dp = [1 for _ in range(size)]

        for idx, num in enumerate(arr[1:], 1):
            if num - difference in rcd:
                dp[idx] = dp[rcd[num - difference]] + 1
            rcd[num] = idx

        return max(dp)
