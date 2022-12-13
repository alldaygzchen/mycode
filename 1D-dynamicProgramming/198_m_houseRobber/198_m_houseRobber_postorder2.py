class Solution:
    """
    dp = [] #max profit
  
    """

    def rob(self, nums):
        self.nums = nums
        self.cache = [-1]*(len(nums)) 
        return self.dfs_postorder(len(nums)-1) # the nth
        

    def dfs_postorder(self,idx):
        # print(idx)

        # base case
        if idx == 0:
            self.cache[idx]=self.nums[0]
            return self.cache[idx]
        
        if idx ==1:
            self.cache[idx]=max(self.nums[0],self.nums[1])
            return self.cache[idx]

        if self.cache[idx] != -1:
            return self.cache[idx]

        # formula

        self.cache[idx] = max(self.dfs_postorder(idx-1),self.dfs_postorder(idx-2)+self.nums[idx])
        return self.cache[idx]
s = Solution()
print(s.rob([1,2,3,1]))
print(s.rob([2,7,9,3,1]))
