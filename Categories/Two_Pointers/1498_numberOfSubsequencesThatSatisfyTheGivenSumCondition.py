from typing import *


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        size = len(nums)
        nums.sort()

        ttl = 0
        left, right = 0, size - 1
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ttl = (ttl + 2**(right - left)) % MOD
                left += 1

        return ttl
