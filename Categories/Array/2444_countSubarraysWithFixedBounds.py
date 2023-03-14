from typing import *

class Solution:
    def countSubarrays(self, nums: List[int], min_k: int, max_k: int) -> int:
        size = len(nums)
        prev_min_k, prev_max_k, boundary = -1, -1, -1

        ret = 0
        for idx in range(size):
            if (
                nums[idx] < min_k or
                nums[idx] > max_k
            ):
                boundary = idx
                continue
            if nums[idx] == min_k:
                prev_min_k = idx
            if nums[idx] == max_k:
                prev_max_k = idx
            
            ret += max(
                0,
                min(
                    prev_min_k,
                    prev_max_k
                ) - boundary,
            )
        
        return ret