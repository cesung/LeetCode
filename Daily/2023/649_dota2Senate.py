from typing import *
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        size = len(senate)
        R, D = deque(), deque()
        for idx, ch in enumerate(senate):
            if ch == 'R':
                R.append(idx)
            else:
                D.append(idx)
                
        while R and D:
            r, d = R.popleft(), D.popleft()
            min_idx = min(r, d)
            if r == min_idx:
                R.append(r + size)
            else:
                D.append(d + size)

        return "Radiant" if R else "Dire"