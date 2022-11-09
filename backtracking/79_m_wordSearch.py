# i think we are going to use preorder recursion

# edge case: satisfies the word or length smaller than th word (prevent time execution)
# every cell should have to be the starting point connected with four different directions 

# class Solution:
#     def exist(self, board, word):
#         self.res = None
#         self.word = word
#         self.board = board
#         self.rows = len(board)
#         self.cols = len(board[0])
#         self.path =set()

#         for r in range(self.rows):
#             for c in range(self.cols):
#                 if self.board[r][c] == self.word[0]:
#                     if self.helper(r, c, 0):
#                         return True
#         return False

#     def helper(self,r,c,idx):

#         if idx == len(self.word):
#             return True
#         if (r<0 or c<0 or r>=self.rows or c>=self.cols or self.word[idx]!= self.board[r][c] or (r,c) in self.path):
#             return False
#         self.path.add((r,c))
#         self.res = (
#             self.helper(r + 1, c, idx + 1)
#                 or self.helper(r - 1, c, idx + 1)
#                 or self.helper(r, c + 1, idx + 1)
#                 or self.helper(r, c - 1, idx + 1)
#         )
#         self.path.remove((r,c))
#         return self.res 

from collections import Counter
from collections import defaultdict
class Solution:
    def exist(self, board, word):
        self.res = None

        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]


        self.word = word
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        path =set()

        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == self.word[0]:
                    if self.helper(r, c, 0,path):
                        return True
        return False

    def helper(self,r,c,idx,path):

        if idx == len(self.word):
            return True
        if (r<0 or c<0 or r>=self.rows or c>=self.cols or self.word[idx]!= self.board[r][c] or (r,c) in path):
            return False
        path.add((r,c))
        self.res = (
            self.helper(r + 1, c, idx + 1,path)
                or self.helper(r - 1, c, idx + 1,path)
                or self.helper(r, c + 1, idx + 1,path)
                or self.helper(r, c - 1, idx + 1,path)
        )
        path.remove((r,c))
        return self.res 