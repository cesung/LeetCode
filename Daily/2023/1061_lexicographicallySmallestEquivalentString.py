from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parents = [idx for idx in range(26)]

    def find(self, ch):
        n = ord(ch) - ord('a')
        root = n
        while self.parents[root] != root:
            root = self.parents[root]
        
        cur = n
        while cur != root:
            nxt = self.parents[cur]
            self.parents[cur] = root
            cur = nxt
        
        return chr(root + ord('a'))
    
    def union(self, ch1, ch2):
        p1, p2 = self.find(ch1), self.find(ch2)
        if p1 == p2:
            return
        
        if p1 < p2:
            self.parents[ord(p2) - ord('a')] = ord(p1) - ord('a')
        else:
            self.parents[ord(p1) - ord('a')] = ord(p2) - ord('a')


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        s_size = len(s1)
        union_find = UnionFind()

        
        for idx in range(s_size):
            union_find.union(s1[idx], s2[idx])
        
        base_size = len(baseStr)
        ret = []
        for idx in range(base_size):
            ret.append(union_find.find(baseStr[idx]))
        
        return "".join(ret)
