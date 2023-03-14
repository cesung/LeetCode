from typing import *

class Solution:
    def get_num_trips(self, search_time):
        ret = 0
        for time in self.times:
            ret += search_time // time
        
        return ret

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        self.times = time

        left, right = 1, 10**7 * 10**7
        while left < right:
            mid = left + (right - left) // 2
            if self.get_num_trips(mid) < totalTrips:
                left = mid + 1
            else:
                right = mid
        
        return left