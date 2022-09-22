# trick
# clean string 

class Solution:

    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

    def isPalindrome(self, s):

        result =False
        
        new_s=""
        for e in s:
            if self.alphanum(e):
                new_s+=e.lower()

        l = 0 
        r = len(new_s)-1

        

        while l<r:
            
            if new_s[l]!=new_s[r]:
                return result

            l+=1
            r-=1

        result = True
        return result
