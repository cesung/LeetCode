class Solution:
    def dfs(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 2
        
        if n in self.dp:
            return self.dp[n]
        
        self.dp[n] = (self.dfs(n // 2) * self.dfs(n // 2) ) % self.MOD
        if n % 2 == 1:
            self.dp[n] = (self.dp[n] * 2) % self.MOD

        return self.dp[n]
        
    
    def monkeyMove(self, n: int) -> int:
        self.MOD = 10**9 + 7
        self.dp = defaultdict(int)
        
        return (self.dfs(n) - 2) % self.MOD
