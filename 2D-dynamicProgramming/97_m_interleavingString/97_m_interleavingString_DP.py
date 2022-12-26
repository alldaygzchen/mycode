class Solution(object):
    
    def isInterleave(self, s1, s2, s3):
        
        if len(s1) +len(s2) != len(s3):
            return False

        dp = [[None]*(len(s2)+1) for i in range(len(s1)+1)]
        
        dp[len(s1)][len(s2)] = True
        
        for j in range(len(s2)-1,-1,-1):
            if s2[j]==s3[len(s1)+j]:
                if dp[len(s1)][j+1]:
                    dp[len(s1)][j] = True
                else:
                    dp[len(s1)][j] = False
            else:
                dp[len(s1)][j] = False

        for i in range(len(s1)-1,-1,-1):
            if s1[i]==s3[len(s2)+i]:
                if dp[i+1][len(s2)]:
                    dp[i][len(s2)]= True
                else:
                    dp[i][len(s2)] = False

            else:
                dp[i][len(s2)] = False

        for i in range(len(s1)-1,-1,-1):
            for j in range(len(s2)-1,-1,-1):
                if s1[i] == s3[i+j]:
                    if dp[i+1][j]:
                        dp[i][j]= True
                        continue
                if s2[j] == s3[i+j]:
                    if dp[i][j+1]:
                        dp[i][j] = True
                        continue
                
                dp[i][j] = False

        return dp[0][0]



