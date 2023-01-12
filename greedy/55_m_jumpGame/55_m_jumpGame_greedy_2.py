class Solution:
    def canJump(self, nums):
        goal = len(nums)-1

        for idx in range(len(nums)-2,-1,-1):
            if idx+nums[idx]>=goal:
                goal = idx
        return goal == 0