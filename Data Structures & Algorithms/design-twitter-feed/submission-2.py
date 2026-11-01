class Twitter:

    def __init__(self):
        self.users = []
        self.tweets = []
        self.tweet_authors = {}
        self.followMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append(tweetId)
        self.tweet_authors[tweetId] = userId

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        i = len(self.tweets) - 1
        while i >= 0:
            tweet = self.tweets[i]
            if (self.tweet_authors[tweet] == userId or (self.tweet_authors[tweet] in self.followMap.get(userId, []))):
                feed.append(tweet)
            if len(feed) == 10:
                break
            i -= 1

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].discard(followeeId)
