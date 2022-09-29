
class Solution:
    def carFleet(self, target, position, speed):

        stack = []
        pair = []

        for p,s in zip(position,speed):
            pair.append((p,s))

        pair.sort()

        for p,s in pair:
            while stack and stack[-1]<=(target-p)/s:
                stack.pop()

            stack.append((target-p)/s)

        res = len(stack)
        # print(stack)


        return res

s = Solution()
s.carFleet(12,[10,8,0,5,3],[2,4,1,1,3])

# class Solution:
#     def carFleet(self, target, position, speed):

#         pair = []
#         stack = []
        
        
#         for p,s in zip(position,speed):
#             pair.append((p,s))

#         pair.sort(reverse=True)

#         for p,s in pair:
#             stack.append((target-p)/s)
#             if len(stack)>=2 and stack[-1]<=stack[-2]:
#                 stack.pop()

#         res =len(stack)
#         print(stack)
        
#         return res

# s = Solution()
# s.carFleet(12,[10,8,0,5,3],[2,4,1,1,3])
