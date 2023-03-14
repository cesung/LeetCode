class Solution:

    def __init__(self):
        self.rcd = defaultdict(int)

    def dp(self, nums, idx):
        if idx == 1:
            return max(nums[0], nums[1])
        elif idx == 0:
            return nums[0]

        if idx in self.rcd:
            return self.rcd[idx]

        self.rcd[idx] = max(self.dp(nums, idx - 2)  + nums[idx], self.dp(nums, idx - 1))

        return self.rcd[idx]

    # O(n) time | O(n) space
    # Top-down DP
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        return self.dp(nums, N - 1)

class Solution2:
    # O(n) time | O(1) space
    # Buttom-up DP, rolling memory
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        rcd = [ 0 for _ in range(2) ]  # O(1) memory usage
        rcd[0] = nums[0]
        rcd[1] = max(rcd[0], nums[1])

        for num in nums[2:]:
            maxv = max(rcd[0] + num, rcd[1])
            rcd[0] = rcd[1]
            rcd[1] = maxv

        return rcd[1]
