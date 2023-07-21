from typing import *

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        intervals.sort(key = lambda interval : interval[1])
        prev_end = intervals[0][1]
        cnt = 0

        for idx in range(1, n):
            if intervals[idx][0] >= prev_end:
                prev_end = intervals[idx][1]
            else:
                cnt += 1
        
        return cnt