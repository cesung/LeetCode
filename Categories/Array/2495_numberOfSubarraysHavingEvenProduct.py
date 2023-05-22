from typing import *

class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        size = len(nums)

        # even number on the RHS cover to the left one
        # [1, 2, 3, 5, 6]
        # => [(1, 2), 3, 5, 6]
        # => [1, (2), 3, 5, 6]
        # => [1, 2, 3, 5, (6)]
        # => [1, 2, 3, (5, 6)]
        # => [1, 2, (3, 5, 6)]
        # => [1, (2, 3, 5, 6)]
        # => [(1, 2, 3, 5, 6)]
        rcd = [size for _ in range(size)]
        # O(n), find the first even number to the right
        first_even = size
        for idx in range(size - 1, -1, -1):
            rcd[idx] = first_even
            if nums[idx] % 2 == 0:
                first_even = idx

        ttl = 0
        for idx in range(size):
            if nums[idx] % 2 == 0:
                # left boundary = idx (- 0) + 1
                # [1, 2, 3, 5, 6]
                #  *  v
                # [(1, (2, 3, 5, 6]

                # right boundary = rcd[idx] - idx
                # [1, 2, 3, 5, 6]
                #     v        *
                # [1, 2), 3, 5, 6]
                # [1, 2, 3), 5, 6]
                # [1, 2, 3, 5), 6], can't pass by 6
                ttl += (idx + 1) * (rcd[idx] - idx)

        return ttl