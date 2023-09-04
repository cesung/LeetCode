from typing import *

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        
        # sort by price increasingly
        items.sort(key = lambda item : item[0])
        
        max_beauty = [0]
        for idx, (price, beauty) in enumerate(items[1:], 1):
            max_beauty.append(
                idx 
                if beauty > items[max_beauty[-1]][1] 
                else max_beauty[-1]
                
            )
            
        ret = []
        for query in queries:
            left, right = 0, n - 1
            while left < right:
                mid = left + (right - left) // 2 + 1
                if items[mid][0] > query:
                    right = mid - 1
                else:
                    left = mid    

            if items[left][0] > query:
                ret.append(0)
            else:
                ret.append(items[max_beauty[left]][1])
            
        return ret
                
        