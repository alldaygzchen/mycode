class Solution:
    def maxSubArray(self, nums):

        maxSum = float('-inf')
        curSum = 0

        for n in nums:
            curSum = max(curSum+n, n)
            maxSum = max(maxSum, curSum)
        return maxSum

    # def kadanes(nums):
    #     maxSum = nums[0]
    #     curSum = 0

    #     for n in nums:
    #         curSum = max(curSum, 0)
    #         curSum += n
    #         maxSum = max(maxSum, curSum)
    #     return maxSum



    # def maxSubArray(self, nums):

    # res = float('-inf')
    # total =0

    # for num in nums:
        
    #     total+=num
    #     res = max(res, total)
        

    #     if total<0:
    #         total = 0 
    # return res