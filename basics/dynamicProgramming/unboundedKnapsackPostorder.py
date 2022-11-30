class Solution:

    """
    profit = [4,4,7,1]
    weight = [5,2,3,1]
    capacity = 8
    
    """

    def unboundedKnapsack(self,profit,weight,capacity):

        self.profit = profit
        self.weight =weight


        #postorder
        return self.dfs_postorder(0,capacity)

    def dfs_postorder(self,i,capacity):

        #base case:
        if i == len(self.profit):
            return 0
        
        #formula
        #skip
        maxprofit = self.dfs_postorder(i+1,capacity)

        new_capacity = capacity -self.weight[i]
        if new_capacity>=0:
            p = self.dfs_postorder(i,new_capacity)+self.profit[i]
            maxprofit =max(maxprofit,p)

        return maxprofit

s = Solution()
profit = [4,4,7,1]
weight = [5,2,3,1]
capacity = 8
print(s.unboundedKnapsack(profit,weight,capacity))

        