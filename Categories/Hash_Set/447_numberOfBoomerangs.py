from typing import *
from collections import defaultdict

class Solution:
    def calDist(self, points: List[List[int]], idx: int, jdx: int) -> int:
        return (
            (points[idx][0] - points[jdx][0])**2 +
            (points[idx][1] - points[jdx][1])**2
        )

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)

        ret = 0
        for idx in range(n):
            dist_rcd = defaultdict(int)
            for jdx in range(n):
                dist_rcd[self.calDist(points, idx, jdx)] += 1
            
            for cnt in dist_rcd.values():
                ret += cnt * (cnt - 1)
        
        return ret