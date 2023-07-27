from typing import *

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)

        # sort events by ending time, increasingly, O(nlog(n))
        events.sort(key = lambda event : event[1])
        # dummy data
        events = [[-1, -1, -1]] + events

        # earliest event that can attend if we attend the i-th event, O(nlog(n))
        prev = [0 for _ in range(n + 1)]
        for idx in range(2, n + 1):
            left, right = 0, idx - 1
            while left < right:
                mid = (left + right) // 2 + 1
                if events[mid][1] >= events[idx][0]:
                    right = mid - 1
                else:
                    left = mid
            
            prev[idx] = left

        
        # dp[idx][jdx]: the maximum value can take by attending jdx events (1-index) in the first idx events (1-index)
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        dp[1][1] = events[1][2]

        for idx in range(1, n + 1):
            for jdx in range(1, k + 1):
                # don't attend the idx-event
                dp[idx][jdx] = dp[idx - 1][jdx]

                prev_val = dp[prev[idx]][jdx - 1] if prev[idx] != 0 else 0

                # attend the idx-event
                dp[idx][jdx] = max(
                    dp[idx][jdx],
                    prev_val + events[idx][2]
                )

        return dp[-1][k]