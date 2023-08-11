from typing import *
from collections import defaultdict, deque

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = defaultdict(list)
        for _pid, _ppid in zip(pid, ppid):
            graph[_ppid].append(_pid)
        
        ret = []
        queue = deque()
        queue.append(kill)
        
        while queue:
            node = queue.popleft()
            ret.append(node)
            
            for child in graph[node]:
                queue.append(child)
        
        return ret