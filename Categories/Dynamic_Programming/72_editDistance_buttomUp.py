import sys
from typing import *

""" 
replace:
    word1 = [X X X X idx]
    word2 = [Y Y Y Y Y Y jdx]

    idx != jdx, either
        . replace idx -> jdx => dp[idx - 1][jdx - 1] + 1
            word1 = [X X X X] jdx
            word2 = [Y Y Y Y Y Y] jdx

        . replace jdx -> idx => dp[idx - 1][jdx - 1] + 1
            word1 = [X X X X] idx
            word2 = [Y Y Y Y Y Y] idx
"""

"""
insert
    word1 = X X X X idx
    word2 = Y Y Y Y Y Y jdx

    idx != jdx, either
        . insert jdx at the end of word1 => dp[idx][jdx - 1] + 1
            word1 = [X X X X idx] jdx
            word2 = [Y Y Y Y Y Y] jdx

        . insert idx at the end of word2 => dp[idx - 1][jdx] + 1
            word1 = [X X X X] idx
            word2 = [Y Y Y Y Y Y jdx] idx
"""

"""
delete
    word1 = X X X X idx
    word2 = Y Y Y Y Y Y jdx

    idx != jdx, either
        . delete idx at the end of word1 => dp[idx - 1][jdx] + 1
            word1 = [X X X X]
            word2 = [Y Y Y Y Y Y jdx]

        . delete jdx at the end of word2 => dp[idx][jdx - 1] + 1
            word1 = [X X X X idx]
            word2 = [Y Y Y Y Y Y]
"""

"""
Summary:
    dp[idx - 1][jdx] + 1:
        . delete idx at the end of word1 OR
        . insert idx at the end of word2

    dp[idx][jdx - 1] + 1:
        . delete jdx at the end of word2 OR
        . insert jdx at the end of word1

    dp[idx - 1][jdx - 1] + 1:
        . replace idx at the end of word1 to jdx
        . replace jdx at the end of word2 to idx
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)

        # dp[idx][jdx]: the minimum number of operations required to convert word1[:idx] to word2[:jdx], both indices inclusive.
        dp = [ [sys.maxsize for _ in range(len2 + 1)] for _ in range(len1 + 1) ]

        # dummy word, make word1 and word2 both 1-index
        word1 = "#" + word1
        word2 = "#" + word2

        # dp[0][jdx] = jdx
        for jdx in range(len2 + 1):
            dp[0][jdx] = jdx
        
        # dp[idx][0] = idx
        for idx in range(len1 + 1):
            dp[idx][0] = idx
        
        for idx in range(1, len1 +1):
            for jdx in range(1, len2 + 1):
                if word1[idx] == word2[jdx]:
                    dp[idx][jdx] = dp[idx - 1][jdx - 1]
                else:
                    dp[idx][jdx] = min(
                        dp[idx][jdx],
                        dp[idx - 1][jdx] + 1,
                        dp[idx][jdx - 1] + 1,
                        dp[idx - 1][jdx-  1] + 1
                    )
        
        return dp[len1][len2]