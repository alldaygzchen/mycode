class Solution:
    """
    different solution: 
    dp => add foward to endpoint
    postorder => add backward to startpoint
    """
    def longestCommonSubsequenceDP(self, text1, text2):
        
        self.N = len(text1)
        self.M = len(text2)
        prevRow = [0]*(self.M+1)


        for i in range(self.N):
            curRow = [0]*(self.M+1)
            for j in range(self.M):
                if text1[i]==text2[j]:
                    curRow[j+1]=1+prevRow[j]
                else:
                    curRow[j+1] = max(prevRow[j+1],curRow[j])
        
            prevRow =curRow
        return prevRow[self.M]

text1 = ['A','D','C','B']   
text2 = ['A','B','C']       
s =Solution()
print(s.longestCommonSubsequenceDP(text1,text2))
