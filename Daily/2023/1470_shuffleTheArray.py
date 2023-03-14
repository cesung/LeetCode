class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret = []
        left, right = 0, n
        while left < n:
            ret.append(nums[left])
            ret.append(nums[right])
            left += 1
            right += 1
        
        return ret
