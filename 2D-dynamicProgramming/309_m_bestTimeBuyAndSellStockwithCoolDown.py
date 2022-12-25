class Solution(object):
    def maxProfit(self, prices):
        self.prices = prices 
        self.cache = {}
        return self.dfs_postorder(0,True)
        

    def dfs_postorder(self,idx,buy):
        
        # considering cooldown skip 2 indexes
        if idx >= len(self.prices):
            return 0
        if (idx,buy) in self.cache:
            return self.cache[(idx,buy)]

        if buy:
            self.cache[(idx,buy)] = max(self.dfs_postorder(idx+1,not buy)-self.prices[idx],self.dfs_postorder(idx+1,buy))
        else:
            self.cache[(idx,buy)] = max(self.dfs_postorder(idx+2,not buy)+self.prices[idx],self.dfs_postorder(idx+1,buy))

        return self.cache[(idx,buy)]