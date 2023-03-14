class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        size = len(costs)
        costs.sort()

        idx = 0
        while idx < size and coins >= costs[idx]:
            coins -= costs[idx]
            idx += 1
        
        return idx
