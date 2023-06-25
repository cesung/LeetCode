from typing import *


class Solution:
    def dfs(self, cur, fuel):
        if fuel < 0:
            return 0
        
        if self.dp[cur][fuel] != -1:
            return self.dp[cur][fuel]
        
        cnt = 0
        if cur == self.finish:
            cnt += 1
        
        for nxt in range(self.n):
            if nxt == cur:
                continue
            cost = abs(self.locations[cur] - self.locations[nxt])
            cnt = (cnt + self.dfs(nxt, fuel - cost)) % self.MOD
        
        self.dp[cur][fuel] = cnt
        return self.dp[cur][fuel]

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        self.MOD = 10**9 + 7

        self.finish = finish
        self.locations = locations

        self.n = len(locations)
        # dp[idx][jdx]: how many possible routes from {idx} city to {finish} city with jdx remaining fuel
        self.dp = [[-1 for _ in range(fuel + 1)] for _ in range(self.n)]

        return self.dfs(start, fuel)