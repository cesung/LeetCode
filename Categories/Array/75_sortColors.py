from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0 red
        # 1 white
        # 2 blue
        size = len(nums)
        
        ptr = idx = 0
        while idx < size:
            if nums[idx] == 0:
                nums[idx], nums[ptr] = nums[ptr], nums[idx]
                ptr += 1
            
            idx += 1
        
        ptr = idx = size - 1
        while idx >= 0:
            if nums[idx] == 2:
                nums[idx], nums[ptr] = nums[ptr], nums[idx]
                ptr -= 1
            idx -= 1