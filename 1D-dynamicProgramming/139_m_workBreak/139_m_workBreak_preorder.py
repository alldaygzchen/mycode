class Solution:

    def wordBreak(self, s, wordDict):
        self.s = s
        self.wordDict = wordDict
        self.res =False
        self.dfs_preorder(0)
        return self.res

    def dfs_preorder(self,idx):  
        # base case
        if idx == len(self.s):
            self.res =True

        # formula
        for w in self.wordDict:
            if len(w)+idx<=len(self.s) and self.s[idx:len(w)+idx] == w:
                self.dfs_preorder(len(w)+idx)