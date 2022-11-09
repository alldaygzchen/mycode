#   []

#   a  b  c

# def def  def



class Solution:
    def letterCombinations(self, digits):
        self.res = []
        self.digits = digits
        self.digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",            
        }
        if digits:
            self.helper(0,"")
        return self.res

    def helper(self,idx,curStr):
        
        if len(curStr) == len(self.digits):
            self.res.append(curStr)
            return

        for c in self.digitToChar[self.digits[idx]]:
            self.helper(idx+1,curStr+c)
