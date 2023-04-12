from typing import *

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and ch == '*':
                stack.pop()
                continue
            stack.append(ch)

        return "".join(stack)