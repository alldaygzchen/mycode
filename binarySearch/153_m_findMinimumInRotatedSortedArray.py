class Solution:
    def findMin(self, nums):
        res = float('inf')
        l = 0 
        r = len(nums)-1

        while l<=r:
            if nums[l]<nums[r]:
                res = min(res,nums[l])
                break

            m = (l+r)//2

            res = min(res,nums[m])

            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1

        return res


# class Solution:
#     def findMin(self, nums):
#         res = float('inf')
#         l = 0 
#         r = len(nums)-1

#         while l<=r:
#             print(l,r)
#             if nums[l]<=nums[r]:
#                 m = (l+r)//2
#                 res = min(res,nums[m])
#                 r = m-1
#                 continue
                


#             m = (l+r)//2

#             res = min(res,nums[m])

#             if nums[m] >= nums[l]:
#                 l = m+1
#             else:
#                 r = m-1

#         return res


s=Solution()
print(s.findMin([4,5,6,7,0,1,2]))