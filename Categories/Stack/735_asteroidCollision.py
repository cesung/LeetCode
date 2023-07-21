from typing import *

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        
        stk = []
        for idx in range(n):
            if asteroids[idx] > 0:
                stk.append(asteroids[idx])
            else:
                if not stk or stk[-1] < 0:
                    stk.append(asteroids[idx])
                    continue
                
                while (
                    stk and
                    stk[-1] > 0 and
                    stk[-1] < abs(asteroids[idx])
                ):
                    stk.pop()

                if stk and stk[-1] == abs(asteroids[idx]):
                    stk.pop()
                    continue 

                if not stk or stk[-1] < 0:
                    stk.append(asteroids[idx])

        return stk