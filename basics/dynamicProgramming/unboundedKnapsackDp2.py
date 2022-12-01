class Solution:

    """
    profit = [4,4,7,1]
    weight = [5,2,3,1]
    capacity = 8

    when using dp methods, think straightly start at index(3,8)
    
    """

    def unboundedKnapsackDp(self,profit,weight,capacity):

        self.profit = profit
        self.weight =weight
        self.N = len(profit)
        self.M = capacity
        prevRow = [0]*(self.M+1)

        for r in range(1,self.N):
            currentRow = [0]*(self.M+1)
            for c in range(1,self.M+1):

                skip = prevRow[c]
                include = 0
                if c-self.weight[r]>=0:
                    include =self.profit[r]+currentRow[c-self.weight[r]]
                currentRow[c]= max(include,skip)
            prevRow=currentRow
        return prevRow[self.M]

s =Solution()
profits= [4,4,7,1]
weights = [5,2,3,1]
capacity = 8
print(s.unboundedKnapsackDp(profits,weights,capacity))