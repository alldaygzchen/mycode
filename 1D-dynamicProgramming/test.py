a= float('inf')
print(a==float('inf'))

class Solution(object):
    def __init__(self):
        self.mem = {0: 0}
    
    def coinChange(self, coins, amount):
		
        coins.sort()
        minCoins = self.getMinCoins(coins, amount)
        
        if minCoins == float('inf'):
            return -1
        
        return minCoins
        
    def getMinCoins(self, coins, amount):
        if amount in self.mem:
            return self.mem[amount]
        
        minCoins = float('inf')
        
        for c in coins:
            if amount - c >=  0:
                numCoins = self.getMinCoins(coins, amount - c) + 1
                minCoins = min(numCoins, minCoins)
        
        self.mem[amount] = minCoins
        
        return minCoins