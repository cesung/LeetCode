from typing import *

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ret = []
        ttl = 0
        for idx in range(n):
            if (
                idx < k or
                idx > n - 1 - k
            ):
                ret.append(-1)
                continue
            
            if idx == k:
                for jdx in range(idx - k, idx + k + 1):
                    ttl += nums[jdx]
            else:
                ttl += nums[idx + k] - nums[idx - k - 1]
            
            ret.append(ttl // (2*k+1))
        
        return ret
