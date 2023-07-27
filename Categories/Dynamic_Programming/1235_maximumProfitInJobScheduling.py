from typing import *

class Solution:
    def jobScheduling(self, start_times: List[int], end_times: List[int], profits: List[int]) -> int:
        jobs = [
            [start_time, end_time, profit]
            for start_time, end_time, profit in zip(start_times, end_times, profits)
        ]
        n = len(jobs)

        # sort by ending time, increasingly, O(nlog(n))
        jobs.sort(key = lambda job : job[1])

        # the earliest non-overlapping job index can take if we take the i-th index, O(nlog(n))
        prev = [-1 for _ in range(n)]

        for idx in range(1, n): 
            left, right = 0, idx - 1
            while left < right:
                mid = (left + right) // 2 + 1
                if jobs[mid][1] > jobs[idx][0]:
                    right = mid - 1
                else:
                    left = mid
        
            if jobs[left][1] > jobs[idx][0]:
                prev[idx] = -1
            else:
                prev[idx] = left

        # the maximum profit can take from the first i intervals
        dp = [0 for _ in range(n)]
        dp[0] = jobs[0][2]

        for idx in range(1, n):
            # do not take i-th job
            dp[idx] = max(
                dp[idx],
                dp[idx - 1]
            )
            # take i-th job
            prev_profit = dp[prev[idx]] if prev[idx] != -1 else 0
            dp[idx] = max(
                dp[idx],
                prev_profit + jobs[idx][2]
            )

        return dp[-1]