from typing import *

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [
            nums[nums[idx]] for idx in range(len(nums))
        ]