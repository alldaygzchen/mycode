
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord =False
        self.refs = 0

    def addWord(self,word):
        curr = self
        curr.refs += 1
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.refs += 1

        curr.isWord = True

    def removeWord(self, word):
            cur = self
            cur.refs -= 1
            for c in word:
                if c in cur.children:
                    cur = cur.children[c]
                    cur.refs -= 1

class Solution:

    def findWords(self,board,words):# output list

        self.root =TrieNode()
        for w in words:
            self.root.addWord(w)

        self.rows = len(board)
        self.cols = len(board[0])

        self.res = set()
        self.visit = set()
        self.board =board

        for r in range(self.rows):
            for c in range(self.cols):
                self.helper(r, c, self.root,'')


        return list(self.res)

    def helper(self,r,c,node,word): #

        if (r<0 or c<0 or r>=self.rows or c>=self.cols or self.board[r][c] not in node.children or node.children[self.board[r][c]].refs < 1 or (r,c) in self.visit): #prevent duplicate
            return
        
        self.visit.add((r, c))
        node = node.children[self.board[r][c]]
        word += self.board[r][c]
        if node.isWord:
            self.res.add(word)
            node.isWord = False
            self.root.removeWord(word) #prevent same word  it removes all characters of the input word from the prefix tree that are not used to store other words.


        self.helper(r + 1, c, node, word) # not postorder
        self.helper(r - 1, c, node, word)
        self.helper(r, c + 1, node, word)
        self.helper(r, c - 1, node, word)
        self.visit.remove((r, c))