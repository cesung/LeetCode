from typing import *

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        nums = [-1] + nums
        
        dp = [False for _ in range(n + 1)]
        dp[0] = 1
        
        for idx in range(1, n + 1):
            if idx >= 2:
                dp[idx] |= dp[idx - 2] & (nums[idx] == nums[idx - 1])
            if idx >= 3:
                dp[idx] |= dp[idx - 3] & (nums[idx] == nums[idx - 1] == nums[idx - 2])
                dp[idx] |= dp[idx - 3] & ((nums[idx] - nums[idx - 1]) == 1 == (nums[idx - 1] - nums[idx - 2]))
    
        return dp[-1]