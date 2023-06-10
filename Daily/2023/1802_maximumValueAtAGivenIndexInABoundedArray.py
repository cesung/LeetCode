from typing import *


class Solution:
    def getSum(self, height, n, index):
        # mid
        ttl = height

        # to left
        if height - index > 0:
            ttl += ((height - index) + (height - 1)) * index // 2
        else:
            ttl += index - height + 1
            ttl += (1 + height-1) * (height - 1) // 2

        # to right
        if height - (n - 1 - (index+1) + 1) > 0:
            ttl += ((height - (n - 1 - (index+1) + 1)) + (height - 1)) * (n - 1 - (index+1) + 1) // 2
        else:
            ttl += (n - 1 - (index+1) + 1) - height + 1
            ttl += (1 + height - 1) * (height - 1) // 2

        return ttl

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            mid = (left + right) // 2 + 1

            if self.getSum(mid, n, index) > maxSum:
                right = mid - 1
            else:
                left = mid
        
        return left