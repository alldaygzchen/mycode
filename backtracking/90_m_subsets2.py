class Solution(object):
    def subsetsWithDup(self, nums):
        self.res = []
        nums.sort() # sorted (for duplicates when using while loop)
        self.nums = nums
        self.helper([],0)

        return self.res

    def helper(self,cur,idx): # self.res

        #edge case
        if idx>=len(self.nums):
            self.res.append(cur[:])
            return

        cur.append(self.nums[idx])
        # left side => at least contain one value of curr index
        self.helper(cur,idx+1)
        cur.pop()
        # right side => Do not contain the value of curr index
        while idx+1<len(self.nums) and self.nums[idx]==self.nums[idx+1]:
            idx+=1
        self.helper(cur,idx+1)
        