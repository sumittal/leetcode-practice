import heapq
from typing import Dict, List, Set, Tuple


class Twitter:
    def __init__(self) -> None:
        # Each user's tweets remain in chronological order for reverse traversal.
        self.tweets: Dict[int, List[Tuple[int, int]]] = {}
        self.followees: Dict[int, Set[int]] = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # A global clock gives every tweet a total recency order.
        self.tweets.setdefault(userId, []).append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # A user's own tweets are always included even without an explicit follow.
        accounts = self.followees.get(userId, set()) | {userId}
        recent = []
        for account in accounts:
            tweets = self.tweets.get(account, [])
            if tweets:
                index = len(tweets) - 1
                timestamp, tweet_id = tweets[index]
                # Seed a merge heap with the newest tweet from each account.
                heapq.heappush(recent, (-timestamp, account, index, tweet_id))
        feed = []
        while recent and len(feed) < 10:
            # The most recent available tweet is emitted before older stream entries.
            _, account, index, tweet_id = heapq.heappop(recent)
            feed.append(tweet_id)
            previous_index = index - 1
            if previous_index >= 0:
                previous_time, previous_tweet = self.tweets[account][previous_index]
                # Advance only the account whose newest item was just consumed.
                heapq.heappush(
                    recent,
                    (-previous_time, account, previous_index, previous_tweet),
                )
        # Merging stops at ten even if followed accounts have more history.
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # Self-follow is harmless because feeds include the user's own account.
        self.followees.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Removing a missing relationship is a no-op, as required by the operation API.
        self.followees.get(followerId, set()).discard(followeeId)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5]
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]
    twitter.follow(3, 3)
    twitter.postTweet(3, 10)
    assert twitter.getNewsFeed(3) == [10]
    for tweet_id in range(12):
        twitter.postTweet(4, tweet_id)
    assert twitter.getNewsFeed(4) == list(range(11, 1, -1))
    print("All tests passed")
