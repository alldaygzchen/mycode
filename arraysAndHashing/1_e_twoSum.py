class Solution:
    def twoSum(self, nums, target ):
        
        res= []
        prev_map={} #value=>index
        
        for i,e in enumerate(nums):


            # if e not in prev_map: 每次都發生放在最後面 用if 做排除
            #     prev_map[e]=i
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
            # if target-e in prev_map:
            #     res = [i,prev_map[target-e]]
            #     return res
            
            # prev_map[e]=i
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            if target-e in prev_map:
                res = [i,prev_map[target-e]]
                return res

            
            
            if e not in prev_map:
                prev_map[e]=i


        return res
