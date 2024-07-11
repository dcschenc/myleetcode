# https://leetcode.com/problems/design-a-leaderboard/editorial/
from sortedcontainers import SortedList
class Leaderboard:
    def __init__(self):
        self.d = defaultdict(int)
        self.rank = SortedList()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.d:
            self.d[playerId] = score
            self.rank.add(score)
        else:
            self.rank.remove(self.d[playerId])
            self.d[playerId] += score
            self.rank.add(self.d[playerId])

    def top(self, K: int) -> int:
        return sum(self.rank[-K:])

    def reset(self, playerId: int) -> None:
        self.rank.remove(self.d.pop(playerId))


class Leaderboard:
    def __init__(self):
        self.scores = {}        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0           
        self.scores[playerId] += score        

    def top(self, K: int) -> int:
        # scores = [score for _, score in self.scores.items()]
        # scores.sort(reverse=True)
        # return sum(scores[:K])    ## N*Log(N)
        heap = []
        for x in self.scores.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)   ### O(K) + O(NlogK)
        # res = 0
        # while heap:
        #     res += heapq.heappop(heap)
        return sum(heap)

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)