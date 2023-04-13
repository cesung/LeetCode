from typing import *

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        size = len(pushed)
        
        stk = []; popped_idx = 0
        for val in pushed:
            stk.append(val)
            while (
                stk and
                stk[-1] == popped[popped_idx]
            ):
                stk.pop()
                popped_idx += 1

        return stk == []