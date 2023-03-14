class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        max_so_far = prices[size - 1]
        max_profit = 0

        for idx in range(size - 2, -1, -1):
            max_profit = max(
                max_profit,
                max_so_far - prices[idx]
            )
            max_so_far = max(
                max_so_far,
                prices[idx]
            )
        return max_profit
