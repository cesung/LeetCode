class Solution:

    def binary_search_leftmost(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid - 1

        return left if nums[left] == target else -1

    def binary_search_rightmost(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return left - 1 if nums[left - 1] == target else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        nums.append(float('inf'))  # add INF at the end of the input array

        left = self.repeated_bs_left(nums, target)
        right = self.repeated_bs_right(nums, target)

        return [left, right]
