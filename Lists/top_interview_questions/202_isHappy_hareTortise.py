class Solution:

    def squared_sum(self, k):
        ttl = 0
        while k > 0:
            ttl += (k % 10)**2
            k //= 10

        return ttl

    # O(K) time | O(1) space
    def isHappy(self, n: int) -> bool:
        hare, tortoise = n, n
        while True:
            tortoise = self.squared_sum(tortoise)  # one step
            hare =  self.squared_sum(self.squared_sum(hare))  # two steps
            if hare == tortoise:
                break

        return True if hare == 1 else False
