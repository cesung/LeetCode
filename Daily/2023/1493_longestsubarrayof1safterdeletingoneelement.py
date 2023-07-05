from typing import *


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        cnt = ret = 0

        left = -1
        for right in range(n):
            if nums[right] == 0:
                cnt += 1
                
                while cnt > 1:
                    left += 1
                    cnt -= (1 - nums[left])

            ret = max(
                ret,
                right - left - cnt
            )
        
        return ret if ret != n else n - 1