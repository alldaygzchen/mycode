class Solution:
    def knapsack(self,profits,weights,capacity):
        self.profits =profits
        self.weights =weights
        self.capacity =capacity
        return self.bruteForce_postorder(0,capacity)
        
    #idx is the point you want to have answer
    def bruteForce_postorder(self,idx,capacity):
        if idx == len(self.profits):
            return 0

        ans = self.bruteForce_postorder(idx+1,capacity)
        
        newCapacity = capacity - self.weights[idx]
        if newCapacity>=0:
            p = self.profits[idx]+self.bruteForce_postorder(idx+1,newCapacity)
            ans = max (ans,p)
        else:
            return 0

        return ans

s =Solution()
profits= [4,4,7,1]
weights = [5,2,3,1]
capacity = 8
print(s.knapsack(profits,weights,capacity))

        
