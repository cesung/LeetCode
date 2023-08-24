from typing import *

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for idx in range(1, n//2 + 1):
            if n % idx == 0:
                m = n // idx
                if s[:idx] * m == s:
                    return True
    
        return False