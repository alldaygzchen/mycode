class Solution:
    def encode(self,strs):
        result=''

        for e in strs:
            result+=str(len(e))
            result+='*'
            result+=e

        return result


    def decode(self,strs):
        result =''
        i=0
        
        while i<len(strs):
            symbol_idx =strs.find('*',i)
            numbers_range = strs[i:symbol_idx]
            string_range = strs[symbol_idx+1:symbol_idx+1+len(numbers_range)]
            result+=string_range
            i = symbol_idx+1+len(numbers_range)


        return result

s = Solution()
print(s.encode('judy'))
print(s.decode('1*j1*u1*d1*y'))