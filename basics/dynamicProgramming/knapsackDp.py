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
        self.dp = [[0]*(self.M+1) for _ in range(self.N)]

        self.weights =weights
        self.capacity =capacity
        
        for r in range(self.N):
               self.dp[r][0]=0

        for c in range(self.M+1):
            if self.weights[0]<=c:
                self.dp[0][c] = self.profits[0]

        for r in range(1,self.N):
            for c in range(1,self.M+1):

                skip = self.dp[r-1][c]
                include = 0 
                if c-self.weights[r]>=0:
                    include = self.profits[r]+self.dp[r-1][ c-self.weights[r]]
                self.dp[r][c] = max(include,skip)
        return self.dp[self.N-1][self.M]


        

s =Solution()
profits= [4,4,7,1]
weights = [5,2,3,1]
capacity = 8
print(s.knapsackDp(profits,weights,capacity))

        
