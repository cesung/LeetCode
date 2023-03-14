class Solution:
    def squared_sum(self, k):
        ttl = 0
        while k > 0:
            ttl += (k % 10)**2
            k //= 10

        return ttl

    # O(K) time | O(K) space
    def isHappy(self, n: int) -> bool:
        vis = set()
        k = n
        while True:
            if k == 1:
                return True

            k = self.squared_sum(k)

            if k in vis:
                return False
            else:
                vis.add(k)
