class Solution:

    """

    Memo vs Dp:
    Memo does not run all the point, just record
    DP does run all the point 

    Suggestion:
    rows and cols start with 0

    """
    def knapsackDp(self,profits,weights,capacity):
        
        self.profits =profits
        self.N = len(profits)
        self.M = capacity
        prevRow = [0]*(self.M+1)

        self.weights =weights
        self.capacity =capacity
        

        for c in range(self.M+1):
            if self.weights[0]<=c:
                prevRow[c] = self.profits[0]

        for r in range(1,self.N):
            curRow =[0]*(self.M+1)
            for c in range(1,self.M+1):

                skip = prevRow[c]
                include = 0 
                if c-self.weights[r]>=0:
                    include = self.profits[r]+prevRow[ c-self.weights[r]]
                curRow[c] = max(include,skip)
            prevRow=curRow
        return prevRow[self.M]


        

s =Solution()
profits= [4,4,7,1]
weights = [5,2,3,1]
capacity = 8
print(s.knapsackDp(profits,weights,capacity))
