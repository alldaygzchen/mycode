# best solution: only need the two previous value 
# save space
class Solution:
    def fibonacci_bottomup(self,n):

        if n <=1:
            return n

        record  = [0,1]
        start_idx =2
        while start_idx<=n:
            tmp = record[1]
            record[1]=record[0]+record[1]
            record[0] =tmp
            start_idx+=1
        return record[1]


        
        

s =Solution()
print(s.fibonacci_bottomup(5))
