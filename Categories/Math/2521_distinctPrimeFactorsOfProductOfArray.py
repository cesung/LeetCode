import math

class Solution:
    
    def get_primes(self, n):
        primes = []

        ptb = [True for _ in range(n + 1)]
        ptb[0] = ptb[1] = False
        for idx in range(2, math.isqrt(n + 1) + 1):
            if ptb[idx]:
                for jdx in range(idx ** 2, n + 1, idx):
                    ptb[jdx] = False

        return [idx for idx in range(n + 1) if ptb[idx] == True]

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        max_num = max(nums)

        primes = self.get_primes(max_num)
        ret = 0
        vis = set()
        for num in nums:
            for prime in primes:
                if prime in vis:
                    continue
                if num % prime == 0:
                    ret += 1
                    vis.add(prime)

        return ret
