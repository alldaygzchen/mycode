class Solution:
    def longest(self,s):
        
        length = float("-inf")

        for i in range(len(s)):

            # odd solutions:
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                length = max(length,r-l+1)
                l-=1
                r+=1

            # even solutions:
            l,r =i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                length = max(length,r-l+1)
                l-=1
                r+=1

        return length

s =Solution()
print(s.longest(['a','b','a','a','b']))