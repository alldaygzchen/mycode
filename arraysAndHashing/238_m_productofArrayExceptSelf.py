class Solution:
    def productExceptSelf(self, nums):

        res = [1 for _ in nums]
        accu_left_mul =1
        accu_right_mul =1 

        for idx in range(len(nums)):
            res[idx]= accu_left_mul
            accu_left_mul*=nums[idx]


        for idx in range(len(nums)-1,-1,-1):
            res[idx]*= accu_right_mul
            accu_right_mul*=nums[idx]

        return res

s = Solution()
print(s.productExceptSelf([1,2,3,4]))