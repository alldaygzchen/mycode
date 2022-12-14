class Solution:

    "dp = min coin to the objective"

    def coinChange(self, coins, amount):
        dp  = [float('inf')]*(amount+1)
        dp[0] = 0
        
        for a in range(1,amount+1):
                for c in coins:
                    if a-c>=0:
                        dp[a] = min(dp[a], 1 + dp[a - c])


        if dp[amount] == float('inf'):
            return -1
        return dp[amount]

# class Solution:

#     "dp = min coin to the objective"

#     def coinChange(self, coins, amount):

#         if amount==0:
#             return 0

#         dp  = [float('inf')]*(amount)
        
#         for i in range(amount):
#             if i+1 in coins:
#                 dp[i] = 1
#         for a in range(amount):
#             print(a)
#             if dp[a]!=1:
#                 for c in coins:
#                     if a+1-c>0:
#                         dp[a] = min(dp[a], 1 + dp[a - c])

#         if dp[amount-1] == float('inf'):
#             return -1
        
#         return dp[amount-1]




# class Solution:

#     '''dp = min coin to the objective'''

#     def coinChange(self, coins, amount):

#         if amount==0:
#             return 0

#         amounts = [ i+1 for i in range(amount)]
#         dp  = [float('inf')]*len(amounts)
        
#         for idx,a in enumerate(amounts):
#             if a in coins:
#                 dp[idx] = 1


#         for i in range(len(amounts)):
#             if dp[i]!=1:
#                 for c in coins:
#                     if amounts[i]-c>0:
#                         dp[i] = min(dp[i], 1 + dp[amounts[i]-c-1])

#         if dp[amount-1] == float('inf'):
#             return -1
        
#         return dp[amount-1]

s = Solution()
print(s.coinChange([1,2,5],11))
print(s.coinChange([2],3))
print(s.coinChange([1],0))

#[1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
