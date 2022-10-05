class Solution:
    def search(self, nums, target):

        res =-1
        l= 0
        r = len(nums)-1

        while l<=r:
            m = (l+r)//2

            if target == nums[m]:
                return m

            if nums[m]>=nums[l]:

                if nums[l]<=target and target <= nums[m]:
                    r= m-1
                else:
                    l=m+1

            else:
                if nums[m]<=target and target<=nums[r]:
                    l =m+1
                else:
                    r =m-1


        return res
