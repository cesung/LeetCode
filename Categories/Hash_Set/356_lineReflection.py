from typing import *
from collections import defaultdict

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        rcd = defaultdict(set)
        for x, y in points:
            rcd[y].add(x)

        mid_x = None
        for y in rcd:
            xs = rcd[y]
            if mid_x == None:
                min_x, max_x = min(xs), max(xs)
                mid_x = (min_x + max_x) / 2
            for x in xs:
                diff = abs(mid_x - x)
                if mid_x > x and x + 2*diff not in xs:
                    return False
                elif mid_x < x and x - 2*diff not in xs:
                    return False

        return True