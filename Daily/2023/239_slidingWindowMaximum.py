from typing import *
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        queue = deque()
        for idx in range(k):
            while queue and queue[-1] < nums[idx]:
                queue.pop()
            queue.append(nums[idx])
        
        ret = []
        ret.append(queue[0])
        
        for idx in range(k, n):
            if nums[idx - k] == queue[0]:
                queue.popleft()
            while queue and queue[-1] < nums[idx]:
                queue.pop()
            queue.append(nums[idx])
            ret.append(queue[0])
        
        return ret
            