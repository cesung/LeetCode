from typing import *

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
    
        ret = []
        while n:
            ret.append(1 if n & 1 == 1 else 0)
            n = -(n >> 1)
        
        return "".join(map(str, ret[::-1]))