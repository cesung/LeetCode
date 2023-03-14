"""
Iterative
"""
class Solution:

    def is_valid(self, s, left, right):
        sec, val = s[left : right], -1 if not s[left : right] else int(s[left : right])

        return False if (
            val == -1 or
            val == 0 and len(sec) != 1 or
            val != 0 and sec[0] == '0' or
            val > 255
        ) else True

    def restoreIpAddresses(self, s: str) -> List[str]:
        size = len(s)
        ret = []

        for idx in range(1, 3 + 1):
            if not self.is_valid(s, 0, idx):
                continue
            for jdx in range(idx + 1, idx + 3 + 1):
                if not self.is_valid(s, idx, jdx):
                    continue
                for kdx in range(jdx + 1, jdx + 3 + 1):
                    if not self.is_valid(s, jdx, kdx):
                        continue
                    if not self.is_valid(s, kdx, size):
                        continue

                    ret.append(".".join(
                            [
                                s[:idx],
                                s[idx:jdx],
                                s[jdx:kdx],
                                s[kdx:],
                            ]
                        )
                    )

        return ret

"""
Backtracking
"""
class Solution2:

    def is_valid(self, sec, val):
        return False if (
            val == 0 and len(sec) != 1 or
            val != 0 and sec[0] == '0' or
            val > 255
        ) else True

    def dfs(self, idx, num_dots, ip_address):
        if (
            idx == self.size and
            num_dots == 3 + 1
        ):
            self.ret.append(ip_address[:-1])
            return
        
        for jdx in range(idx, min(idx + 3, self.size)):
            sec, val = self.s[idx:jdx + 1], int(self.s[idx:jdx + 1])
            if self.is_valid(sec, val):
                self.dfs(jdx + 1, num_dots + 1, ip_address + self.s[idx:jdx + 1] + '.')

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.size = len(s)
        self.s = s
        self.ret = []

        self.dfs(0, 0, "")

        return self.ret
