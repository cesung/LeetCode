from typing import *

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        size = len(potions)

        ret = []
        for spell in spells:
            left, right = 0, size - 1
            while left < right:
                mid = left + (right - left) // 2
                if spell * potions[mid] < success:
                    left = mid + 1
                else:
                    right = mid
            ret.append(
                size - left if potions[left] * spell >= success else 0
            )

        return ret