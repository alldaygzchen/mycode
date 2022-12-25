class Solution(object):
    """
    compare with 309
    It is postorder not inorder
    """
    def findTargetSumWays(self, nums, target):
        self.nums = nums
        self.target =target
        self.cache = {}
        return self.dfs_postorder(0,0)
    def dfs_postorder(self,i,t): # considering adding or substracting
        # base case 
        if i==len(self.nums):
            return 1 if t==self.target else 0

        if (i,t) in self.cache:
            return self.cache[(i,t)] 


        # formula 
        self.cache[(i,t)] = self.dfs_postorder(i+1,t+self.nums[i]) + self.dfs_postorder(i+1,t-self.nums[i])
        return self.cache[(i,t)] 