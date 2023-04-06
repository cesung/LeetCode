import math
from typing import *

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        size = len(nums)

        ret = 0; prefix_sum = 0
        for idx in range(size):
            prefix_sum += nums[idx]
            ret = max(
               ret,
               math.ceil(prefix_sum / (idx + 1))
            )
        
        return ret