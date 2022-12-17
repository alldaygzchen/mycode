class Solution:
    def canPartition(self, nums):

        if sum(nums)%2:
            return False

        dp =set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums)-1,-1,-1):
            temp = set()
            for t in dp:
                if (t+nums[i])==target:
                    return True
                temp.add(t+nums[i])
                temp.add(t)
            dp =temp
        return False



s =Solution()
print(s.canPartition([1,5,11,5]))