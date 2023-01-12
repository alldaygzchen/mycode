
class Solution:
    def canCompleteCircuit(self, gas, cost):
        
        if sum(gas)<sum(cost):
            return -1

        res= 0
        total =0
        
        for idx in range(len(gas)):
            total += gas[idx]-cost[idx]

            if total<0:
                total =0
                res = idx+1
                

        return res