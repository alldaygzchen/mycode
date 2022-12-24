class Solution:
    def uniquePaths(self, m: int, n: int):
        
        self.dp = [[None for c in range(n)] for r in range(m)]

        for c in range(n):
            self.dp[-1][c] = 1

        for r in range(m):
            self.dp[r][-1] = 1

        for r in range(m-2,-1,-1):
            for c in range(n-2,-1,-1):
                self.dp[r][c] = self.dp[r+1][c] + self.dp[r][c+1]

        return self.dp[0][0]

