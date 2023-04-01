from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left, right = 0, size - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left if nums[left] == target else -1