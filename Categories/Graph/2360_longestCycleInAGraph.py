from collections import defaultdict

class Solution:
    def dfs(self, node):
        self.vis.add(node)
        neighbor = self.edges[node]

        # neighbor not exist
        if neighbor == -1:
            return
            
        # visit the neighbor twice in the current traversal
        if neighbor in self.path:
            self.longest_cycle_length = max(
                self.longest_cycle_length,
                self.path[node] - self.path[neighbor] + 1,
            )
            return
        
        # visit the neighbor which hasn't visited before
        if neighbor not in self.vis:
            self.path[neighbor] = self.path[node] + 1
            self.dfs(neighbor)

    def longestCycle(self, edges: List[int]) -> int:
        self.vis = set()
        self.edges = edges
        self.longest_cycle_length = -1

        for node in range(len(edges)):
            if node not in self.vis:
                self.path = defaultdict(int)
                self.dfs(node)

        return self.longest_cycle_length