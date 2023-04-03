from typing import *

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        size = len(people)
        people.sort()
        left, right = 0, size - 1

        cnt = 0
        while left < right:
            ttl = people[left] + people[right]
            if ttl > limit:
                cnt += 1
                right -= 1
            else:
                cnt += 1
                left += 1; right -= 1

        return cnt + 1 if left == right else cnt