class Solution:

    from collections import defaultdict

    def dfs(self, cid, edges, vis, in_stack):
        vis[cid], in_stack[cid] = True, True

        suc = True
        for nei in edges[cid]:

            if in_stack[nei]:
                return False

            elif vis[nei]:
                continue

            else:
                suc &= self.dfs(nei, edges, vis, in_stack)

        in_stack[cid] = False
        return suc

    # O(n) time | O(1) space
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        for post, prev in prerequisites:
            edges[prev].append(post)

        vis = [False for cid in range(numCourses)]
        in_stack = [False for cid in range(numCourses)]

        for cid in range(numCourses):
            if vis[cid]:
                continue
            if not self.dfs(cid, edges, vis, in_stack):
                return False

        return True
