from typing import *
import sys

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        len1, len2 = len(s1), len(s2)

        # dp[idx][jdx]: the lowest ASCII sum of deleted characters to make string s1[0:idx] and s2[0:jdx] equal, both indices includsive.
        dp = [[sys.maxsize for _ in range(len2 + 1)] for _ in range(len1 + 1)]

        # dummy word, make s1, and s2 1-index
        s1 = "#" + s1
        s2 = "#" + s2

        # dp[0][0]
        dp[0][0] = 0

        for jdx in range(1, len2 + 1):
            dp[0][jdx] = dp[0][jdx - 1] + ord(s2[jdx])

        for idx in range(1, len1 + 1):
            dp[idx][0] = dp[idx - 1][0] + ord(s1[idx])
        
        for idx in range(1, len1 + 1):
            for jdx in range(1, len2 + 1):
                if s1[idx] == s2[jdx]:
                    dp[idx][jdx] = dp[idx - 1][jdx - 1]
                else:
                    dp[idx][jdx] = min(
                        dp[idx][jdx],
                        dp[idx - 1][jdx] + ord(s1[idx]),
                        dp[idx][jdx - 1] + ord(s2[jdx]),
                    )

        return dp[len1][len2]