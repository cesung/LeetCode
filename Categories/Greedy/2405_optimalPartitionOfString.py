from typing import *

class Solution:
    def partitionString(self, s: str) -> int:
        size = len(s)
        vis = set()

        cnt = 0
        for idx in range(size):
            if s[idx] in vis:
                cnt += 1
                vis.clear()
            vis.add(s[idx])

        return cnt + 1