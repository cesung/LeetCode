from typing import *
from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_size = len(nums1); nums2_size = len(nums2)

        # mapping from nums1 to nums2
        rcd = defaultdict(int)
        for idx, num1 in enumerate(nums1):
            for jdx, num2 in enumerate(nums2):
                if num1 == num2:
                    rcd[idx] = jdx
                    break

        next_greater = [-1 for _ in range(nums2_size)]

        stk = []
        for idx, num in enumerate(nums2):
            while (
                stk and
                nums2[stk[-1]] < num
            ):
                jdx = stk.pop()
                next_greater[jdx] = idx
            stk.append(idx)

        ret = []
        for idx in range(nums1_size):
            ret.append(
                -1 if next_greater[rcd[idx]] == -1 else
                nums2[next_greater[rcd[idx]]]
            )
        
        return ret
