

class Solution:

    "dp = min coin to the objective"

    def coinChange(self, coins, amount):

        self.coins = coins
        self.dp = {0: 0}
        res = self.dfs_postorder(amount)
        if res == float('inf'):
              return -1
        return res


    def dfs_postorder(self,idx):
        
        # base case

        if idx in self.dp :
            return self.dp[idx]


        res = float('inf')
        
        
        #formula
        for c in self.coins:
            if idx-c >=0:
                res = min (res,1+self.dfs_postorder(idx-c))
        self.dp[idx] = res
        
        return self.dp[idx]



s = Solution()
print(s.coinChange([1,2,5],11))
print(s.coinChange([2],3))
print(s.coinChange([1],0))

#[1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
