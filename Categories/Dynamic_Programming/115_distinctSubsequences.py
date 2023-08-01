from typing import *

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        
        # dp[idx][jdx]: number of distinct subsequences of s[:idx] which equals t[jdx], both indices includsive
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        s = "#" + s
        t = "#" + t

        # dp[idx][0] = 1
        for idx in range(n + 1):
            dp[idx][0] = 1

        for idx in range(1, n + 1):
            for jdx in range(1, m + 1):        
                if s[idx] == t[jdx]:
                    dp[idx][jdx] += dp[idx - 1][jdx - 1]
                dp[idx][jdx] += dp[idx - 1][jdx]
                

        return dp[n][m]
                

S = Solution()
print(S.numDistinct("rabbbit", "rabit"), 3)
print(S.numDistinct("babgbag", "bag"), 5)