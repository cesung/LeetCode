from typing import *

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        size = len(nums)
        idx = 0
        cnt, ttl = 0, 0
        while idx < size:
            if nums[idx] == 0:
                cnt += 1
            else:
                ttl += (1 + cnt) * cnt // 2
                cnt = 0
            
            idx += 1
        
        ttl += (1 + cnt) * cnt // 2
        return ttl
