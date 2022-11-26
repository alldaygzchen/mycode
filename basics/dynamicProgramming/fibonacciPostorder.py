class Solution:
    def fibonacci_postorder_dp(self,n,cache):

        #base case
        if n <=1:
            return n
        # faster
        if n in cache:
            return cache[n]

        #record the result n at cache
        cache[n] = self.fibonacci_postorder_dp(n-1)+self.fibonacci_postorder_dp(n-1)
        return cache[n] 

s =Solution()
print(s.fibonacci_postorder_dp(5,{}))
