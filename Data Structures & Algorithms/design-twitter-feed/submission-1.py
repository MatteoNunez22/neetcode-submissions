class Twitter:

    def __init__(self):
        self.users = []
        self.tweets = []
        self.tweet_authors = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append(tweetId)
        self.tweet_authors[tweetId] = userId

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        i = len(self.tweets) - 1
        while i >= 0:
            tweet = self.tweets[i]
            if (self.tweet_authors[tweet] == userId or (userId in self.following and
                self.tweet_authors[tweet] in self.following[userId])):
                feed.append(tweet)
            if len(feed) == 10:
                break
            i -= 1

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].discard(followeeId)
