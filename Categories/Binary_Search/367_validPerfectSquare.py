from typing import *

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, 2**31-1
        
        while left < right:
            mid = left + (right - left) // 2
            if mid**2 < num:
                left = mid + 1
            else:
                right = mid
        
        return True if left**2 == num else False