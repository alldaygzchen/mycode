class Solution:
    def maxCoins(self, nums):
        self.nums = [1]+nums+[1]
        self.cache = [[-1]*len(self.nums) for _ in range(len(self.nums))]
        return self.dfs_postorder(1,len(self.nums)-2)

    def dfs_postorder(self,l,r):
        if l>r:
            return 0
        if self.cache[l][r]!=-1:
            return self.cache[l][r]
        
        for i in range(l,r+1):
            coin = self.nums[l-1] * self.nums[i] * self.nums[r+1]
            coin += self.dfs_postorder(l,i-1) + self.dfs_postorder(i+1,r)
            self.cache[l][r]= max(self.cache[l][r],coin)
        return self.cache[l][r]
