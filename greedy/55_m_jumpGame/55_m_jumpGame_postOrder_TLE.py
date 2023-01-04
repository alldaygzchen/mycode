class Solution:
    def canJump(self, nums):
        self.nums =nums 
        self.cache ={}
        return self.dfs_postorder(0)
    
    def dfs_postorder(self,idx):
  
        # base case

        if idx in self.cache:
            return self.cache[idx]

        if idx == len(self.nums)-1:
            return True
        if idx >= len(self.nums):
            return False

        # formula
        for i in range(1,min(self.nums[idx],len(self.nums)-1-idx)+1):
        # for i in range(min(self.nums[idx],len(self.nums)-1-idx),0,-1):
            if self.dfs_postorder(idx+i):
                self.cache[idx] = True
                return self.cache[idx]

        self.cache[idx] =False
        return self.cache[idx]