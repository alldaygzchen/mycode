class Solution:
    """
    subsequence might not be continous (against subarray)
    subsequence order matters (against subset)
    """
    def longestCommonSubsequence(self, text1, text2):
        
        self.s1 = text1
        self.s2 =text2
        self.N =len(self.s1)
        self.M =len(self.s2)
        self.cache = [[-1]*self.M for _ in range(self.N)]
        
        return self.dfs_postorder(0,0)

    def dfs_postorder(self,i1,i2):

        # put first since we do not want out of bounce
        if i1==len(self.s1) or i2==len(self.s2):
            return 0
        if self.cache[i1][i2]!=-1:
            return self.cache[i1][i2]
        
        if self.s1[i1] == self.s2[i2]:
            self.cache[i1][i2]= 1 + self.dfs_postorder(i1+1,i2+1)
        else:
            self.cache[i1][i2]= max(self.dfs_postorder(i1+1,i2),self.dfs_postorder(i1,i2+1))

        return self.cache[i1][i2]

text1 = ['A','D','C','B']   
text2 = ['A','B','C']       
s =Solution()
print(s.longestCommonSubsequence(text1,text2))
