from collections import defaultdict

class Solution:

    def get_encoding(self, cntr):
        return ",".join(map(str, cntr))

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_size, s2_size = len(s1), len(s2)

        if s1_size > s2_size:
            return False

        s1_cntr = [0 for _ in range(26)]
        for idx in range(s1_size):
            s1_cntr[ord(s1[idx]) - ord('a')] += 1
        
        s2_cntr = [0 for _ in range(26)]
        for idx in range(s1_size):
            s2_cntr[ord(s2[idx]) - ord('a')] += 1

        s1_encoding = self.get_encoding(s1_cntr)
        if s1_encoding == self.get_encoding(s2_cntr):
            return True

        for idx in range(s1_size, s2_size):
            s2_cntr[ord(s2[idx - s1_size]) - ord('a')] -= 1
            s2_cntr[ord(s2[idx]) - ord('a')] += 1
            if s1_encoding == self.get_encoding(s2_cntr):
                return True

        return False
