class Solution:
    def knapsack(self,profits,weights,capacity):
        
        self.profits =profits
        self.N = len(profits)
        self.M = capacity
        self.cache = [[-1]*(self.M+1) for _ in range(self.N)]

        self.weights =weights
        self.capacity =capacity
        self.dfs_postorder(0,capacity)
        # print(self.cache)
        return self.cache[0][capacity]

        
    #idx is the point you want to have answer
    def dfs_postorder(self,idx,capacity):
        if idx == len(self.profits):
            return 0
        if self.cache[idx][capacity] != -1:
            return self.cache[idx][capacity]



        self.cache[idx][capacity] = self.dfs_postorder(idx+1,capacity)
        
        newCapacity = capacity - self.weights[idx]
        if newCapacity>=0:
            p = self.profits[idx]+self.dfs_postorder(idx+1,newCapacity)
            self.cache[idx][capacity] = max (self.cache[idx][capacity],p)

        return self.cache[idx][capacity]

s =Solution()
profits= [4,4,7,1]
weights = [5,2,3,1]
capacity = 8
print(s.knapsack(profits,weights,capacity))

        
