class Solution:

    """
        leetcode
    leet        code

    code

    """

    def wordBreak(self, s, wordDict):
        self.s = s
        self.wordDict = wordDict
        self.cache = [None]*(len(s)+1)
        return self.dfs_postorder(0)

    def dfs_postorder(self,idx):
        
        # base case
        if idx == len(self.s):
            self.cache[-1] =True
            return self.cache[-1]

        if self.cache[idx] is not None:
            return self.cache[idx]
        

        # formula
        for w in self.wordDict:
            if len(w)+idx<=len(self.s) and self.s[idx:len(w)+idx] == w:
                if self.dfs_postorder(len(w)+idx):
                    self.cache[idx] = True 
                    return self.cache[idx]

        self.cache[idx] = False
        return self.cache[idx]
        
    

s = Solution()
print(s.wordBreak("cars",["car","ca","rs"]))
print(s.wordBreak("applepenapple",["apple","pen"]))
print(s.wordBreak("catsandog",["cats","dog","sand","and","cat"]))