from typing import *

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k

        size = len(arr)
        num_miss = []
        for idx, num in enumerate(arr):
            num_miss.append(num - 1 - idx)

        left, right = 0, size - 1
        while left < right:
            mid = left + (right - left) // 2 + 1
            if num_miss[mid] >= k:
                right = mid - 1
            else:
                left = mid

        return arr[left] + (k - num_miss[left])
