class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        INF = float('inf')
        size = len(nums)
        ttl = sum(nums)
        prefix_sum = 0
        ret = -INF

        for idx in range(size):
            # first i + 1 elements
            prefix_sum += nums[idx]
            # last n - i elements
            suffix_sum = ttl - prefix_sum + nums[idx]

            ret = max(ret, prefix_sum, suffix_sum)

        return ret
