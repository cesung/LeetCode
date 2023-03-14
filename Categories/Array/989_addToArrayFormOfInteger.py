from typing import *

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        size = len(num)

        val = 0
        for idx in range(size):
            val *= 10
            val += num[idx]
        
        val += k

        ret = []
        while val:
            ret.append(val % 10)
            val //= 10
        
        return ret[::-1]