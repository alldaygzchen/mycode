class Solution:


    def wordBreak(self, s, wordDict):
        
        dp = [False]*(len(s)+1)
        dp[-1] =True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] =dp[i + len(w)]
                if dp[i]:
                    break


        return dp[0]

        
    

s = Solution()
print(s.wordBreak("leetcode",["leet","code"]))
print(s.wordBreak("applepenapple",["apple","pen"]))
print(s.wordBreak("catsandog",["cats","dog","sand","and","cat"]))