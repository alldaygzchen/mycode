import heapq
class Solution:
    def isNStraightHand(self,hand, groupSize):
        
        if len(hand) % groupSize:
            return False

        count = {} 
        for e in hand:
            count[e] = 1 + count.get(e,0)

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            left = minH[0]
            right = minH[0]+groupSize
            for i in range(left,right):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=minH[0]:
                        return False
                    heapq.heappop(minH)
        return True