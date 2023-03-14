from typing import *
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rcd = defaultdict(int, {
            0 : 1
        })

        cur, ret = 0, 0
        for num in nums:
            cur += num
            ret += rcd[cur - k]
            rcd[cur] += 1

        return ret