from typing import *


class StockSpanner:

    def __init__(self):
        self.size = 0
        self.prices = []
        self.stk = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        self.size += 1

        while (
            self.stk and 
            self.prices[self.stk[-1]] <= price
        ):
            self.stk.pop()

        prev_idx, cur_idx = self.stk[-1] if self.stk else -1, self.size - 1
        self.stk.append(cur_idx)

        return (
            cur_idx + 1 if prev_idx == -1 else
            cur_idx - prev_idx
        )
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)