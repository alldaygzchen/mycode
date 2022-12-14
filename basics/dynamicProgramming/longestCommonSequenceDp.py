class Solution:
    """
    different solution: 
    dp => add foward to endpoint
    postorder => add backward to startpoint
    """
    def longestCommonSubsequenceDP(self, text1, text2):
        
        self.N = len(text1)
        self.M = len(text2)
        self.dp = [[0]*(self.M+1) for _ in range(self.N+1)]


        for i in range(self.N):
            for j in range(self.M):
                if text1[i]==text2[j]:
                    self.dp[i+1][j+1]=1+self.dp[i][j]
                else:
                    self.dp[i+1][j+1] = max(self.dp[i][j+1],self.dp[i+1][j])
        print(self.dp)
        return self.dp[self.N][self.M]

text1 = ['A','D','C','B']   
text2 = ['A','B','C']       
s =Solution()
print(s.longestCommonSubsequenceDP(text1,text2))
