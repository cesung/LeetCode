from typing import *

class Solution:
    def find_rotation_point(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                left = mid + 1
            else:
                right = mid

        return -1 if nums[left] >= target else left
    
    def binary_search(self, nums: List[int], left: int, right: int, target: int) -> bool:
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return nums[left] == target

    def search(self, nums: List[int], target: int) -> bool:
        while len(nums) > 1 and nums[-1] == nums[0]:
            nums.pop()
        
        rotation_point = self.find_rotation_point(nums, nums[0])
        if rotation_point == -1:
            return self.binary_search(nums, 0, len(nums) - 1, target)

        return (
            self.binary_search(nums, 0, rotation_point - 1, target) if target >= nums[0] else 
            self.binary_search(nums, rotation_point, len(nums) - 1, target) 
        )