class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self,word):

        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.word =True

    def search(self,word):
        self.word = word
        return self.helper(0,self.root)


    def helper(self,j,root):

        cur = root

        for i in range(j,len(self.word)):

            c= self.word[i]

            if c==".":
                for child in cur.children.values():#values #next
                    if self.helper(i+1,child):
                        return True
                return False

            else:
                if c not in cur.children:#check entrance
                    return False
                cur = cur.children[c] #next

        return cur.word

        



    






