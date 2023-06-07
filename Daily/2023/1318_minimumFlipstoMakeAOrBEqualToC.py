from typing import *


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        while a or b or c:
            a_bit, b_bit, c_bit = a % 2, b % 2, c % 2
            if c_bit == 0:
                cnt += (a_bit + b_bit)
            else:
                cnt += 1 if (
                    a_bit == 0 and
                    b_bit == 0
                ) else 0

            a //= 2
            b //= 2
            c //= 2

        return cnt