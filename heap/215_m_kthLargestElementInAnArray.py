#Quick select
# class Solution:

#     def findKthLargest(self,nums,k):
#         self.nums = nums
#         self.k = len(self.nums)-k #the len(nums)-kth  index
#         return self.helper(0,len(self.nums)-1)



#     # attention
#     # recursion using repeated function not postorder or inorder
#     # self.nums and self.k
#     def helper(self,left,right):
        
#         pivot = self.nums[right]
#         partition = left

#         for i in range(left,right):#does not include right
#             if self.nums[i]<=pivot:
#                 self.nums[partition],self.nums[i] = self.nums[i],self.nums[partition] #same or swap
#                 partition+=1
#         self.nums[partition],self.nums[right] = self.nums[right],self.nums[partition] #same or swap

#         if partition>self.k:
#             return self.helper(left,partition-1)

#         elif partition<self.k:
#             return self.helper(partition+1,right)
#         else:
#             return self.nums[partition]


# class Solution2:
#     def partition(self, nums: List[int], left: int, right: int) -> int:
#         pivot, fill = nums[right], left

#         for i in range(left, right):
#             if nums[i] <= pivot:
#                 nums[fill], nums[i] = nums[i], nums[fill]
#                 fill += 1

#         nums[fill], nums[right] = nums[right], nums[fill]

#         return fill

#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k = len(nums) - k
#         left, right = 0, len(nums) - 1

#         while left < right:
#             pivot = self.partition(nums, left, right)

#             if pivot < k:
#                 left = pivot + 1
#             elif pivot > k:
#                 right = pivot - 1
#             else:
#                 break

#         return nums[k]

