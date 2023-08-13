from typing import *

class Solution:
    def binarySearch(self, prices: List[int], left: int, right: int, tastiness: int) -> int:
        target = prices[left] + tastiness
        while left < right:
            mid = left + (right - left) // 2
            if prices[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    def findBasketsOfKCadiesWithTastiness(self, prices: List[int], k: int, tastiness: int) -> bool:
        left, right = 0, len(prices) - 1
        
        while k > 1:
            nleft = self.binarySearch(prices, left, right, tastiness)
            if prices[nleft] < prices[left] + tastiness:
                return False
            left, right = nleft, len(prices) - 1
            k -= 1
            
        return True
    
    def maximumTastiness(self, prices: List[int], k: int) -> int:
        prices.sort()
        
        left, right = 0, prices[-1] - prices[0]
        while left < right:
            mid = left + (right - left) // 2 + 1
            if not self.findBasketsOfKCadiesWithTastiness(prices, k, mid):
                right = mid - 1
            else:
                left = mid

        return left