#prevent duplicate check 
#trick 
# sort and clean duplicate result 

class Solution:
    def threeSum(self, nums):
        
        res = []
        nums.sort()
        
        for s in range(len(nums)):

            if s>=1 and nums[s-1]==nums[s]:
                continue

            l,r= s+1,len(nums)-1

            while l<r:

                current = nums[s]+nums[l]+nums[r]

                if current==0:
                    res.append([nums[s],nums[l],nums[r]])
                    l+=1
                    while nums[l-1] == nums[l] and l<r:
                        l+=1
                elif current>0:
                    r-=1
                else:
                    l+=1
        return res

s= Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))