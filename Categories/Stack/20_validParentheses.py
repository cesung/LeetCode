from collections import defaultdict
from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        rcd = defaultdict(str, {
            '}' : '{',
            ']' : '[',
            ')' : '(',
        })

        stack = []
        for ch in s:
            if ch in ['{', '[', '(']:
                stack.append(ch)
            else:
                if not stack or stack[-1] != rcd[ch]:
                    return False
                stack.pop()

        return not stack