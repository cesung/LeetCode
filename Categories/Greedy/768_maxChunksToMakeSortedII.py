from typing import *


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        exp_arr = sorted(arr)
        # multi-set
        lack, extra = defaultdict(int), defaultdict(int)
        chunks = 0


        for val_arr, val_exp_arr in zip(arr, exp_arr):
            if val_arr in lack:
                lack[val_arr] -= 1
                if lack[val_arr] == 0:
                    del lack[val_arr]
            else:
                extra[val_arr] += 1

            if val_exp_arr in extra:
                extra[val_exp_arr] -= 1
                if extra[val_exp_arr] == 0:
                    del extra[val_exp_arr]
            else:
                lack[val_exp_arr] += 1
            
            if (
                not lack and
                not extra
            ):
                chunks += 1
            

        return chunks