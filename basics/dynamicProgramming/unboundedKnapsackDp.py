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
        self.dp = [[0]*(self.M+1) for _ in range(self.N)]

        for c in range(self.M+1):
            if c>=self.weight[0]:
                self.dp[0][c] = self.profit[0]

        for r in range(self.N):
            self.dp[r][0] = 0

        for r in range(1,self.N):
            for c in range(1,self.M+1):

                skip = self.dp[r-1][c]
                include = 0
                if c-self.weight[r]>=0:
                    include =self.profit[r]+self.dp[r][c-self.weight[r]]
                self.dp[r][c]= max(include,skip)

        return self.dp[self.N-1][self.M]

s =Solution()
profits= [4,4,7,1]
weights = [5,2,3,1]
capacity = 8
print(s.unboundedKnapsackDp(profits,weights,capacity))