import math

class Solution:
    def minEatingSpeed(self, piles, h):

        res = float('inf')

        bana_l, bana_r = 1 , max(piles)

        while bana_l<=bana_r:
            
            total_time = 0
            bana_m = (bana_l+bana_r)//2

            for pile in piles:
                total_time += math.ceil(pile/bana_m)
            
            if total_time > h: # eat too less
                bana_l = bana_m +1
            else: # eat too much
                res = min(res,bana_m)
                bana_r = bana_m -1

        return res 










        return res