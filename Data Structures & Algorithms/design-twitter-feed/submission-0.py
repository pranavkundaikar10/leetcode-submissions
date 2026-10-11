class Twitter:

    def __init__(self):
        self.TweetMap = defaultdict(list)
        self.FollowMap = defaultdict(set)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.TweetMap[userId].append((self.count, tweetId))
        self.count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.FollowMap[userId].add(userId)
        res = []
        heap = []
        for follower in self.FollowMap[userId]:
            if follower not in self.TweetMap:
                continue
            index = len(self.TweetMap[follower])-1
            count, tweetId = self.TweetMap[follower][index]
            heapq.heappush_max(heap, (count, tweetId, follower, index-1))
        
        while heap and len(res) < 10:
            count, tweetId, follower, index = heapq.heappop_max(heap)
            res.append(tweetId)
            if index >= 0:
                nxtCount, nextTweet = self.TweetMap[follower][index]
                heapq.heappush_max(heap, (nxtCount, nextTweet, follower, index-1))

        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.FollowMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.FollowMap[followerId]:
            return
        self.FollowMap[followerId].remove(followeeId)
        
