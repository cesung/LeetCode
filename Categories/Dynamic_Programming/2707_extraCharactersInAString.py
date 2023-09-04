from typing import *
import sys

class Solution:
    # both idx, jdx are includsive
    def dfs(self, idx: int, jdx: int) -> int:
        if jdx == self.n - 1:
            return 0 if (
                self.s[idx : jdx + 1] in self.dictionary
            ) else jdx - idx + 1
        
        
        if (idx, jdx) in self.dp:
            return self.dp[ (idx, jdx) ]
        
        ret = sys.maxsize
        ret = min(
            ret,
            (jdx - idx + 1) + self.dfs(jdx + 1, jdx + 1),
            self.dfs(idx, jdx + 1)
        )
        
        # if match
        if self.s[idx : jdx + 1] in self.dictionary:
            ret = min(
                ret,
                self.dfs(jdx + 1, jdx + 1)
            )
            
        self.dp[ (idx, jdx) ] = ret
        return ret

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.n = len(s)
        self.s = s
        self.dp = defaultdict(int)
        self.dictionary = set(dictionary)
        
        return self.dfs(0, 0)

        