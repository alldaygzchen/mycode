    #         []
    #     a             aa      aab(X)   
    # a       ab(x)

#self.pali and dfs see as horizontal
# part see as vertical



class Solution:
    def partition(self, s):
        self.res = [] 
        self.s = s
        self.dfs(0,[])
        return self.res

    def dfs(self,idx,part):
        
        if idx>=len(self.s):
            self.res.append(part[:])
            return 

        for j in range(idx,len(self.s)):
            if self.isPali(self.s, idx, j):
                part.append(self.s[idx:j+1])
                self.dfs(j+1,part)
                part.pop()

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True