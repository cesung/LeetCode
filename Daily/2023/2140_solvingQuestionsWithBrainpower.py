from typing import *


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        size = len(questions)
        dp = [0 for _ in range(size)]
        dp[-1] = questions[-1][0]

        for idx in range(size-2, -1, -1):
            if idx + questions[idx][1] + 1 >= size:
                dp[idx] = max(
                    questions[idx][0],
                    dp[idx + 1]
                )
            else:
                dp[idx] = max(
                    questions[idx][0] + dp[idx + questions[idx][1] + 1],
                    dp[idx + 1]
                )

        return dp[0]
