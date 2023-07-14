from typing import *
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        rcd = defaultdict(int)

        rcd[arr[0]] = 1
        for idx in range(1, n):
            if arr[idx] - difference in rcd:
                rcd[arr[idx]] = rcd[arr[idx] - difference] + 1
            else:
                rcd[arr[idx]] = 1

        return max(rcd.values())
