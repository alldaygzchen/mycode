class Solution:
    def evalRPN(self, tokens):

        res = None
        stack = []

        for token in tokens:

            if token == "+":
                b=stack.pop()
                a= stack.pop()
                stack.append(a+b)

            elif token == "-":
                b=stack.pop()
                a= stack.pop()
                stack.append(a-b)

            elif token == "*":
                b=stack.pop()
                a= stack.pop()
                stack.append(a*b)

            elif token == "/":
                b=stack.pop()
                a= stack.pop()
                stack.append(a/b)

            else:
                stack.append(token)



        res = stack[0]
        return res