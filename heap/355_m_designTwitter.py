from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) #userId:[[time1,tweetIds],[time2,tweetIds],...]
        self.followMap = defaultdict(set) #userId:set of followeeId

    def postTweet(self,userId,tweetId):
        self.tweetMap[userId].append([self.time,tweetId])
        self.time +=1


    def getNewsFeed(self,userId):
        res = []
        minHeap = []

        self.followMap[userId].add(userId)

        #initial

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                time,tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap,[-1*time,tweetId,followeeId,index-1]) # add the last tweet of each followees

        #run procees
        while minHeap and len(res)<10:
            time_neg,tweetId,followeeId,index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index>=0:
                time,tweetId= self.tweetMap[followeeId][index]
                heapq.heappush(minHeap,[time*-1,tweetId,followeeId,index-1])

        return res

    def follow(self,followerId,followeeId):
        self.followMap[followerId].add(followeeId)

    def unfollow(self,followerId,followeeId):
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


