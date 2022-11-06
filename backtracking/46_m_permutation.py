class Solution:

    def permute(self,nums):#list

        res = []
        
        if len(nums)==1:
            return [nums[:]]

        for i in range(len(nums)):
            pop_init = nums.pop(0)

            perms=self.permute(nums)

            for perm in perms:
                perm.append(pop_init)
            res.extend(perms)
            nums.append(pop_init)
        return res 