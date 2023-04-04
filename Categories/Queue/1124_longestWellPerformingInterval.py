from typing import *

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        size = len(hours)
        tiring = [
            1 if hour > 8 else -1
            for hour in hours
        ]

        rcd = defaultdict(int)

        ret = 0
        cur = 0
        for idx in range(size):
            cur += tiring[idx]

            if cur > 0:
                ret = idx + 1

            if cur - 1 in rcd:
                ret = max(
                    ret,
                    idx - rcd[cur - 1]
                )
            
            if cur not in rcd:
                rcd[cur] = idx

        return ret