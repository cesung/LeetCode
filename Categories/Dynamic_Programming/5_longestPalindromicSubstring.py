from typing import *


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        left, right = 0, 0
        dp = [[False for _ in range(n)] for _ in range(n)]

        for idx in range(n - 1, -1, -1):
            for jdx in range(idx, n):
                if (
                    s[idx] == s[jdx] and
                    (idx + 1 > jdx - 1 or dp[idx + 1][jdx - 1])
                ):
                    if jdx - idx > right - left:
                        left, right = idx, jdx
                    dp[idx][jdx] = True

        return s[left: right + 1]
