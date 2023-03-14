class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        size = len(nums)
        ttl = sum(nums)

        prefix_sum = [0]
        for idx in range(size):
            prefix_sum.append(prefix_sum[-1] + nums[idx])
        
        for idx in range(size):
            if prefix_sum[idx] == ttl - nums[idx] - prefix_sum[idx]:
                return idx

        return -1
