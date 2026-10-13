class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        self.followers[userId].add(userId)
        heap = []
        for follower in self.followers[userId]:
            if self.tweets[follower]:
                index = len(self.tweets[follower])-1
                count, tweet = self.tweets[follower][index]
                heapq.heappush(heap, (count, tweet, index-1, follower))

        while heap and len(res) < 10:
            count, tweet, index, follower = heapq.heappop(heap)
            res.append(tweet)
            if index >= 0:
                count, tweet = self.tweets[follower][index]
                heapq.heappush(heap, (count, tweet, index-1, follower))    
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)        


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            return
        self.followers[followerId].remove(followeeId)
        
