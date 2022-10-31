
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord =False

    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.isWord = True

class Solution:

    def findWords(self,board,words):# output list

        root =TrieNode()
        for w in words:
            root.addWord(w)

        self.rows = len(board)
        self.cols = len(board[0])

        self.res = set()
        self.visit = set()
        self.board =board

        for r in range(self.rows):
            for c in range(self.cols):
                self.helper(r, c, root,'')


        return list(self.res)

    def helper(self,r,c,node,word): #

        if (r<0 or c<0 or r>=self.rows or c>=self.cols or self.board[r][c] not in node.children or (r,c) in self.visit): #prevent duplicate
            return
        
        self.visit.add((r, c))
        node = node.children[self.board[r][c]]
        word += self.board[r][c]
        if node.isWord:
            self.res.add(word)

        self.helper(r + 1, c, node, word) # not postorder
        self.helper(r - 1, c, node, word)
        self.helper(r, c + 1, node, word)
        self.helper(r, c - 1, node, word)
        self.visit.remove((r, c))