import sys
from typing import *

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)

        # dp[idx][jdx] : the minimum number of steps required to make word1[:idx] and word2[:jdx] the same (both indices inclusive)
        dp = [[sys.maxsize for _ in range(len2 + 1)] for _ in range(len1 + 1)]

        # dummy word, make word1 and word2 both 1-index
        word1 = "#" + word1
        word2 = "#" + word2

        # dp[0][jdx] = jdx
        for jdx in range(len2 + 1):
            dp[0][jdx] = jdx
        
        # dp[idx][0] = idx
        for idx in range(len1 + 1):
            dp[idx][0] = idx
        
        for idx in range(1, len1 + 1):
            for jdx in range(1, len2 + 1):
                if word1[idx] == word2[jdx]:
                    dp[idx][jdx] = min(
                        dp[idx][jdx],
                        dp[idx - 1][jdx - 1]
                    )
                else:
                    dp[idx][jdx] = min(
                        dp[idx][jdx],
                        dp[idx - 1][jdx] + 1,
                        dp[idx][jdx - 1] + 1,
                    )
    
        return dp[len1][len2]