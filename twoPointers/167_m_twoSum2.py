# trick
#hashmap => do not need order
#two pointer => needs to be in order


class Solution:
    def twoSum(self, nums, target ):
        
        l=0
        r= len(nums)-1
        res = []

        while l<r:

            current = nums[l] +nums[r]

            if current == target:
                res.append(l+1)
                res.append(r+1)
                return res

            if current<target:
                l+=1
            elif current>target:
                r-=1

        return res