from typing import *
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rcd = defaultdict(int)
        for idx, num in enumerate(nums):
            if target - num in rcd:
                return [idx, rcd[target - num]]
        
            rcd[num] = idx
        
        # error handling
        return [-1, -1]