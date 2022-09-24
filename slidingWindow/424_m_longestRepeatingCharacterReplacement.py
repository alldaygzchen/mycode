# trick
class Solution:
    def characterReplacement(self, s, k):

        res = 0
        l=0
        r=0
        char_dict = dict()

        while r<len(s):
            
            if s[r] in char_dict:
                char_dict[s[r]]+=1
            else:
                char_dict[s[r]]=1


            while (r-l+1)-max(char_dict.values())>k:
                char_dict[s[l]]-=1
                l+=1



            res = max(res,r-l+1)
            r+=1

        return res


s= Solution()
print(s.characterReplacement("ABAB",2))


