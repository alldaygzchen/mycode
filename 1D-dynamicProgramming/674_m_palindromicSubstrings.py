class Solution:
    def countSubstrings(self, s):

        self.count = 0
        
        
        for i in range(len(s)):
            
            # odd situation
            l,r=i,i

            while l>=0 and r<len(s) and s[l]==s[r]:
                self.count+=1
                l-=1
                r+=1

                
            # even situation
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                self.count+=1
                l-=1
                r+=1

        return self.count
        
s =Solution()
print(s.countSubstrings("abc"))
print(s.countSubstrings("aaa"))