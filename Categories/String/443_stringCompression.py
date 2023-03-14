from typing import *

class Solution:
    def compress(self, chars: List[str]) -> int:
        size = len(chars)
        if size == 1:
            return 1

        left, right = 0, 0
        while right < size:
            cnt = 1
            while right < size - 1 and chars[right] == chars[right + 1]:
                cnt += 1
                right += 1
            
            chars[left] = chars[right]
            left += 1
        
            if cnt > 1:
                for digit in str(cnt):
                    chars[left] = digit
                    left += 1
            right += 1

        return left