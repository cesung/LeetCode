from collections import defaultdict, deque

class Solution:

    def bfs(self, node):
        rcd = defaultdict(int)
        queue = deque()
        queue.append( (node, 0) )

        while queue:
            node, step = queue.popleft()
            rcd[node] = step

            for neighbor in self.graph[node]:
                if neighbor in rcd:
                    continue
                queue.append( (neighbor, step + 1) )
        
        return rcd

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        INF = float('inf')
        size = len(edges)
        self.graph = defaultdict(list)
        for src, tar in enumerate(edges):
            if tar == -1:
                continue
            self.graph[src].append(tar)

        rcd1 = self.bfs(node1)
        rcd2 = self.bfs(node2)

        min_dist = INF
        min_dist_node = -1
        for node in range(size):
            if node in rcd1 and node in rcd2:
                dist = max(rcd1[node], rcd2[node])
                if min_dist > dist:
                    min_dist = dist
                    min_dist_node = node
        
        return min_dist_node
