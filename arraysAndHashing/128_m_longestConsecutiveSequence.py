class Solution:
    def longestConsecutive(self,nums):

        result = 0
        
        nums_set = set(nums)

        for num in nums_set:

            if num-1 in nums_set:
                continue
            
            length=0
            while num in nums_set:
                num+=1
                length+=1
                
                result = max(result,length)

        return result