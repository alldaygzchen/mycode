class Solution:
    def solveNQueens(self, n) :

        colSet= set()
        posDiagSet =set() #r+c
        negDiagSet =set() #r-c
        self.len =n
        self.res =[]
        self.board = [["."]*n for i in range(n)]
        self.helper(0,colSet,posDiagSet,negDiagSet)
        return self.res

    def helper(self,r,colSet,posDiagSet,negDiagSet): #modify self.board

        if r==self.len:
            copy = ["".join(row) for row in self.board]
            self.res.append(copy)
            return 
        
        for c in range(self.len):
            if c in colSet or (r+c) in posDiagSet or (r-c) in negDiagSet:
                continue

            colSet.add(c)
            posDiagSet.add(r+c)
            negDiagSet.add(r-c)
            self.board[r][c] = "Q"

            self.helper(r+1,colSet,posDiagSet,negDiagSet)

            colSet.remove(c)
            posDiagSet.remove(r+c)
            negDiagSet.remove(r - c)
            self.board[r][c] = "."