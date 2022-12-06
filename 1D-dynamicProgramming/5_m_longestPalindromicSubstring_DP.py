class Solution:
    def longestPalindrome(self, s):

        self.max = float("-inf")
        self.res = None
        
        
        for i in range(len(s)):
            
            # odd situation
            l,r=i,i

            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>self.max:
                    self.res = s[l:r+1]
                    self.max = r-l+1
                l-=1
                r+=1

                
            # even situation
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>self.max:
                    self.res = s[l:r+1]
                    self.max = r-l+1
                l-=1
                r+=1

        return self.res
        
s =Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))