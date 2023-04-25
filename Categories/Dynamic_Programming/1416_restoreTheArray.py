class Solution:
    def dfs(self, idx):
        if idx == self.size:
            return 1
        if self.s[idx] == '0':
            return 0
        if idx in self.rcd:
            return self.rcd[idx]

        val, cnt = 0, 0
        for jdx in range(idx, self.size):
            val *= 10
            val += int(self.s[jdx])

            if val > self.k:
                break

            cnt = (cnt + self.dfs(jdx + 1)) % self.MOD
        
        self.rcd[idx] = cnt

        return self.rcd[idx]

    def numberOfArrays(self, s: str, k: int) -> int:
        self.MOD = 10**9 + 7
        self.s = s
        self.k = k
        self.size = len(s)

        # s[idx:]
        self.rcd = defaultdict(int)

        return self.dfs(0)