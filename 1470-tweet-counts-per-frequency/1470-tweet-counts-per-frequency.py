from sortedcontainers import SortedList
class TweetCounts:
    def __init__(self):
        self.tweets = defaultdict(SortedList)        

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].add(time)        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        times = self.tweets[tweetName]
        ans = []
        minutes = 60        
        if freq == 'minute':
            minutes = 59
        elif freq == 'hour':
            minutes = 3599
        else:
            minutes = 86399
        while startTime <= endTime:
            left = bisect_left(times, startTime)
            end = min(startTime + minutes, endTime)
            right = bisect_right(times, end)
            ans.append(right - left)
            startTime += minutes + 1
        return ans



# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)