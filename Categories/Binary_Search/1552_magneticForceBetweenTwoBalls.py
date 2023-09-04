from typing import *

class Solution:
    def canPlace(self, dist: int, num: int) -> bool:
        prev = self.position[0]
        num -= 1
        
        while num:
            nxt = prev + dist
            left, right = 0, self.size - 1
            while left < right:
                mid = left + (right - left) // 2
                if self.position[mid] < nxt:
                    left = mid + 1
                else:
                    right = mid
            
            if self.position[left] < nxt:
                return False
        
            prev = self.position[left]
            num -= 1
        
        return True
        
    
    def maxDistance(self, position: List[int], m: int) -> int:
        self.size = len(position)
        self.position = position
        self.position.sort()
        left, right = 1, 10**9
        
        while left < right:
            mid = left + (right - left) // 2 + 1
            if not self.canPlace(mid, m):
                right = mid - 1
            else:
                left = mid
        
        return left