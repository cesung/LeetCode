from typing import *
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        len1, len2 = len(nums1), len(nums2)
        
        pq = [ ((nums1[0] + nums2[0]), 0, 0) ]
        vis = set()
        vis.add( (0, 0) )
        
        ret = []
        while k and pq:
            _, ptr1, ptr2 = heapq.heappop(pq)
            ret.append( (nums1[ptr1], nums2[ptr2]) )

            if (
                ptr1 + 1 < len1 and
                (ptr1 + 1, ptr2) not in vis
            ):
                vis.add( (ptr1 + 1, ptr2) )
                heapq.heappush(
                    pq,
                    ((nums1[ptr1 + 1] + nums2[ptr2]), ptr1 + 1, ptr2)
                )

            if (
                ptr2 + 1 < len2 and
                (ptr1, ptr2 + 1) not in vis
            ):
                vis.add( (ptr1, ptr2 + 1) )
                heapq.heappush(
                    pq,
                    ((nums1[ptr1] + nums2[ptr2 + 1]), ptr1, ptr2 + 1)
                )

            k -= 1
        
        return ret