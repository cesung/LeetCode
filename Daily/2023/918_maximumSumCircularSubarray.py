class Solution:
    def maxSubarray(self, nums):
        size = len(nums)
        cur, max_so_far = nums[0], nums[0]

        for idx in range(1, size):
            cur = nums[idx] if cur + nums[idx] < nums[idx] else cur + nums[idx]
            max_so_far = max(max_so_far, cur)
        
        return max_so_far

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        INF = float('inf')

        size = len(nums)
        max_circular_subarray = self.maxSubarray(nums)

        max_suffix = [nums[-1]]
        cur_suffix = nums[-1]
        for idx in range(size - 2, -1, -1):
            cur_suffix += nums[idx]
            max_suffix.append(
                max(
                    max_suffix[-1],
                    cur_suffix,
                )
            )
        max_suffix = max_suffix[::-1]
        max_suffix.append(0)

        prefix = 0
        for idx in range(size):
            prefix += nums[idx]
            max_circular_subarray = max(
                max_circular_subarray,
                prefix + max_suffix[idx + 1],
            )
        
        return max_circular_subarray
