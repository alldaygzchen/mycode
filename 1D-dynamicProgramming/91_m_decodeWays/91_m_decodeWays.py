class Solution:
    def numDecodings(self,s):
        self.s = s
        self.dp = [-1]* (len(s)+1)
        res =self.dfs_postorder(0)
        print(self.dp)
        return res

    def dfs_postorder(self,idx):
        
        #base case 
        if idx == len(self.s):
            print('idx',idx)
            self.dp[idx]=1
            return self.dp[idx]
        if idx>len(self.s):
            return 0

        if self.dp[idx]!=-1:
            return self.dp[idx]

        if self.s[idx] == "0":
            return 0

        
        #formula
        res = self.dfs_postorder(idx+1)
        if idx+1<len(self.s) and (self.s[idx] == "1" or self.s[idx]=="2" and self.s[idx+1] in "0123456"):
            res+=self.dfs_postorder(idx+2)

        self.dp[idx] = res
        return res
        
