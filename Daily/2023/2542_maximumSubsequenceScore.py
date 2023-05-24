from typing import *
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        INF = float('inf')
        size = len(nums1)
        arr = [(num2, num1) for num1, num2 in zip(nums1, nums2)]
        arr.sort(reverse=True)

        min_heap = []
        min_val = INF
        max_score = 0
        ttl = 0
        for idx in range(size):
            min_val = arr[idx][0]
            heapq.heappush(min_heap, arr[idx][1])
            ttl += arr[idx][1]

            if len(min_heap) > k:
                ttl -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                max_score = max(
                    max_score,
                    ttl * min_val
                )

        return max_score
