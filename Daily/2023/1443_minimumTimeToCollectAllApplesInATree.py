from collections import defaultdict

class Solution:

    def dfs(self, root, parent):
        ttl_t = 0
        for children in self.graph[root]:
            if children == parent:
                continue

            children_t = self.dfs(children, root)

            if children_t or self.has_apple[children]:
                ttl_t += children_t + 2
        
        return ttl_t


    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.graph = defaultdict(list)
        self.has_apple = hasApple

        for v1, v2 in edges:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
        
        return self.dfs(0, -1)
