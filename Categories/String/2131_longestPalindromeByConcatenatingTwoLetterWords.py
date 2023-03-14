from typing import *
from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ret = 0
        rcd = defaultdict(int)
        vis = set()

        for word in words:
            rcd[word] += 1
        
        flag = False
        for word in rcd:
            rev_word = word[::-1]
    
            if rev_word in vis:
                continue
            
            if (
                word == rev_word and
                rcd[word] % 2 == 1
            ):
                flag = True

            if rev_word in rcd:

                if word == rev_word:
                    ret += rcd[word] // 2 * 4
                else:
                    ret += min(
                        rcd[word],
                        rcd[rev_word],
                    ) * 4

            vis.add(word)
            vis.add(rev_word)
    
        return ret if not flag else ret + 2