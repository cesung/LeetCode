from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        size = len(nums)
        dp = defaultdict(int, {
            0 : 1
        })

        ttl = 0
        cur = 0
        for idx in range(size):
            cur += nums[idx]
            ttl += dp[cur % k]
            dp[cur % k] += 1
        
        return ttl
