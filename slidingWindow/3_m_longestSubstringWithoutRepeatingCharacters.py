# trick
# delete duplicate
# remember it is a substring
class Solution:
    def lengthOfLongestSubstring(self, s):
        res =0
        char_set = set()
        l=0
        r=0
        
        while r<len(s):

            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1

            
            char_set.add(s[r])
            res = max(res,r-l+1)
            r+=1

        return res