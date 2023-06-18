from typing import *


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        pairs = []
        for pos, spd in zip(position, speed):
            pairs.append( (pos, spd) )
        pairs.sort(key = lambda x: x[0])

        ret = 1
        prev = n - 1
        for idx in range(n - 2, -1, -1):
            t_prev = (target - pairs[prev][0]) / pairs[prev][1]
            t_cur = (target - pairs[idx][0]) / pairs[idx][1]

            if t_cur > t_prev:
                prev = idx
                ret += 1
        
        return ret