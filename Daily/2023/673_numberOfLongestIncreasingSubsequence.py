from typing import *

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # times[i]: number of LIS ending at index idx
        times = [1 for _ in range(n)]
        # lens[i]: length of LIS ending at index idx
        lens = [1 for _ in range(n)]

        for idx in range(1, n):
            for jdx in range(idx):
                if nums[idx] <= nums[jdx]:
                    continue

                if lens[jdx] + 1 < lens[idx]:
                    continue
                elif lens[jdx] + 1 == lens[idx]:
                    times[idx] += times[jdx]
                else:
                    times[idx] = times[jdx]

                lens[idx] = lens[jdx] + 1 
                    
        ret = 0
        max_len = 0
        for idx in range(n):
            if lens[idx] > max_len:
                max_len = lens[idx]
                ret = times[idx]
            elif lens[idx] == max_len:
                ret += times[idx]
        
        return ret