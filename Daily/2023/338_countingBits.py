from typing import *

class Solution:
    def countBits(self, n: int) -> List[int]:
        rcd = [0 for _ in range(n + 1)]
        ret = [0]
        for idx in range(1, n + 1):
            rcd[idx] = rcd[idx // 2] + idx % 2
            ret.append(rcd[idx])
        
        return ret