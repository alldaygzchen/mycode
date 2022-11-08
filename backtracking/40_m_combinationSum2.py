#can use only one time and  arrays may contain same value
# class Solution:
#     def combinationSum2(self,candidates,target):

#         self.res = []
#         candidates.sort() # sorted (for duplicates when using while loop)
#         self.candidates = candidates
#         self.target =target
#         self.helper([],0)

#         return self.res


#     def helper(self,cur,idx):
        
#         # print('cur',cur)
        
#         #edge case
        
#         if cur and sum(cur)>self.target :
#             return
        
#         if cur and sum(cur)==self.target :
#             self.res.append(cur[:])
#             return

#         if idx>=len(self.candidates):
#             return

#         cur.append(self.candidates[idx])
#         # left side => at least contain one value of curr index
#         self.helper(cur,idx+1)
#         cur.pop()
#         # right side => Do not contain the value of curr index
#         while idx+1<len(self.candidates) and self.candidates[idx]==self.candidates[idx+1]:
#             idx+=1
#         self.helper(cur,idx+1)

class Solution:
    def combinationSum2(self,candidates,target):
        candidates.sort()
        self.res = []
        self.candidates = candidates
        self.helper([],0,target)
        return self.res

    def helper(self,cur,idx,target):
        

        # edge case: target == 0 
        if target == 0:
            self.res.append(cur[:])
            return 
        
        # edge case: target<0
        if target <0:
            return

        # vertical has no prev, while horizontal has
        prev =-1 

        
        # for loop (make sure each parallel node is unequal[prevent duplicate result])
        for i in range(idx,len(self.candidates)):

            # edge case: pop(previous) == new value =>pass
            if self.candidates[i] == prev:
                continue

            # append new value to curr
            cur.append(self.candidates[i])
            
            # recursion helper function 
            self.helper(cur,i+1,target-self.candidates[i])

            # pop added new value
            prev = cur.pop()
            




