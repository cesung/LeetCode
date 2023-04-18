from typing import *

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        M = 10**9 + 7
        target_size = len(target); word_size = len(words[0])

        word_count = [[0 for _ in range(26)] for _ in range(word_size)]
        for idx in range(word_size):
            for word in words:
                word_count[idx][ord(word[idx]) - ord('a')] += 1

        # dp[idx][kdx]: number of ways to build target[0:idx] using words[:][0:kdx]
        # dp[idx][kdx] = (don't use words[:][kdx]) + (use words[:][kdx])
        dp = [[0 for _ in range(word_size)] for _ in range(target_size)]
        # initial state for dp[0][:]
        dp[0][0] = word_count[0][ord(target[0]) - ord('a')]
        for kdx in range(1, word_size):
            dp[0][kdx] = dp[0][kdx - 1] + word_count[kdx][ord(target[0]) - ord('a')]

        for idx in range(1, target_size):
            for kdx in range(1, word_size):
                # don't use words[:][kdx]
                dp[idx][kdx] = dp[idx][kdx - 1]

                # use words[:][kdx]
                dp[idx][kdx] += (
                    dp[idx - 1][kdx - 1] * 
                    word_count[kdx][ord(target[idx]) - ord('a')]
                )

                dp[idx][kdx] %= M

        return dp[target_size - 1][word_size - 1]