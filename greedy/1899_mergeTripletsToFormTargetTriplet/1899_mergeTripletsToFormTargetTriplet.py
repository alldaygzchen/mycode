class Solution:
    def mergeTriplets(self, triplets, target):
        
        good = set()

        for l in triplets:
            if l[0] > target[0] or l[1]>target[1] or l[2]>target[2]:
                continue
            
            if l[0] == target[0]:
                good.add(0)

            if l[1] == target[1]:
                good.add(1)

            if l[2] == target[2]:
                good.add(2)

        return len(good) == 3