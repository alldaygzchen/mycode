class Solution:
    def minDistance(self, word1, word2):
        self.w1 = word1
        self.w2 = word2
        self.cache = {}
        return self.dfs_postorder(0,0)

    def dfs_postorder(self,i,j):
        
        # base case
        if i == len(self.w1):
            return len(self.w2)-j

        if j == len(self.w2):
            return len(self.w1)-i

        if (i,j) in self.cache:
            return self.cache[(i,j)]


        # formula 
        if self.w1[i] == self.w2[j]:
            self.cache[(i,j)] = self.dfs_postorder(i+1,j+1)

        else:
            val  = min(self.dfs_postorder(i,j+1),self.dfs_postorder(i+1,j),self.dfs_postorder(i+1,j+1))
            self.cache[(i,j)] = 1+ val
        return self.cache[(i,j)]