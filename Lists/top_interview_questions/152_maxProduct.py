class Solution:
    # O(n) time | O(1) space
    # Buttom-up DP
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cur_max, cur_min, global_max = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            cur_max, cur_min = max(cur_max*num, cur_min*num, num), min(cur_max*num, cur_min*num, num)  # can't seperate into two lines
            global_max = max(cur_max, global_max)

        return global_max
