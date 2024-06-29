class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.votes = defaultdict(list)
        for p, t in zip(persons, times):
            self.votes[p].append(t)        

    def q(self, t: int) -> int:
        mx, winner = 0, -1
        pre = 0
        for p, times in self.votes.items():
            idx = bisect_right(times, t)
            if idx > mx:
                mx = idx
                winner = p
                pre = times[idx - 1]
            elif idx == mx:
                if times[idx-1] > pre:
                    winner = p
                    pre = times[idx-1]
        return winner
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)