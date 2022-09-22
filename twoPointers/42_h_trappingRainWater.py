# trick: 
# left_max = max(left_max ,height[l])
# right_max = max(height[r],right_max)
# left_max<=right_max

class Solution:
    def trap(self, height):

        l,r =0,len(height)-1
        res = 0

        left_max =height[l]
        right_max = height[r]
        while l<r:

            if left_max<=right_max:
                l+=1
                left_max = max(left_max ,height[l])
                res+=left_max-height[l]

            else:
                r-=1
                right_max = max(height[r],right_max)
                res+=right_max-height[r]

        return res

s = Solution()
s.trap([4,2,0,3,2,5])



# class Solution:
#     def trap(self, height):

#         l,r =1,len(height)-2
#         res = 0

#         left_max =height[l-1]
#         right_max = height[r+1]
#         while l<r:

#             if left_max<=right_max:
#                 left_max = max(left_max ,height[l])
#                 print('left_max',left_max)
#                 print('height[l]',height[l])
#                 res+=left_max-height[l]
#                 l+=1

#             else:
#                 right_max = max(height[r],right_max)
#                 print('right_max ',right_max )
#                 print('height[r]',height[r])
#                 res+=right_max-height[r]
#                 r-=1

#         return res

# s = Solution()
# s.trap([4,2,0,3,2,5])

