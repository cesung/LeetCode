from collections import deque

class Solution:
    def distinctIntegers(self, n: int) -> int:
        vis = set()
        vis.add(n)
        queue = deque()
        queue.append(n)
        
        while queue:
            num = queue.popleft()
            for val in range(2, num + 1):
                if num % val == 1 and val not in vis:
                    vis.add(val)
                    queue.append(val)
        
        return len(vis)
