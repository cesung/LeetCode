from typing import *

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        INF = sys.maxsize
        arr = [-INF] + arr + [-INF]
        
        n = len(arr)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid + 1] > arr[mid] > arr[mid - 1]:
                left = mid + 1
            else:
                right = mid
        
        return left - 1