from typing import *

class Solution:
    def helper(self, target):
        buget = 0
        for num in self.nums:
            buget += (target - num)
            if buget < 0:
                return False
        
        return True

    def minimizeArrayValue(self, nums: List[int]) -> int:
        self.nums = nums
        left, right = nums[0], 10**9
        while left < right:
            mid = left + (right - left) // 2
            if not self.helper(mid):
                left = mid + 1
            else:
                right = mid
        
        return left