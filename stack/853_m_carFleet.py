class Solution:
    def carFleet(self, target, position, speed):

        pair = []
        stack = []
        
        
        for p,s in zip(position,speed):
            pair.append((p,s))

        pair.sort(reverse=True)

        for p,s in pair:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        res =len(stack)
        
        return res


