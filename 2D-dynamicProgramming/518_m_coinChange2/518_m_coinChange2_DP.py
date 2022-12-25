class Solution(object):
    

    def change(self, amount, coins):


        self.dp = [[None]*(len(coins)+1) for _ in range(amount+1)]
        self.dp[0] = [1]*(len(coins))+[0]
        for r in range(amount+1):
            self.dp[r][-1]=0

        for r in range(1,amount+1):
            for c in range(len(coins)-1,-1,-1):
                self.dp[r][c] =self.dp[r][c+1]
                if r-coins[c]>=0:
                    self.dp[r][c]+=self.dp[r-coins[c]][c]

        return self.dp[amount][0]

s =Solution()
print(s.change(5,[1,2,5]))