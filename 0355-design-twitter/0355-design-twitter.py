import heapq

class Twitter:
    def __init__(self):
        self.tweets = {}
        self.follows = {}        
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []        
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followee = set()
        if userId in self.follows:
            followee = set(self.follows[userId])
        followee.add(userId)
        tweets = []       
        for user in followee:
            if user not in self.tweets:
                continue
            for timeId, tweetId in self.tweets[user][::-1][:10]:
                tweets.append((timeId, tweetId))
                
        heapq.heapify(tweets)
        while len(tweets) > 10:
            heapq.heappop(tweets)
        res = []
        while len(tweets) > 0:
            res.append(heapq.heappop(tweets)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = []
        self.follows[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)