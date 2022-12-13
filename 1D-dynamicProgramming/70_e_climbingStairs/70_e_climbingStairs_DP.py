class Solution:
    """
    Addition notes: normally postorder is the top-down 
    
    # make sure what is my function:
    climbStairs(5) = how many steps
    # how do we calculate climbStairs(5)
    climbStairs(5) = climbStairs(4) +climbStairs(3)
    # It is a dp problem
    # bottom up 
    # declare the base case and calculate


    """
    def climbStairs(self, n):

        # declare the base case and calculate
        if n<=2:
            return n

        pre=1
        curr=2
        
        for i in range(3,n+1):

            tmp=pre

            pre = curr
            curr = tmp+curr

        
        return curr


    # def climbStairs(self, n):

        # if n<=2:
        #     return n

        # # declare the base case and calculate
        # dp = [0]*(n+1)
        # dp[0]=0
        # dp[1]=1
        # dp[2]=2
        
        
        # for i in range(3,n+1):
        #     dp[i]= dp[i-1]+dp[i-2]
        
        # return dp[n]

s =Solution()
print(s.climbStairs(5))