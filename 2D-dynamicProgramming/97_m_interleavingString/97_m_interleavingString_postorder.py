class Solution(object):
    
    def isInterleave(self, s1, s2, s3):
        self.s1 =s1
        self.s2 =s2
        self.s3 =s3
        if len(s1)+len(s2)!=len(s3):
            return False
        self.cache = {}
        return self.dfs_postorder(0,0)
    
    def dfs_postorder(self,i,j):
        if i == len(self.s1) and j ==len(self.s2):
            return True
        if (i,j) in self.cache:
            return self.cache[(i,j)]

        if i<len(self.s1) and self.s1[i] == self.s3[i+j]:
            if self.dfs_postorder(i+1,j):
                self.cache[(i+1,j)] = True
                return self.cache[(i+1,j)] 

        if j<len(self.s2) and self.s2[j] == self.s3[i+j]:
            if self.dfs_postorder(i,j+1):
                self.cache[(i,j+1)] =True
                return self.cache[(i,j+1)]

        self.cache[(i,j)] = False
        return self.cache[(i,j)]
        