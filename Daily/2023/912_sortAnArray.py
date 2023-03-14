from typing import *

class Solution:
    def merge_sort(self, nums):
        size = len(nums)

        if size == 1:
            return nums
        
        left = self.merge_sort(nums[:size // 2])
        left_size = len(left)
        right = self.merge_sort(nums[size // 2:])
        right_size = len(right)

        ret = []
        left_idx, right_idx = 0, 0
        while (
            left_idx < left_size and
            right_idx < right_size
        ):
            if left[left_idx] < right[right_idx]:
                ret.append(left[left_idx])
                left_idx += 1
            else:
                ret.append(right[right_idx])
                right_idx += 1
        
        while left_idx < left_size:
            ret.append(left[left_idx])
            left_idx += 1
        
        while right_idx < right_size:
            ret.append(right[right_idx])
            right_idx += 1

        return ret

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
