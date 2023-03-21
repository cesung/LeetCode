from typing import *

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        cnt = 0
        for idx in range(size):
            left_suc, right_suc = False, False
            if (
                idx == 0 or
                idx != 0 and flowerbed[idx - 1] == 0
            ):
                left_suc = True
            if (
                idx == size - 1 or
                idx != size - 1 and flowerbed[idx + 1] == 0
            ):
                right_suc = True
            
            if (
                left_suc and
                right_suc
            ):
                cnt += 0 if flowerbed[idx] == 1 else 1
                flowerbed[idx] = 1
        
        return cnt >= n
            
            