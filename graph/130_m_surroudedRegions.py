
# Find surrounded regions from the borders with DFS =>marked as E
# Run through every cell=> marked as X
# Run through every cell and if self.visit() = >mark O



class Solution:
    def solve(self, board):

        self.board = board 
        self.rows = len(board)
        self.cols = len(board[0])
        # self.visit = set()

        for c in range(self.cols):
            self.dfs_preorder(0,c)

        for c in range(self.cols):
            self.dfs_preorder(self.rows-1,c)

        for r in range(self.rows):
            self.dfs_preorder(r,0)

        for r in range(self.rows):
            self.dfs_preorder(r,self.cols-1)


        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c]=="E":
                    self.board[r][c] = "O"
                else:
                    self.board[r][c] = "X"

        return self.board


    def dfs_preorder(self,r,c):
        # base case
        if r<0 or c<0 or r==self.rows or c == self.cols or self.board[r][c]!="O":
            return
        # formula
        self.board[r][c] = "E"
        self.dfs_preorder(r+1,c)
        self.dfs_preorder(r-1,c)
        self.dfs_preorder(r,c+1)
        self.dfs_preorder(r,c-1)






