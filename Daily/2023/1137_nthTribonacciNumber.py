class Solution:
    def tribonacci(self, n: int) -> int:
        rcd = [0 for _ in range(37 + 1)]
        rcd[0] = 0
        rcd[1] = rcd[2] = 1
        
        for idx in range(3, n + 1):
            rcd[idx] = rcd[idx - 1] + rcd[idx - 2] + rcd[idx - 3]
        
        return rcd[n]
