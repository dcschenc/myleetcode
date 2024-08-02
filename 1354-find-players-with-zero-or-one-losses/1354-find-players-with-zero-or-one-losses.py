class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2225.Find%20Players%20With%20Zero%20or%20One%20Losses
        wins, loses = defaultdict(int), defaultdict(int)
        for w, l in matches:
            wins[w] += 1
            loses[l] += 1
        ans = []       
        wins = list(set(wins.keys()) - set(loses.keys()))
        wins.sort()
        loses = [l for l, c in loses.items() if c == 1]
        loses.sort()
        return [wins, loses]