#can use same values multiple time but arrays only contain different value
class Solution:
    def combinationSum(self,candidates,target):
        self.res = []
        self.target =target
        self.candidates =candidates
        self.helper(0,[])
        return self.res

    def helper(self,idx,cur):


        if sum(cur)==self.target:
            self.res.append(cur[:])
            return 

        if idx>=len(self.candidates) or sum(cur)>self.target:
            return

        cur.append(self.candidates[idx])
        self.helper(id,cur)
        cur.pop()
        self.helper(idx+1,cur)

