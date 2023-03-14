from typing import *

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        # 0 -> even, 1 -> odd
        rcd = [0 for _ in range(2)]
        rcd[0] += 1

        cur, ret = 0, 0
        for num in arr:
            cur += num
            if cur % 2 == 0:
                ret = (ret + rcd[1]) % MOD
            else:
                ret = (ret + rcd[0]) % MOD
            rcd[cur % 2] += 1

        return ret