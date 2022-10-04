class Solution:
    def search(self, nums, target):

        res = -1
        l=0
        r=len(nums)-1

        while l<=r: #maybe no return 
            m= (l+r)//2 #include left partition

            if nums[m]==target:
                return m

            elif nums[m]<target:
                l = m+1
            else:
                r = m-1

        return res