from typing import *

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        size = len(s)

        cnt = 0
        left, right = 0, k
        for idx in range(left, right):
            if s[idx] in vowels:
                cnt += 1

        max_cnt = cnt
        while right < size:
            cnt += 1 if s[right] in vowels else 0
            cnt -= 1 if s[left] in vowels else 0
            left += 1
            right += 1

            max_cnt = max(
                max_cnt,
                cnt,
            )
    
        return max_cnt
