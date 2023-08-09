from typing import *

class Solution:
    def findPairsWithThreshold(self, n: int, nums: List[int], threshold: int) -> int:
        num_pairs = 0
        idx = 0
        while idx < n-1:
            if nums[idx + 1] - nums[idx] <= threshold:
                num_pairs += 1
                idx += 1
            idx += 1

        return num_pairs

    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if self.findPairsWithThreshold(n, nums, mid) < p:
                left = mid + 1
            else:
                right = mid
        
        return left