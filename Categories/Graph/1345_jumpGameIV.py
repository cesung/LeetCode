from typing import *
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        size = len(arr)
        rcd = defaultdict(list)
        for idx, num in enumerate(arr):
            rcd[num].append(idx)
        
        queue = deque()
        queue.append( (0, 0) )

        vis = set()
        vis.add(0)

        while queue:
            idx, step = queue.popleft()
            if idx == size - 1:
                return step

            if idx + 1 < size and idx + 1 not in vis:
                vis.add(idx + 1)
                queue.append( (idx + 1, step + 1) )
                
            if idx - 1 >= 0 and idx - 1 not in vis:
                vis.add(idx - 1)
                queue.append( (idx - 1, step + 1))
            
            if arr[idx] in rcd:
                for jdx in rcd[arr[idx]]:
                    queue.append( (jdx, step + 1) )
                del rcd[arr[idx]]

        return -1