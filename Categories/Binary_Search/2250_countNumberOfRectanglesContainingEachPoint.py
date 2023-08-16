from typing import *
from collections import defaultdict

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort(key = lambda x: x[0])
        rcd = defaultdict(list)
        
        for length, height in rectangles:
            rcd[height].append(length)
        
        ret = []
        for x, y in points:
            cnt = 0
            for height in range(y, 100 + 1):
                size = len(rcd[height])
                if size == 0:
                    continue
                    
                # binary search on length of rectangles with height euqals to `height`
                left, right = 0, size - 1
                while left < right:
                    mid = left + (right - left) // 2
                    if rcd[height][mid] < x:
                        left = mid + 1
                    else:
                        right = mid
                if rcd[height][left] < x:
                    continue
                cnt += (size - left)
            ret.append(cnt)
        
        return ret