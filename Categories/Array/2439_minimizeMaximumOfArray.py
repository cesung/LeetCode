from typing import *

class Solution:
    def is_possible(self, val):
        cnt = 0
        for idx in range(self.size):
            cnt += (val - self.nums[idx])

            if cnt < 0:
                return False
        
        return True

    def minimizeArrayValue(self, nums: List[int]) -> int:
        self.nums = nums
        self.size = len(nums)

        left, right = nums[0], max(self.nums)
        while left < right:
            mid = left + (right - left) // 2
            if not self.is_possible(mid):
                left = mid + 1
            else:
                right = mid
        
        return left