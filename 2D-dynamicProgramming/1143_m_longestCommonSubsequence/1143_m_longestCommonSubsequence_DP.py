class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        self.text1 = text1
        self.text2 = text2
        self.len1= len(text1)
        self.len2 =len(text2)
        self.dp = [[None]*(self.len2+1) for _ in range(self.len1+1)]

        for c in range(self.len2+1):
            self.dp[-1][c] = 0

        for r in range(self.len1+1):
            self.dp[r][-1] = 0

        for r in range(self.len1-1,-1,-1):
            for c in range(self.len2-1,-1,-1):
                if self.text1[r] == self.text2[c]:
                    self.dp[r][c] = 1+self.dp[r+1][c+1]
                else:
                    self.dp[r][c] = max(self.dp[r+1][c],self.dp[r][c+1])



        return self.dp[0][0]