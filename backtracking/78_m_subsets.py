class Solution:
    def subsets(self, nums):

        self.res = []
        self.nums = nums
        self.helper(0,[])

        return self.res


    def helper(self,i,curr):
        if i>=len(self.nums):
            self.res.append(curr[:])
            return 


        curr.append(self.nums[i])
        self.helper(i+1,curr)
        curr.pop()
        self.helper(i+1,curr)


