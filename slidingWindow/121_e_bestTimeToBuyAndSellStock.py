




class Solution:
    def maxProfit(self, prices):
        result = 0
        l = 0
        r = 0
        while r<len(prices):
            print(l,r)
            if prices[l]>prices[r]:
                l =r
                r+=1
                continue
            result = max(result,prices[r]-prices[l])
            r+=1

        return result 
prices = [2,6,1,3]
s= Solution()
print(s.maxProfit(prices))


# class Solution:
#     def maxProfit(self, prices):
#         result = float("-inf")
#         s = 0

#         while s<len(prices)-1:
#             e = s 
#             while e<len(prices):
#                 print(s,e)
#                 result =max(result,prices[e]-prices[s])
#                 e+=1
#             s+=1

#         return result