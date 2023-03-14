class Solution:

    # O(nd) time | O(n) space
    # Buttom-up DP
    def coinChange(self, coins: List[int], amount: int) -> int:
        nums = [float('inf') for _ in range(amount + 1)]
        nums[0] = 0

        for coin in coins:
            for idx in range(coin, amount + 1):
                nums[idx] = min(nums[idx], 1 + nums[idx - coin])

        return -1 if nums[-1] == float('inf') else nums[-1]

class Solution2:

    from collections import defaultdict

    def __init__(self):
        self.rcd = defaultdict(int, {0:0})

    def dp(self, coins, amount):

        if amount in self.rcd:
            return self.rcd[amount]

        min_coin = float('inf')
        for coin in coins:
            if amount - coin < 0:
                break
            num_coin = self.dp(coins, amount - coin) + 1
            min_coin = min(min_coin, num_coin)

        self.rcd[amount] = min_coin
        return self.rcd[amount]

    # O(nd) time | O(n) space
    # Top-down DP
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        min_coin = self.dp(coins, amount)

        return -1 if min_coin == float('inf') else min_coin
