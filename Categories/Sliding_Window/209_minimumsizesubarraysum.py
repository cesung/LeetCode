from typing import *

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        
        ret, cur_sum = n + 1, 0
        left = -1
        for right in range(n):
            cur_sum += nums[right]

            while cur_sum >= target:
                ret = min(
                    ret,
                    right - left
                )
                left += 1
                cur_sum -= nums[left]
        
        return ret if ret != n + 1 else 0