from typing import *


class Solution:
    def helper(self, key, answerKey, k):
        left = -1
        for right in range(self.n):
            if answerKey[right] != key:
                if k >= 0:
                    k -= 1
                
                while k < 0:
                    left += 1
                    k += 1 if answerKey[left] != key else 0

            self.ret = max(
                self.ret,
                right - left
            )

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        self.n = len(answerKey)
        self.ret = 0
        self.helper('T', answerKey[:], k)
        self.helper('F', answerKey[:], k)

        return self.ret
        
