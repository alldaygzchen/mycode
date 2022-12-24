class Solution:
    """
    Compare 746 vs 1143
    For formula pruning:  
    Only added if occur neccesary, otherwise optimal solution can consider the base case for simplicity 
    """
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text1 = text1
        self.text2 = text2
        self.cache = [[-1]*len(self.text2) for _ in range(len(self.text1))]
        return self.dfs_postorder(0,0)
    def dfs_postorder(self,idx1,idx2):
        
        # # base case 
        if idx1==len(self.text1) or idx2==len(self.text2):
            return 0

        if self.cache[idx1][idx2]!=-1:
            return self.cache[idx1][idx2]

        # formula
        if self.text1[idx1] == self.text2[idx2]:
            self.cache[idx1][idx2] = 1+ self.dfs_postorder(idx1+1,idx2+1)
            return self.cache[idx1][idx2]
        else:
            self.cache[idx1][idx2] = max(self.dfs_postorder(idx1+1,idx2),self.dfs_postorder(idx1,idx2+1))
            return self.cache[idx1][idx2]


# class Solution:
    
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         self.text1 = text1
#         self.text2 = text2
#         self.cache = [[-1]*len(self.text2) for _ in range(len(self.text1))]
#         return self.dfs_postorder(0,0)
#     def dfs_postorder(self,idx1,idx2):
        

#         if self.cache[idx1][idx2]!=-1:
#             return self.cache[idx1][idx2]

#         # formula
#         if self.text1[idx1] == self.text2[idx2]:
#             if idx1+1==len(self.text1) or idx2+1==len(self.text2):
#                 return 1

#             self.cache[idx1][idx2] = 1+ self.dfs_postorder(idx1+1,idx2+1)
#             return self.cache[idx1][idx2]        
        
#         else:
#             if idx1+1==len(self.text1) and idx2+1==len(self.text2):
#                 return 0
#             elif idx1+1==len(self.text1):
#                 self.cache[idx1][idx2] = self.dfs_postorder(idx1,idx2+1)
#                 return self.cache[idx1][idx2]
#             elif idx2+1==len(self.text2):
#                 self.cache[idx1][idx2] = self.dfs_postorder(idx1+1,idx2)
#                 return self.cache[idx1][idx2]

#             self.cache[idx1][idx2] = max(self.dfs_postorder(idx1+1,idx2), self.dfs_postorder(idx1,idx2+1))
#             return self.cache[idx1][idx2]