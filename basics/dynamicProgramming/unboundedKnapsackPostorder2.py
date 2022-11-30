class Solution:

    """
    profit = [4,4,7,1]
    weight = [5,2,3,1]
    capacity = 8
    
    """

    def unboundedKnapsack(self,profit,weight,capacity):

        self.profit = profit
        self.weight =weight
        self.res = float("-inf")


        #postorder
        return self.dfs_postorder(capacity)

    def dfs_postorder(self,capacity):
        print(capacity,self.res)

        #base case:
        if capacity <0:
            return 0

        collect = []
        #formula
        for i in range(len(self.weight)):

            if capacity-self.weight[i]>=0:    
                self.res = max(self.res,self.dfs_postorder(capacity-self.weight[i])+self.profit[i])
            else:
                self.res = max(self.res,self.dfs_postorder(capacity-self.weight[i]))
        # print(self.res)
 
        return self.res 
        
        

s = Solution()
profit = [4,4,7,1]
weight = [5,2,3,1]
capacity = 8
print(s.unboundedKnapsack(profit,weight,capacity))


# class Solution:

#     """
#     profit = [4,4,7,1]
#     weight = [5,2,3,1]
#     capacity = 8
    
#     """

#     def unboundedKnapsack(self,profit,weight,capacity):

#         self.profit = profit
#         self.weight =weight
#         self.res = float("-inf")


#         #postorder
#         return self.dfs_postorder(capacity)

#     def dfs_postorder(self,capacity):

#         #base case:
#         if capacity <0:
#             return 0

#         collect = []
#         #formula
#         for i in range(len(self.weight)):

#             if capacity-self.weight[i]>=0:    
#                 collect.append(self.dfs_postorder(capacity-self.weight[i])+self.profit[i])
#             else:
#                 collect.append(self.dfs_postorder(capacity-self.weight[i]))
   
 
#         return max(collect)
        
        

# s = Solution()
# profit = [4,4,7,1]
# weight = [5,2,3,1]
# capacity = 8
# print(s.unboundedKnapsack(profit,weight,capacity))

        