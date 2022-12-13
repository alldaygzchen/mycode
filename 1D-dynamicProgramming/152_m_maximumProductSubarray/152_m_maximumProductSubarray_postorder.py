class Solution:
    def maxProduct(self, nums):
        self.nums = nums
        self.res =max(nums)
        self.dfs_postorder(0)
        return self.res

    def dfs_postorder(self,idx):

        # base case
        if idx == len(self.nums):
            return (1,1)
        
        # formula
        prev_min, prev_max= self.dfs_postorder(idx+1)
        var = self.nums[idx]

        if var ==0: 
            curMax =1
            curMin =1
            self.res = max(self.res,0)
        else:
            curMax = max(prev_min*var,prev_max*var,var)
            curMin = min(prev_min*var,prev_max*var,var)
            self.res = max(self.res,curMax)
        return (curMin,curMax)

s = Solution()
print(s.maxProduct([2,3,-2,4]))
print(s.maxProduct([-2,0,-1]))
print(s.maxProduct([0,2]))