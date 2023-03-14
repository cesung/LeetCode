from collections import defaultdict

class Solution:

    def dfs(self, node, parent):

        rcd = defaultdict(int)
        
        for neighbor in self.graph[node]:
            if neighbor == parent:
                continue

            children_rcd = self.dfs(neighbor, node)
            for label in range(ord('a'), ord('z') + 1):
                rcd[chr(label)] += children_rcd[chr(label)]
        
        rcd[self.labels[node]] += 1
        self.ret[node] = rcd[self.labels[node]]

        return rcd
            

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.labels = labels
        self.graph = defaultdict(list)

        for v1, v2 in edges:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
        
        self.ret = [0 for _ in range(n)]

        self.dfs(0, -1)

        return self.ret
