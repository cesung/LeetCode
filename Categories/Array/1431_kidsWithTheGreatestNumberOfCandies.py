from typing import *

class Solution:
    def kidsWithCandies(self, candies: List[int], extra_candies: int) -> List[bool]:
        size = len(candies)
        maxv = max(candies)

        ret = [False] * size
        for idx in range(size):
            if candies[idx] + extra_candies >= maxv:
                ret[idx] = True
        
        return ret