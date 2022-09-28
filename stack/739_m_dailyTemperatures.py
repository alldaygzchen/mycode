class Solution:
    def dailyTemperatures(self, temperatures):

        res = [0]*len(temperatures)
        stack = [] 

        for idx,temp in enumerate(temperatures):

            while stack and stack[-1][1]<temp:
                stack_idx,stack_temp = stack.pop()
                res[stack_idx] = idx-stack_idx
            
            stack.append([idx,temp])

        return res
        
