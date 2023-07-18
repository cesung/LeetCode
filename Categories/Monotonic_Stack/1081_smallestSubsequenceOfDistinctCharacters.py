from typing import *
from collections import defaultdict

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        rcd = defaultdict(int)
        for idx, ch in enumerate(s):
            rcd[ch] = idx

        vis = set()
        stk = []
        for idx, ch in enumerate(s):
            if ch in vis:
                continue

            while (
                stk and
                ord(stk[-1]) > ord(ch) and
                rcd[stk[-1]] > idx
            ):
                rm_ch = stk.pop()
                vis.remove(rm_ch)

            stk.append(ch)
            vis.add(ch)
        
        return "".join(stk)
