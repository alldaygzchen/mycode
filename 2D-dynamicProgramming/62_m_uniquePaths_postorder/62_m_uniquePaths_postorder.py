



class Solution:
    def uniquePaths(self, m: int, n: int):
        self.cache = [[-1]*n for i in range(m)]
        self.rows = m
        self.cols = n
        return self.dfs_postorder(0,0)


    def dfs_postorder(self,r,c):


        if r>=self.rows or c>=self.cols:
            return 0

        if r==self.rows-1 and c==self.cols-1:
            self.cache[r][c]=1
            return self.cache[r][c]

        if self.cache[r][c]!=-1:
            return self.cache[r][c]

        self.cache[r][c]=self.dfs_postorder(r+1,c) +self.dfs_postorder(r,c+1)
        return self.cache[r][c]


# class Solution:
#     def uniquePaths(self, m: int, n: int):
#         self.cache = [[-1]*n for i in range(m)]
#         self.rows = m
#         self.cols = n
#         return self.dfs_postorder(0,0)


#     def dfs_postorder(self,r,c):

#         if r==self.rows-1 and c==self.cols-1:
#             self.cache[r][c]=1
#             return self.cache[r][c]
 
#         if self.cache[r][c]!=-1:
#             return self.cache[r][c]

#         if r+1>=self.rows:
#             self.cache[r][c]=self.dfs_postorder(r,c+1)
#             return self.cache[r][c]

#         if c+1>=self.cols:
#             self.cache[r][c]=self.dfs_postorder(r+1,c)
#             return self.cache[r][c]

#         self.cache[r][c]=self.dfs_postorder(r+1,c) +self.dfs_postorder(r,c+1)
#         return self.cache[r][c]

        