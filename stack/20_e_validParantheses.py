class Solution:
    def isValid(self, s):


        s_map = {"(":")","{":"}","[":"]"}
        stack = []

        for e in s:
            if e in s_map:
                stack.append(s_map[e])
            else:
                if e == stack[-1]:
                    stack.pop()
                else:
                    return False

        return True


s= Solution()
print(s.isValid("()"))
