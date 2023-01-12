class Solution:
    def canJump(self, nums):

        max_reach = 0

        for idx in range(len(nums)-1):
            if idx == max_reach and nums[idx]==0:
                return False
            max_reach = max(max_reach,idx + nums[idx])
        return True