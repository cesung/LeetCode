from typing import *
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rcd = defaultdict(int)
        for num in nums:
            rcd[num] += 1
        
        rcd = list(rcd.items())
        size = len(rcd)

        start, end = 0, size - 1
        while True:
            pivot, left, right = start, start + 1, end
            while left <= right:
                # < pivot to left
                # >= pivot to right
                if rcd[left][1] < rcd[pivot][1] and rcd[right][1] >= rcd[pivot][1]:
                    # do swap
                    rcd[left], rcd[right] = rcd[right], rcd[left]
                elif rcd[left][1] >= rcd[pivot][1]:
                    left += 1
                elif rcd[right][1] < rcd[pivot][1]:
                    right -= 1
            
            # right always >= pviot
            rcd[pivot], rcd[right] = rcd[right], rcd[pivot]

            if right == k-1:
                return [num for num, freq in rcd[:k] ]
            elif right > k-1:
                end = right - 1
            else: # right < k-1
                start = right + 1
        
        return -1