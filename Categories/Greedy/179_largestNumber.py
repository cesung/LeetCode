from typing import *
from functools import cmp_to_key

class Solution:
    def get_size(self, val):
        if val == 0:
            return 1

        size = 0
        while val:
            size += 1
            val //= 10
        
        return size

    def sortFunc(self, val1, val2):
        val12 = val1 * 10**self.get_size(val2) + val2
        val21 = val2 * 10**self.get_size(val1) + val1
        return 1 if val12 > val21 else -1

    
    def largestNumber(self, nums: List[int]) -> str:
        size = len(nums)
        nums.sort(key = cmp_to_key(self.sortFunc), reverse=True)

        ttl = 0
        for idx in range(size):
            ttl *= 10 ** self.get_size(nums[idx])
            ttl += nums[idx]

        return str(ttl)