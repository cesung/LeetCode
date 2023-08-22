from typing import *
    
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = []        
        
        while columnNumber:
            columnNumber -= 1
            ret.append(columnNumber % 26)
            columnNumber //= 26
        
        return "".join( chr(ord('A') + num) for num in ret[::-1])