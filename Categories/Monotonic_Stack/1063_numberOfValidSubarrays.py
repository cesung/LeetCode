class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        size = len(nums)
        next_larger = [size for idx in range(size)]

        stk = []
        for idx in range(size):
            while stk and nums[idx] < nums[stk[-1]]:
                next_larger[stk[-1]] = idx
                stk.pop()
            
            stk.append(idx)
    
        ttl = 0
        for idx in range(size):
            ttl += (next_larger[idx] - idx)
        
        return ttl
