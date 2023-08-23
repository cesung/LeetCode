from typing import *

class Solution:
    # O(\sqrt{n}\log_{\log_{n}} + n)
    def getPrimes(self, n: int) -> List[int]:
        if n <= 1:
            return []
        
        ptb = [True for _ in range(n + 1)]
        ptb[0] = ptb[1] = False
        
        idx = 2
        while idx ** 2 <= n:
            if ptb[idx] == True:
                for jdx in range(idx**2, n + 1, idx):
                    ptb[jdx] = False
                
            idx += 1
    
        primes = []
        for idx in range(n + 1):
            if ptb[idx] == True:
                primes.append(idx)
        
        return primes
        
    
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        primes = self.getPrimes(n - 1)
        
        return len(primes)