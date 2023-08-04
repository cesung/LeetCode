from typing import *

class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        word_set = set(word_dict)

        n = len(s)
        s = "#" + s
        
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        
        for idx in range(1, n + 1):
            for jdx in range(idx):
                if dp[jdx] and s[jdx + 1:idx + 1] in word_set:
                    dp[idx] = True
        
        return dp[-1]