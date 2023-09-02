from typing import *
from collections import defaultdict

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        rcd = defaultdict(int)
        
        ret = 1
        for idx, num in enumerate(nums):
            if num**2 in rcd:
                rcd[num] = rcd[num**2] + 1
            else:
                rcd[num] = 1
            
            ret = max(
                ret,
                rcd[num]
            )
    
        return ret if ret != 1 else -1
            