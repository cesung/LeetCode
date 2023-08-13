from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, cur_liters: int) -> bool:
        if (
            cur_liters < 0 or
            cur_liters > self.ttl_capacity
        ):
            return False
        
        if cur_liters == self.target_capacity:
            return True
    
        for operation in self.operations:
            nxt_liters = cur_liters + operation
            if nxt_liters in self.vis:
                continue
            self.vis.add(nxt_liters)
            if self.dfs(nxt_liters):
                return True
            
        return False

    
    def canMeasureWater(self, jug1_capacity: int, jug2_capacity: int, target_capacity: int) -> bool:
        self.ttl_capacity = jug1_capacity + jug2_capacity
        self.target_capacity = target_capacity
        self.operations = [
            +jug1_capacity,
            +jug2_capacity,
            -jug2_capacity,
            -jug2_capacity
        ]
        
        self.vis = set()
        
        self.vis.add(0)
        return self.dfs(0)