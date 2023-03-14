class Solution:

    # O(n*m) time | O(n*m) space
    # Buttom-up DP
    def uniquePaths(self, m: int, n: int) -> int:
        # create m*n matrix
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # initialization
        for _ in range(m):
            dp[_][0] = 1
        for _ in range(n):
            dp[0][_] = 1

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]

class Solution2:

    def __init__(self):
        self.dp = defaultdict(int)

    def factorial(self, n):
        if n in self.dp:
            return self.dp[n]

        if n == 0 or n == 1:
            return 1

        self.dp[n] = n * self.factorial(n - 1)

        return self.dp[n]

    # O(n+m) time | O(n+m) space
    # Math
    def uniquePaths(self, m: int, n: int) -> int:
        return self.factorial(m-1 + n-1) // self.factorial(m - 1) // self.factorial(n - 1)

