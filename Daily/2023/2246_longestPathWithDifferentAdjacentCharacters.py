from collections import defaultdict

class Solution:

    def dfs(self, node):
        pool = []
        for child in self.graph[node]:
            ret_child = self.dfs(child)
            pool.append(
                ret_child
                if self.s[child] != self.s[node] 
                else 0
            )

        if not pool:
            return 1
        
        pool.sort(key = lambda x : -x)

        if len(pool) > 1:
            self.ret = max(
                self.ret,
                pool[0] + pool[1] + 1,
            )
        else:
            self.ret = max(
                self.ret,
                pool[0] + 1,
            )

        return pool[0] + 1

    def longestPath(self, parents: List[int], s: str) -> int:
        self.size = len(parents)
        self.s = s
        self.graph = defaultdict(list)
        for node, parent in enumerate(parents):
            if parent == -1:
                continue
            self.graph[parent].append(node)
        
        
        self.ret = 1
        self.dfs(0)
    
        return self.ret
