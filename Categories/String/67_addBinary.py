from typing import *

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_size, b_size = len(a), len(b)
        a, b = list(map(int, list(a[::-1]))), list(map(int, list(b[::-1])))
        a_ptr, b_ptr = 0, 0

        carry = 0
        ret = []
        while (
            a_ptr < a_size or
            b_ptr < b_size or
            carry
        ):
            a_val = a[a_ptr] if a_ptr < a_size else 0
            b_val = b[b_ptr] if b_ptr < b_size else 0
            ttl = a_val + b_val + carry
            ret.append(ttl % 2)
            carry = ttl // 2

            a_ptr += 1
            b_ptr += 1

        return "".join(map(str, ret[::-1]))