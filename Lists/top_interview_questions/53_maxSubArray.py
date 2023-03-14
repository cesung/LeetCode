class Solution:
	# O(n) time | O(1) space
    # Buttom-up DP
    def maxSubArray(self, nums):
        cur_max, gbl_max = nums[0], nums[0]
        for num in nums[1:]:
            cur_max = max(cur_max + num, num)
            gbl_max = max(gbl_max, cur_max)

        return gbl_max

class Solution2:

    def __init__(self):
        self.gbl_max = -float('inf')

    def dp(self, pos, nums):
        if pos == len(nums):
            return 0

        cur_max = max(nums[pos] + self.dp(pos + 1, nums), nums[pos])
        self.gbl_max = max(self.gbl_max, cur_max)

        return cur_max

    # O(n) time | O(1) space
    # Top-down DP
    def maxSubArray(self, nums):
        self.dp(0, nums)
        return self.gbl_max

