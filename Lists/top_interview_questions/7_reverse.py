class Solution:

    def __init__(self):
        self.MAX = 2**31 - 1

    def reverse(self, x: int) -> int:
        is_negative = True if x < 0 else False
        x = abs(x)

        rst = 0
        while x > 0:

            if is_negative:
                if self.MAX // 10 < rst:
                    return 0
            else:
                if self.MAX // 10 < rst:
                    return 0
            rst *= 10

            r = x % 10
            if is_negative:
                if self.MAX - rst + 1 < r:
                    return 0
            else:
                if self.MAX - rst < r:
                    return 0
            rst += r

            x //= 10

        return -rst if is_negative else rst
