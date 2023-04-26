from typing import *

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        val = 0
        while num:
            val += num % 10
            num //= 10
        
        return self.addDigits(val)