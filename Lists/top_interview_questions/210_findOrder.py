class Solution:

    def bfs(self, root, edges, in_degree):

        queue = [root]
        order = []

        while queue:
            root = queue.pop(0)
            order.append(root)

            for nei in edges[root]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return order if len(order) == len(edges) else []

    # O(n) time | O(1) space
    def findOrder(self, numCourses, prerequisites):

        from collections import defaultdict

        edges = defaultdict(list, {cid:[] for cid in range(numCourses)})
        in_degree = defaultdict(int, {cid:0 for cid in range(numCourses)})

        for tar, src in prerequisites:
            in_degree[tar] += 1
            edges[src].append(tar)

        for cid in range(numCourses):
            if in_degree[cid] > 0:
                continue
            else:
                edges[numCourses].append(cid)
                in_degree[cid] += 1

        ans = self.bfs(numCourses, edges, in_degree)

        return ans[1:]
