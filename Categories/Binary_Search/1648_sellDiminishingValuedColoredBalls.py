from typing import *

class Solution:
    
    def countOrdersWithScore(self, score: int) -> int:
        orders = 0
        for num_balls in self.inventory:
            if num_balls < score:
                break
            orders += (num_balls - score + 1)
        return orders
    
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        self.inventory = inventory
        self.inventory.sort(reverse=True)
        MOD = 10**9 + 7
        
        left, right = 1, self.inventory[0]
        while left < right:
            mid = left + (right - left) // 2
            if self.countOrdersWithScore(mid) > orders:
                left = mid + 1
            else:
                right = mid
        
        score = 0
        for num_balls in self.inventory:
            if num_balls < left:
                break
            score = (score + (num_balls + left) * (num_balls - left + 1) // 2) % MOD
        
        remaining_order = orders - self.countOrdersWithScore(left)
        score = (score + remaining_order * (left - 1)) % MOD
        
        return score