class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                last_idx = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][last_idx]
                min_heap.append([time, tweetId, followeeId, last_idx - 1])

        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            time, tweetId, userId, idx = heapq.heappop(min_heap)
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tweetMap[userId][idx]
                heapq.heappush(min_heap, [time, tweetId, userId, idx - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
