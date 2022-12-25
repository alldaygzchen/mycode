class Solution(object):
    
    """
    322 CoinChange: uses for loop since does not consider combination
    518 CoinChange2: pick or not pick since considering combination
    
    
    """
    def change(self, amount, coins):

        self.amount  = amount
        self.coins = coins
        self.cache = {}
        return self.dfs_postorder(0,0)

    def dfs_postorder(self,idx,a):
        
        if idx ==len(self.coins):
            return 0
        if a == self.amount:
            return 1
        if a > self.amount:
            return 0
        if (idx,a) in self.cache:
            return self.cache[(idx,a)]

        self.cache[(idx,a)] = self.dfs_postorder(idx,a+self.coins[idx])+self.dfs_postorder(idx+1,a)
        return self.cache[(idx,a)]
