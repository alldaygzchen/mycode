class Solution:
    def containsDuplicate(self, nums):
        
        res = False
        hashSet= set()
        
        for ele in nums:
            
            # if ele not in hashSet:
            #     hashSet.add(ele)
            # else:
            #     res = True
            #     return res

            if ele in hashSet:
                res =True
                return res

            if ele not in hashSet:
                hashSet.add(ele)
        
        return res