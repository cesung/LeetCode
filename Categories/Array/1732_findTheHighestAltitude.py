from typing import *

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)

        max_alt, cur_alt = 0, 0
        for idx in range(n):
            cur_alt += gain[idx]
            max_alt = max(
                max_alt,
                cur_alt
            )
        
        return max_alt