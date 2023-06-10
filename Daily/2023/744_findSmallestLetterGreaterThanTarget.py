from typing import *


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2
            if ord(letters[mid]) <= ord(target):
                left = mid + 1
            else:
                right = mid

        if ord(letters[left]) <= ord(target):
            return letters[0]

        return letters[left]
