class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        step = 0
        left, right = 0, 0
        
        while right < size - 1:
            tmp = right
            for idx in range(left, right + 1):
                right = max(right, idx + nums[idx])
            left = tmp + 1
            step += 1
        
        return step
