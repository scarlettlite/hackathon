from collections import deque, defaultdict
from itertools import islice
import heapq
class User:
    def __init__(self, id):
        self.id = id
        self.followed = set()
        self.tweets = deque()

    def postTweet(self, tweetid, time):
        self.tweets.appendleft((time, tweetid))

    def gettop10tweets(self):
        return list(islice(self.tweets,0,10))

    def follow(self, followed):
        self.followed.add(followed)

    def unfollow(self, followed):
        if followed in self.followed:
            self.followed.remove(followed)

    def getnewsfeed(self):
        newsfeed =  self.gettop10tweets()
        for f in self.followed:
            if f.id != self.id:
                newsfeed.extend(f.gettop10tweets())
        return [x[1] for x in heapq.nlargest(10, newsfeed, key=lambda x: x[0])]

class Mydefaultdict(defaultdict):
    def __missing__(self, key):
        self[key] = new = self.default_factory(key)
        return new
    
class Twitter:
    def __init__(self):
        self.users = Mydefaultdict(User)
        self.time = 0

    def postTweet(self, userid, tweetid):
        self.time += 1
        self.users[userid].postTweet(tweetid, self.time)

    def follow(self, follower, followed):
        self.users[follower].follow(self.users[followed])

    def unfollow(self, follower, followed):
        self.users[follower].unfollow(self.users[followed])

    def getNewsFeed(self, userid):
        return self.users[userid].getnewsfeed()