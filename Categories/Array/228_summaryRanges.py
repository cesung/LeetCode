from typing import *


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        prev = nums[0]

        ret = []
        for idx in range(1, n + 1):
            if idx == n:
                ret.append(
                    f"{prev}->{nums[idx - 1]}" if prev != nums[idx - 1] else
                    f"{nums[idx - 1]}"
                )
                break

            if nums[idx] != nums[idx - 1] + 1:
                ret.append(
                    f"{prev}->{nums[idx - 1]}" if prev != nums[idx - 1] else
                    f"{nums[idx - 1]}"
                )
                prev = nums[idx]
        
        return ret