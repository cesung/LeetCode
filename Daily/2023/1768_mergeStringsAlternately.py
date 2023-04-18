from typing import *

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        ptr1, ptr2 = 0, 0

        ret = []
        turn = True

        while (
            ptr1 < len1 and
            ptr2 < len2
        ):
            if turn == True:
                ret.append(word1[ptr1])
                ptr1 += 1
            else:
                ret.append(word2[ptr2])
                ptr2 += 1
            
            turn = not turn
        
        if ptr1 == len1:
            ret.append(word2[ptr2:])
        else:
            ret.append(word1[ptr1:])
        
        return "".join(ret)