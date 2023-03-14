from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parents = [idx for idx in range(size)]
        self.ranks = [1 for _ in range(size)]

    def find(self, n):
        root = n
        while self.parents[root] != root:
            root = self.parents[root]
        
        cur = n
        while cur != root:
            nxt = self.parents[cur]
            self.parents[cur] = root
            cur = nxt
        
        return root

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return
        
        if self.ranks[p1] > self.ranks[p2]:
            self.ranks[p1] += self.ranks[p2]
            self.parents[p2] = p1
        else:
            self.ranks[p2] += self.ranks[p1]
            self.parents[p1] = p2

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        size = len(vals)
        union_find = UnionFind(size)

        rcd = defaultdict(list)
        for edge in edges:
            v1, v2 = edge
            # swap, make sure vals[v1] > vals[v2]
            if vals[v2] > vals[v1]:
                v1, v2 = v2, v1
            
            rcd[vals[v1]].append( (v1, v2) )

        vals_set = set(vals)
        sorted_vals = sorted(vals_set)

        val_to_indices = defaultdict(list)
        for idx, val in enumerate(vals):
            val_to_indices[val].append(idx)

        ret = 0

        for val in sorted_vals:
            for v1, v2 in rcd[val]:
                union_find.union(v1, v2)

            count = defaultdict(int)
            for idx in val_to_indices[val]:
                parent = union_find.find(idx)
                count[parent] += 1

            for parent, freq in count.items():
                ret += (freq * (freq - 1) // 2)
        
        return ret + size
