from typing import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        rcd = defaultdict(int)
        for idx in range(32):
            for num in nums:
                rcd[idx] += (num >> idx) & 1

        ret = 0
        for idx in range(32):
            ret += (rcd[idx] % 3) << idx
        
        """
        Python doesn't have fixed-size integers, they are dynamically allocated. 
        The interpreter doesn't know if the answer is constructed in 2's complement or not. 
        In other words, it doesn't know if the leftmost set MSB is a sign bit or a value bit.

        Convert to 2's complement by subtracting 2**32 from ret
        """
        return ret if ret < (1 << 31) else ret - (1 << 32)