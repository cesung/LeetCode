class Solution:
    def get_encoding(self, cntr):
        return ",".join(map(str, cntr))

    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_size, p_size = len(s), len(p)
        if p_size > s_size:
            return []
        
        p_cntr = [0 for _ in range(26)]
        for idx in range(p_size):
            p_cntr[ ord(p[idx]) - ord('a') ] += 1
        p_encoding = self.get_encoding(p_cntr)

        s_cntr = [0 for _ in range(26)]
        for idx in range(p_size):
            s_cntr[ ord(s[idx]) - ord('a') ] += 1
        
        ret = []
        if self.get_encoding(s_cntr) == p_encoding:
            ret.append(0)

        for idx in range(p_size, s_size):
            s_cntr[ ord(s[idx]) - ord('a') ] += 1
            s_cntr[ ord(s[idx - p_size]) - ord('a') ] -= 1
            s_encoding = self.get_encoding(s_cntr)
        
            if s_encoding == p_encoding:
                ret.append(idx - p_size + 1)
        
        return ret
