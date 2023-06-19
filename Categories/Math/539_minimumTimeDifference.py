from typing import *
import sys

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)

        timePoints = set(timePoints)
        if len(timePoints) != n:
            return 0 

        times = []
        for time in timePoints:
            hour, minute = map(int, time.split(":"))
            times.append(hour * 60 + minute)
        
        times.sort()

        min_diff = sys.maxsize
        for idx in range(1, n):
            min_diff = min(
                min_diff,
                times[idx] - times[idx - 1]
            )
        
        max_time = 24 * 60
        min_diff = min(
            min_diff,
            (max_time - times[-1]) + times[0]
        )

        return min_diff